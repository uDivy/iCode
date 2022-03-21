def reverseWordsInString(string):
    # Write your code here.
	space = ''
	word = ''
	wrd_cnt = 0
    for i,char in enumerate(string):
		if char == " ":
			space = space + ' '
		else:
			l = len(space)
			if l > 0:
				word = word[0:wrd_cnt][::-1] + word[wrd_cnt:len(word)]
				wrd_cnt = 0
				print(word)
			word = char + str(space) + word
			wrd_cnt += 1
			space = ''
	word = str(space) + word[0:wrd_cnt][::-1] +  word[wrd_cnt:len(word)]
	return word