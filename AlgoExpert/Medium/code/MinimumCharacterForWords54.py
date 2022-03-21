class char_inv:
	def __init__(self, char, isDel):
		self.char = char
		self.isDel = isDel

def minimumCharactersForWords(words):
    # Write your code here.
	inv_list = []
    for word in words:
		for option in inv_list:
			option.isDel = False
		for char in word:
			found = False
			for option in inv_list:
				if char == option.char and not option.isDel:
					option.isDel = True
					found = True
					break
					
			if not found:
				obj = char_inv(char, True)
				inv_list.append(obj)
			
	return [val.char for val in inv_list]
			