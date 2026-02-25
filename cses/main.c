#include <stdio.h>

int main(){

    char * str1 = "Hello";
    char * str2 = "World";
    char ** strPtrs = &str1;
    strPtrs++;
    strPtrs = &str2;
    strPtrs--;
    for(int i = 0; i < 2; i++){
        printf("%s\n", *strPtrs);
        strPtrs++;
    }
    strPtrs--;
    strPtrs--;
    printf("%c\n", **strPtrs);
    return 0;
}
