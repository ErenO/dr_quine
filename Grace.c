#include<stdio.h>

#define FIRST
#define SECOND
#define THIRD(x) int main(){FILE*file = fopen("Grace_kid.c", "w");char*a="#include<stdio.h>%c#define FIRST%c#define SECOND%c#define THIRD(x) int main(){FILE*file = fopen(%cGrace_kid.c%c, %cw%c);char*a=%c%s%c;fprintf(file, a,10,34,a,34);}%cTHIRD(1)%c";fprintf(file, a,10,34,a,34);}
THIRD(1)
