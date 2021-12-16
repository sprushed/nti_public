#include <stdio.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

char string[128] = {0};

int main() {
	setup();
	int fd = open("/dev/urandom", 0);
	read(fd, string, 34);
	void (*fun_ptr)(char*) = mmap(0, 0x1000, PROT_EXEC|PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0);	
	mmap(0, 0x1000, PROT_EXEC|PROT_READ, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0);
	puts("Hello fellow hacker!");
	puts("Input your shellcode and be happy");
	read(0, fun_ptr, 8);
	fun_ptr(string);
	if (!strcmp(string, "password_for_this_one_is_very_hard")) {
		puts("Wow! How you even did that??");
	} else {
		puts("You did something wrong!");
	}

}

void setup() {
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);	
}
