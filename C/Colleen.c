#include<stdio.h>
/*
** ceci est un commentaire
*/
int main(){/*en voici un autre*/char *s="#include<stdio.h>%1$c/*%1$c** ceci est un commentaire%1$c*/%1$cint main(){/*en voici un autre*/char *s=%2$c%3$s%2$c;printf(s,10,34,s);}";printf(s,10,34,s,34);}
