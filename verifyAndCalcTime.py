#!/usr/bin/env python3

import os, json
from datetime import datetime

DIR = "%s/project/pubsub/outputs/" % os.environ["HOME"]

class Packet:

	def __init__(self, topic_id, pkt_ts, src_ip, log_ts, content="."):
		self.topic_id = topic_id
		self.pkt_ts = pkt_ts
		self.src_ip = src_ip
		self.log_ts = log_ts
		self.content = content

	def __hash__(self):
		return hash("%d%d%s" % (self.topic_id, self.pkt_ts, self.src_ip))

	def __eq__(self, other):
		return self.topic_id == other.topic_id and self.pkt_ts == other.pkt_ts and self.src_ip == other.src_ip

	def __repr__(self):
		return "[topic=%d, pkttime=%d, src=%s, logtime=%d, content=%s]" % (self.topic_id, self.pkt_ts, self.src_ip, self.log_ts, self.content)

	def __str__(self):
		return "[topic=%d, pkttime=%d, src=%s, logtime=%d, content=%s]" % (self.topic_id, self.pkt_ts, self.src_ip, self.log_ts, self.content)

	def diff_log_ts(self, other):
		return abs(self.log_ts - other.log_ts)

def find_diff(d1, d2):
	data = {}
	for src1, pkts1 in d1.items():
		add = 0
		cnt = 0
		for pkt1 in pkts1:
			for src2, pkts2 in d2.items():
				for pkt2 in pkts2:
					if pkt1 == pkt2:
						cnt += 1
						add += pkt1.diff_log_ts(pkt2)
		avg = 0.0 if cnt == 0 else float(add) / cnt
		data[src1] = avg
	return data

pubp = {}
subp = {}
notp = {}
resp = {}

pubcnt = [0] * 64

for filename in os.listdir(DIR):
	f = open("%s%s" % (DIR, filename), 'r')

	curr_ip = "10.0.%s.%s" % (filename[1:-4], filename[1:-4])

	pubp[curr_ip] = set()
	subp[curr_ip] = set()
	notp[curr_ip] = set()
	resp[curr_ip] = set()

	for line in f.readlines():
		if "sending publish" in line:
			log_ts = int(datetime.strptime(line[0:23], '%Y-%m-%d %H:%M:%S,%f').timestamp() * 1000)
			lst = [l.split("=")[1] for l in line.split("[")[1][:-2].split(",")]
			pkt = Packet(topic_id=int(lst[0]), pkt_ts=int(lst[1]), src_ip=curr_ip, log_ts=log_ts)
			if pkt not in pubp[curr_ip]:
				pubp[curr_ip].add(pkt)
				pubcnt[int(lst[0])] += 1
		elif "sending subscribe" in line:
			log_ts = int(datetime.strptime(line[0:23], '%Y-%m-%d %H:%M:%S,%f').timestamp() * 1000)
			lst = [l.split("=")[1] for l in line.split("[")[1][:-2].split(",")]
			subp[curr_ip].add(Packet(topic_id=int(lst[0]), pkt_ts=int(lst[1]), src_ip=curr_ip, log_ts=log_ts))
		elif "received notify" in line:
			log_ts = int(datetime.strptime(line[0:23], '%Y-%m-%d %H:%M:%S,%f').timestamp() * 1000)
			lst = [l.split("=")[1] for l in line.split("[")[1][:-2].split(",")]
			notp[curr_ip].add(Packet(topic_id=int(lst[0]), pkt_ts=int(lst[1]), src_ip=lst[2], log_ts=log_ts))
		elif "received response" in line:
			log_ts = int(datetime.strptime(line[0:23], '%Y-%m-%d %H:%M:%S,%f').timestamp() * 1000)
			lst = [l.split("=")[1] for l in line.split("[")[1][:-2].split(",")]
			resp[curr_ip].add(Packet(topic_id=int(lst[0]), pkt_ts=int(lst[1]), src_ip=lst[2], log_ts=log_ts, content=lst[3]))

	f.close()

f = open("verification.txt", "w")
f.write("")
f.close()

f = open("verification.txt", "a")

for i in range(len(pubcnt)):
	if pubcnt[i] != 0:
		f.write("Topic %d: %d pubs\n" % (i, pubcnt[i]))

for src1, pkts1 in subp.items():
	f.write("\n%s\n" % src1)
	for pkt0 in pubp[src1]:
		f.write("\tpub: %s\n" % pkt0)
	for pkt1 in pkts1:
		f.write("\tsub: %s\n" % pkt1)
		for pkt2 in resp[src1]:
			if pkt1.topic_id == pkt2.topic_id:
				f.write("\tres: %s\n" % pkt2)

f.close()

data = {"avg_not_delay": find_diff(pubp, notp), "avg_tat": find_diff(pubp, resp)}

with open('time.json', 'w', encoding='utf-8') as f:
	json.dump(data, f, ensure_ascii=False, indent=4)