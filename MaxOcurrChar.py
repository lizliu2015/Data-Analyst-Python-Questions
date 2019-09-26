func maxOccurChar(str):
	counter = dict()
  
  # count up each char
  for char in string:
  	if counter.get(char):
    	counter[char] = counter[char] + 1
    else:
    	counter[char] = 1
  
  # loop through dict to find the key with highest value
  max = None
  for char in counter:
  	if counter[char] > max:
    	max = char
  
  return max
