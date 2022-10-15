

def getBullsAndCows(key, word):
	bulls = 0
	cows = 0
	for ind, c in enumerate(word):
		if c in key:
			indexes = [i for i, ch in enumerate(key) if ch == c]
			if ind in indexes:
				bulls += 1
			else:
				cows += 1
	return (bulls, cows)
