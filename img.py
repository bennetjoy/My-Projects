try:
	f = open("D:\\bennet.txt")
	print(f.read)
finally:
	f.close()