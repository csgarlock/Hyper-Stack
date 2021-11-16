import sys

def setup():
	if(len(sys.argv) < 2):
		raise "Invalid Argument"
		return []
	hyper_file = open(sys.argv[1], "r")
	line_split = hyper_file.read().split("\n")
	a_split = []
	for l in line_split:
		a_split.append(l.split(" "))
	return a_split

def main():
	args = setup()
	arg_p = 0;
	while(not arg_p == len(args))

if __name__ == '__main__':
	main()