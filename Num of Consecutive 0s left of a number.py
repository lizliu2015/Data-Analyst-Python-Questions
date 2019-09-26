def countzero(x):
	zeroes = 0
	res = str(abs(x))
	for i in reversed(res):
  	if i == '0':
    	zeroes = zeroes + 1
    else:
    	break
  return zeroes
