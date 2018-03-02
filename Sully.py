import os
import sys

def main():
    i = 12
    if (i <= 0):
        return (0)
    str = "Sully_%d.py" % i
    f1 = open(str, "w")
    i -= 1
    stri = str(i)
    s = r"print>>f1, 'import os\n\ndef main():\n\ti = ' + stri + '\n\tif (i <= 0):\n\t\treturn (0)\n\ts = r\"' + s + '\"'+'\n\texec(s)\nmain()'"
    command = "python %s" % (str)
    os.system(command)
    exec(s)
main()
