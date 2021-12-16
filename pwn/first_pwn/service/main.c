#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
	char buf[16];

	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);

	printf("ROP at me now, how far I've come I hope that you're proud\n");
	read(0, buf, 128);
}
