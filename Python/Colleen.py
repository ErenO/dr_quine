#Ceci est un commentaire
def main():
    #ceci est le second commentaire
    s = r"print '#Ceci est un commentaire\ndef main():\n\t#ceci est le second commentaire\n\ts = r\"' + s + '\"' + '\n\texec(s)\nmain()'"
    exec(s)
main()
