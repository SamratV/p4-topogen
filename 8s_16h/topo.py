#!/usr/bin/env python3

import json

topo = {}
topo["hosts"] = {}
topo["switches"] = {}
topo["links"] = []

scount = 8
hcount = 16

links = [
	[1, [2, 5]],
	[4, [3, 5, 6]],
	[2, [4, 6, 7]],
	[3, [6, 7, 8]],
	[2, [6]],
	[0, []],
	[2, [8]],
	[2, []]
]

maxh = [1, 1, 1, 1, 1, 1, 1, 1]
maxl = [2, 5, 3, 4, 3, 1, 3, 3]

k = hex(hcount).split("x")[1].zfill(2)

for i in range(1, hcount + 1):
	j = hex(i).split("x")[1].zfill(2)
	l = i * 10

	topo["hosts"]["h%d" % i] = {
        "ip": "10.0.%d.%d/24" % (i, i),
        "mac": "08:00:00:00:%s:%s" % (j, k),
        "commands": [
            "route add default gw 10.0.%d.%d dev eth0" % (i, l),
            "arp -i eth0 -s 10.0.%d.%d 08:00:00:00:%s:00" % (i, l, j),
            "./host.py h%d 10.0.%d.%d &" % (i, i, i)
        ]
    }

for i in range(1, scount + 1):
	topo["switches"]["s%d" % i] = {}

n = 1

for idx, val in enumerate(links):
	swid0 = "s%d" % (idx + 1)
	hosts = val[0]
	conns = val[1]

	for m in range(hosts):
		topo["links"].append(["h%d" % n, "%s-p%d" % (swid0, maxh[idx])])
		n = n + 1
		maxh[idx] = maxh[idx] + 1

	for m in range(len(conns)):
		swid = "s%d" % conns[m]
		k = conns[m] - 1
		topo["links"].append(["%s-p%d" % (swid0, maxl[idx]), "%s-p%d" % (swid, maxl[k])])
		maxl[idx] = maxl[idx] + 1
		maxl[k] = maxl[k] + 1

if __name__ == '__main__':
	print(json.dumps(topo, indent=4))