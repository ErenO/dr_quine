first = open('Grace_kid.py', 'w')
second = 0 #Ceci est un commentaire
third = r"print>>first, 'first = 0\nsecond = 0 #Ceci est un commentaire\nthird = r\"' + third + '\"' + '\nexec(third)'"
exec(third)
