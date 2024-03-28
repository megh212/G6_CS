//made by uday rawat g6-cs
#include <stdio.h>
#include <string.h>
//encrypt
void encrypt(char *txt) {
	int len = strlen(txt);

	for (int i = 0; i < len; i++) {
		txt[i] = ((txt[i] + 5) * 2 + 1) % 128;
	}
}
//decrypt
void decrypt(char *txt) {
	int len = strlen(txt);

	for (int i = 0; i < len; i++) {
		txt[i] = ((txt[i] - 1 + 128) / 2 - 5) % 128;
	}
}

int main() {
	int choice;
	char txt[50];

	printf("Press 1 to encrypt text\nPress 2 to decrypt text\n");
	scanf("%d", &choice);

	printf("Enter the text:\n");
	getchar();
	fgets(txt, sizeof(txt), stdin);
	txt[strcspn(txt, "\n")] = '\0';
	if (choice == 1) {
		encrypt(txt);
		printf("Encrypted text: %s\n", txt);
		getch();
		return 0;
	} else if (choice == 2) {
		decrypt(txt);
		printf("Decrypted text: %s\n", txt);
        getch();
		return 0;
	} else {
		printf("Invalid choice\n");
        getch();
		return 0;
	}
	getch();
	return 0;
}

