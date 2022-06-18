#!/usr/bin/env python3

import sys

inputs = {}
folder = ""
option = int(sys.argv[1])

if option == 0:
	folder = "4s_8h/inputs/"
	inputs = {
		"h1": ["subscribe,java,0,_\n", "publish,cpp,30,C++ supports OOPs."],
		"h2": ["subscribe,cpp,0,_"],
		"h3": ["subscribe,java,0,_"],
		"h4": ["subscribe,cpp,0,_"],
		"h5": ["subscribe,java,0,_"],
		"h6": ["subscribe,cpp,0,_"],
		"h7": ["subscribe,java,0,_"],
		"h8": ["subscribe,cpp,0,_\n", "publish,java,30,Java is platform independent."]
	}
elif option == 1:
	folder = "8s_16h/inputs/"
	inputs = {
		"h1": ["subscribe,java,0,_\n", "publish,cpp,30,C++ supports OOPs."],
		"h2": ["subscribe,cpp,0,_"],
		"h3": ["subscribe,java,0,_"],
		"h4": ["subscribe,cpp,0,_"],
		"h5": ["subscribe,java,0,_"],
		"h6": ["subscribe,cpp,0,_"],
		"h7": ["subscribe,java,0,_"],
		"h8": ["subscribe,cpp,0,_\n", "publish,java,30,Java was created by James Gosling."],
		"h9": ["subscribe,java,0,_\n", "publish,cpp,30,C++ was created by Bjarne Stroustrup."],
		"h10": ["subscribe,cpp,0,_"],
		"h11": ["subscribe,java,0,_"],
		"h12": ["subscribe,cpp,0,_"],
		"h13": ["subscribe,java,0,_"],
		"h14": ["subscribe,cpp,0,_"],
		"h15": ["subscribe,java,0,_"],
		"h16": ["subscribe,cpp,0,_\n", "publish,java,30,Java is platform independent."]
	}

if __name__ == '__main__':
	for host, stdin in inputs.items():
		filename = folder + host + ".txt"
		f = open(filename, "a", encoding="utf-8")
		for line in stdin:
			f.write(line)
		f.close()