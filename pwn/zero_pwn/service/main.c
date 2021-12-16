#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int win() {
	system("/bin/sh");
}

int main() {
	char buf[16];

	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);

	printf("Hello dude! Here's something you need: %p\n", main);
	printf("What do you answer to this?\n");
	read(0, buf, 128);
	puts("Got it. See you next time!");
}
