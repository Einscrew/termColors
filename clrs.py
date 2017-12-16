#! /usr/bin/python3

def palete(code):
	f= '\033[{};5;{}m{:3}\033[0m'
	print('', *[f.format(code,x,x) for x in range(16)], sep='|')
	print('', *[f.format(code,x,x)+'\n'if (x-15)%6==0 else f.format(code,x,x)+'' for x in range(16,232)], sep='|')
	print('', *[f.format(code,x,x) for x in range(232,256)], sep='|')


if __name__ == '__main__':
	palete(input('insert 38 for foreground colors or 48 for background colors: '))

