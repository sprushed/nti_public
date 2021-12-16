#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

unsigned long int check1 = 0;
unsigned long int check2 = 0;
unsigned long int check3 = 0;
unsigned long int check4 = 0;

void check() {
	if ((check1 == 0xdeadbeef) && (check2 == 0xcafebabe) && (check3 == 0xabbaabba) && (check4 == 0x41414141)) {
		system("/bin/sh");
	}
}

int main() {
	char buf[128];

	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);

	printf("<<<1C Bitrix>>>\nPlease prove you are not an american boy:\n");

	for (int i = 0; i < 4; i++) {
		read(0, buf, 128);
		printf(buf);
	}
	check();
}
