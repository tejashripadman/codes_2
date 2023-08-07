def removeVowels(self, S):
	s = "aeiou"
	s1 = ""
	for i in S:
		  if i not in s:
		      s1 = s1 + i
	return s1
