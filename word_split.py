
def word_split(phrase, list, output=None):
	if output is None:
		output = []
	
	for word in list:
		if phrase[0:len(word)] == word:
			output.append(word)
			word_split(phrase[len(word):], list, output)
			break
	return output


print(word_split('Heythere',['Hi', 'there']))