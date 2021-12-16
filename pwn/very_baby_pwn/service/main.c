#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

struct play {
	char buf[16];
	int canary;
};

int main() {
	struct play on_stack;
	on_stack.canary = 0;

	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);

	printf("Don't be afraid. Everything is gonna be alright:\n");
	read(0, on_stack.buf, 20);
	if (!on_stack.canary) {
		printf("Oh sheeesh... I think you should try again\n");
	} else {
		printf("Take it bruh!\n");
		system("/bin/sh");
	}
}
