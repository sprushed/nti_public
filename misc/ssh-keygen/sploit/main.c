#include "sploitlib.c"
#include <stdio.h>
#include <stdlib.h>

int main() {
	setresuid(0, 0, 0);
	printf("%d\n", getuid());
	FILE *fp;

	fp = fopen("/etc/passwd", "r");
	char* buf = malloc(1024);
	fgets(buf, 1023, fp);
	printf("%s\n", buf);
	C_GetFunctionList();
}
