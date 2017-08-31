#include<stdio.h>
#define FIRST
#define SECOND
#define THIRD(x) int main(){FILE*file = fopen("Grace_kid.c", "w");char*s="#include<stdio.h>%1$c#define FIRST%1$c#define SECOND%1$c#define THIRD(x) int main(){FILE*file = fopen(%3$cGrace_kid.c%3$c, %3$cw%3$c);char*s=%3$c%2$s%3$c;fprintf(file,s,10,s,34);}%1$cTHIRD()%1$c";fprintf(file,s,10,s,34);}
THIRD()
