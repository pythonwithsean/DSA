def main():
	n = 10
	binaryString = ""
	while n > 0:
		binaryChar,n = n % 2, n // 2
		binaryString = str(binaryChar) + binaryString
	print(binaryString)





if __name__ == "__main__":
	main()