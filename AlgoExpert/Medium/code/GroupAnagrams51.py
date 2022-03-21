def groupAnagrams(words):
    # Write your code here.
	my_word = {}
	for word in words:
		tmp = 0
		salt=0
		for char in word:
			asc = ord(char)
			if asc > salt:
				salt = asc
			tmp += asc
		tmp += salt
		if tmp in my_word.keys():
			my_word[tmp].append(word)
		else:
			my_word[tmp] = [word]
	return (list(my_word.values()))