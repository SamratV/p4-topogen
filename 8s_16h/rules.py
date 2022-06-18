#!/usr/bin/env python3

import json

hcount = 16
k = hex(hcount).split("x")[1].zfill(2)

rule = {
    "s1": [
    	{
            "table": "PubSubIngress.ipv4_lpm",
            "default_action": True,
            "action_name": "PubSubIngress.drop",
            "action_params": { }
        }
    ],
    "s2": [
    	{
            "table": "PubSubIngress.ipv4_lpm",
            "default_action": True,
            "action_name": "PubSubIngress.drop",
            "action_params": { }
        }
    ],
    "s3": [
    	{
            "table": "PubSubIngress.ipv4_lpm",
            "default_action": True,
            "action_name": "PubSubIngress.drop",
            "action_params": { }
        }
    ],
    "s4": [
    	{
            "table": "PubSubIngress.ipv4_lpm",
            "default_action": True,
            "action_name": "PubSubIngress.drop",
            "action_params": { }
        }
    ],
    "s5": [
    	{
            "table": "PubSubIngress.ipv4_lpm",
            "default_action": True,
            "action_name": "PubSubIngress.drop",
            "action_params": { }
        }
    ],
    "s6": [
    	{
            "table": "PubSubIngress.ipv4_lpm",
            "default_action": True,
            "action_name": "PubSubIngress.drop",
            "action_params": { }
        }
    ],
    "s7": [
    	{
            "table": "PubSubIngress.ipv4_lpm",
            "default_action": True,
            "action_name": "PubSubIngress.drop",
            "action_params": { }
        }
    ],
    "s8": [
    	{
            "table": "PubSubIngress.ipv4_lpm",
            "default_action": True,
            "action_name": "PubSubIngress.drop",
            "action_params": { }
        }
    ]
}

swid = "s1"

for i in range(1, 17):
	port = 0
	j = hex(i).split("x")[1].zfill(2)

	if i == 1:
		port = 1
	elif i in [11, 12]:
		port = 3
	else:
		port = 2

	rule[swid].append(
		{
			"table": "PubSubIngress.ipv4_lpm",
			"match": {
			    "hdr.ipv4.dstAddr": ["10.0.%d.%d" % (i, i), 32]
			},
			"action_name": "PubSubIngress.ipv4_forward",
			"action_params": {
			    "dstAddr": "08:00:00:00:%s:%s" % (j, k),
			    "port": port
			}
		}
	)

swid = "s2"

for i in range(1, 17):
	port = 0
	j = hex(i).split("x")[1].zfill(2)

	if i in [1, 11, 12]:
		port = 5
	elif i in [2, 3, 4, 5]:
		port = i - 1
	else:
		port = 6

	rule[swid].append(
		{
			"table": "PubSubIngress.ipv4_lpm",
			"match": {
			    "hdr.ipv4.dstAddr": ["10.0.%d.%d" % (i, i), 32]
			},
			"action_name": "PubSubIngress.ipv4_forward",
			"action_params": {
			    "dstAddr": "08:00:00:00:%s:%s" % (j, k),
			    "port": port
			}
		}
	)

swid = "s3"

for i in range(1, 17):
	port = 0
	j = hex(i).split("x")[1].zfill(2)

	if i < 6 or i in [11, 12]:
		port = 3
	elif i in [6, 7]:
		port = i - 5
	else:
		port = 4

	rule[swid].append(
		{
			"table": "PubSubIngress.ipv4_lpm",
			"match": {
			    "hdr.ipv4.dstAddr": ["10.0.%d.%d" % (i, i), 32]
			},
			"action_name": "PubSubIngress.ipv4_forward",
			"action_params": {
			    "dstAddr": "08:00:00:00:%s:%s" % (j, k),
			    "port": port
			}
		}
	)

swid = "s4"

for i in range(1, 17):
	port = 0
	j = hex(i).split("x")[1].zfill(2)

	if i < 8 or i in [11, 12]:
		port = 4
	elif i in [8, 9, 10]:
		port = i - 7
	else:
		port = 6

	rule[swid].append(
		{
			"table": "PubSubIngress.ipv4_lpm",
			"match": {
			    "hdr.ipv4.dstAddr": ["10.0.%d.%d" % (i, i), 32]
			},
			"action_name": "PubSubIngress.ipv4_forward",
			"action_params": {
			    "dstAddr": "08:00:00:00:%s:%s" % (j, k),
			    "port": port
			}
		}
	)

swid = "s5"

for i in range(1, 17):
	port = 0
	j = hex(i).split("x")[1].zfill(2)

	if i in [11, 12]:
		port = i - 10
	elif i == 1:
		port = 3
	elif i > 1 and i < 6:
		port = 4
	else:
		port = 5

	rule[swid].append(
		{
			"table": "PubSubIngress.ipv4_lpm",
			"match": {
			    "hdr.ipv4.dstAddr": ["10.0.%d.%d" % (i, i), 32]
			},
			"action_name": "PubSubIngress.ipv4_forward",
			"action_params": {
			    "dstAddr": "08:00:00:00:%s:%s" % (j, k),
			    "port": port
			}
		}
	)

swid = "s6"

for i in range(1, 17):
	port = 0
	j = hex(i).split("x")[1].zfill(2)

	if i < 6:
		port = 1
	elif i < 8:
		port = 2
	elif i in [11, 12]:
		port = 4
	else:
		port = 3

	rule[swid].append(
		{
			"table": "PubSubIngress.ipv4_lpm",
			"match": {
			    "hdr.ipv4.dstAddr": ["10.0.%d.%d" % (i, i), 32]
			},
			"action_name": "PubSubIngress.ipv4_forward",
			"action_params": {
			    "dstAddr": "08:00:00:00:%s:%s" % (j, k),
			    "port": port
			}
		}
	)

swid = "s7"

for i in range(1, 17):
	port = 0
	j = hex(i).split("x")[1].zfill(2)

	if i < 8 or i in [11, 12]:
		port = 3
	elif i in [8, 9, 10]:
		port = 4
	elif i in [13, 14]:
		port = i - 12
	else:
		port = 5

	rule[swid].append(
		{
			"table": "PubSubIngress.ipv4_lpm",
			"match": {
			    "hdr.ipv4.dstAddr": ["10.0.%d.%d" % (i, i), 32]
			},
			"action_name": "PubSubIngress.ipv4_forward",
			"action_params": {
			    "dstAddr": "08:00:00:00:%s:%s" % (j, k),
			    "port": port
			}
		}
	)

swid = "s8"

for i in range(1, 17):
	port = 0
	j = hex(i).split("x")[1].zfill(2)

	if i in [15, 16]:
		port = i - 14
	else:
		port = 4

	rule[swid].append(
		{
			"table": "PubSubIngress.ipv4_lpm",
			"match": {
			    "hdr.ipv4.dstAddr": ["10.0.%d.%d" % (i, i), 32]
			},
			"action_name": "PubSubIngress.ipv4_forward",
			"action_params": {
			    "dstAddr": "08:00:00:00:%s:%s" % (j, k),
			    "port": port
			}
		}
	)

if __name__ == '__main__':
	print(json.dumps(rule, indent=4))