def caesarCipherEncryptor(string, key):
    # Write your code here.
	temp = ""
	for letter in string:
		val = ord(letter)+(key%26)
		if val > 122:
			val = val - 26
		temp += chr(val)
	return temp