#commentaire
a='#commentaire%ca=%s;print a%%`a`';print a%`a`

''' ceci est un commentaire'''
s="'''ceci est un commentaire'''%cs=, print(s%s,10)"; print (s%s, 10)

f1=open('./testfile', 'w')
print >> f1, "hello world"
