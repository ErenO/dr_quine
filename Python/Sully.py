import os

def main():
    i = 12
    if (i <= 0):
        return (0)
    str = ""
    str = "Sully_%d.py" % i
    f1 = open(str, "w")
    i -= 1
    s = r"print>>f1, 'import os\n\ndef main():\n\ti = 12\n\tif (i <= 0):\n\t\treturn (0)\n\tstr = \"\"\n\tstr = \"Sully_%d.c\" % i\n\tf1 = open(str, \"w\")\n\ti -= 1\n\ts = r\"' + s + '\"' + '\n\tf1.close()\n\tcommand = ""\n\tcommand = \"gcc -Wall -Wextra -Werror -o %*s %s\" % (str[:-2], str)\n\tos.system(command)\n\tcommand = \"./%s\" % \str[:-2]\n\texec(s)\nmain()'"
    f1.close()
    command = ""
    command = "gcc -Wall -Wextra -Werror -o %s %s" % (str[:-2], str)
    os.system(command)
    command = "./%s" % str[:-2]
    exec(s)
main()
