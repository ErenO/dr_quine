import os

def main():
    i = 12
    if (i <= 0):
        return (0)
    str = "Sully_%d.py" % i
    f1 = open(str, "w")
    i -= 1
    s = r"print>>f1, 'import os\n\ndef main():\n\ti = 11\n\tif (i <= 0):\n\t\treturn (0)\n\tstr = \"Sully_%d.py\" % i\n\tf1 = open(str, \"w\")\n\ti -= 1\n\ts = r\"' + s + '\"\n\tf1.close()\n\tcommand = \"python %s\" % (str)\n\tos.system(command)\n\texec(s)\nmain()'"
    command = "python %s" % (str)
    os.system(command)
    exec(third)
main()
