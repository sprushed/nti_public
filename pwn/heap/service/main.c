#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void* chunk_ptrs[10] = {0};
int special = 0;

void add_note() {
	int number = -1;
	for (int i = 0; i < 10; i++) {
		if (!chunk_ptrs[i]) {
			number = i;
			break;
		}
	}
	printf("Your chunk number is [%d]\n", number);
	if (number == -1) {
		printf("The list is full. Delete something\n");
		return;
	}

	unsigned int size;
	printf("Input the size you want>> ");
	scanf("%d", &size);

	chunk_ptrs[number] = malloc(size);
	printf("What is your note about? >> ");
	read(0, chunk_ptrs[number], size);
}

void add_special_note() {
	if (special) {
		puts("You already created your special note");
		return;
	}
	special = 1;
	int number = -1;
	for (int i = 0; i < 10; i++) {
		if (!chunk_ptrs[i]) {
			number = i;
		}
	}

	if (number == -1) {
		printf("The list is full. Delete something\n");
		return;
	}

	chunk_ptrs[number] = malloc(0x40);
	printf("What is your very special note about? >> ");
	read(0, chunk_ptrs[number], 0x49);
}

void delete_note() {
	unsigned int number;

	printf("What note do you want to delete? >> ");
	scanf("%d", &number);
	if (number > 9) {
		puts("This note doesn't exist");
		return;
	}
	if (chunk_ptrs[number]) {
		free(chunk_ptrs[number]);
		chunk_ptrs[number] = 0;
		puts("Successfully deleted.");
	} else {
		puts("This note doesn't exist");
	}
}

void print_note() {
	unsigned int number;

	printf("Tell me what do you want to see? >> ");
	scanf("%d", &number);
	if (number > 9) {
		puts("This note doesn't exist");
		return;
	}
	if (chunk_ptrs[number]) {
		puts((char*)chunk_ptrs[number]);
	} else {
		puts("This note doesn't exist");
	}
}


void menu() {
	puts("[1] Add note");
	puts("[2] Add special note");
	puts("[3] Delete note");
	puts("[4] Print note");
	puts("[5] Exit");
	printf("Your choice>> ");
}

int main() {
	int choice;

	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);

	puts("Here we go again...");
	while (1) {
		menu();
		scanf("%d", &choice);
		switch (choice) {
			case 1:
				add_note();
				break;
			case 2:
				add_special_note();
				break;
			case 3:
				delete_note();
				break;
			case 4:
				print_note();
				break;
			case 5:
				return 0;
		}
	}
}
