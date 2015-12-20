 def palin():
	word = str(input("Please enter a word to test: "))
	if word[::-1] == word:
		print ("This is a palindrome")
	else:
		print ("This is not a palindrome")


if __name__ == "__main__":
	palin()
