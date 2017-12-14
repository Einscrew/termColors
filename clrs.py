#! /usr/bin/python3

def palete():
	f= '\033[48;5;{}m{:3}\033[0m'
	print(*[f.format(x,x) for x in range(256)], sep='|')


if __name__ == '__main__':
	palete()

