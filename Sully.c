#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main(){
int i = 5;
if (i <= 0)
return(0);
char str[1000];
sprintf(str, "Sully_%d.c", i);
FILE *f = fopen(str, "w");
i--;
char*a="#include <stdio.h>%1$c#include <string.h>%1$c#include <stdlib.h>%1$cint main(){%1$cint i = %4$d;%1$cif (i <= 0)%1$creturn(0);%1$cchar str[5000];%1$csprintf(str, %2$cSully_%%d.c%2$c, i);%1$cFILE *f = fopen(str, %2$cw%2$c);%1$ci--;%1$cchar*a=%2$c%3$s%2$c;%1$cfprintf(f, a, 10, 34, a, i);%1$cfclose(f);%1$cchar command[5000];%1$csprintf(command, %2$cclang -Wall -Wextra -Werror -o %%.*s %%s%2$c, (int)strlen(str)-2, str, str);%1$csystem(command);%1$csprintf(command, %2$c./%%.*s%2$c, (int)strlen(str)-2, str);%1$csystem(command);%1$c}%1$c";
fprintf(f, a, 10, 34, a, i);
fclose(f);
char command[1000];
sprintf(command, "clang -Wall -Wextra -Werror -o %.*s %s", (int)strlen(str)-2, str, str);
system(command);
sprintf(command, "./%.*s", (int)strlen(str)-2, str);
system(command);
}
