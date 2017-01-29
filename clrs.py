def palete():
	i=0
	var = ''
	for i in range(256):
		var += '\033[48;5;'+str(i)+'m'+str(i)+' \033[0m'
	print(var)
palete()

