#include <stdio.h>
#include <stdlib.h>

extern void m3d_(char*);

int main(int argc, char **argv) {

    printf("Hello from C!\n");
    m3d_("Hello from Fortran!");
    
    return 0;
}


