#!/usr/bin/env python3

import json

clone = {}

ports = [
	[1, 3],
	[4, 8],
	[2, 6],
	[3, 7],
	[2, 5],
	[0, 4],
	[2, 5],
	[2, 4]
]

for idx, val in enumerate(ports):
	swid = "s%d" % (idx + 1)
	clone[swid] = {
		"max_hosts": val[0],
		"max_ports": val[1]
	}

if __name__ == '__main__':
	print(json.dumps(clone, indent=4))