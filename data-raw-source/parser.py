#--------------------
# simple text parser
#--------------------


import sys

def parser (r, w) :

    while True :
    	s = r.readline()
    	i = 0
    	strg = "<tr>\n<td>"
    	# print(type(s))
    	# print(str(s))
    	for char in s :
    		if(char != " ") :
    			strg += char
    		else :
    			strg += "</td>\n<td>"
    	strg += "</td>\n</tr>"
    	print (strg)

    	if(s == ""):
    		return
    w.write(strg)


parser(sys.stdin, sys.stdout)
