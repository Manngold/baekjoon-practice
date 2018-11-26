#include <stdio.h>

int main(void) {
	int vowelIndex = 0;
	int consonantIndex = 0;
	int vowel = 0;
	int consonant = 0;
	int changeChecker = 0;
	char vowelTester[5] = { 'a', 'e', 'i', 'o', 'u' };
	char vowels[20] = { 0 };
	char consonants[20] = { 0 };
	char input[40] = { 0 };
	char quit;
TRYAGAIN:
	printf("Enter a string: ");
	scanf("%[^\n]s", input);

	for (int i = 0; i < 40; i++) {
		for (int j = 0; j < 5; j++) {
			if (input[i] == vowelTester[j]) {
				vowels[vowelIndex] = vowelTester[j];
				vowelIndex++;
				vowel++;
			}
		}
		if (changeChecker == vowel) {
			consonants[consonantIndex] = input[i];
			consonantIndex++;
		}
		else changeChecker++;

	}
	for (int i = 0; i < 40; i++) {
		if (consonants[i] == 0) {
			break;
		}
		else consonant++;
	}

	printf("The total number of vowels: %d\n", vowel);
	printf("The total number of consonants: %d\n", consonant);
	printf("Vowels: %s \n", vowels);
	printf("Consonants: %s \n", consonants);
	printf("Try Again? Y/y continues, other quits. ");
	scanf(" %c", &quit);
	if (quit = 'y' || 'Y') {
		goto TRYAGAIN;
	}
	else printf("Bye");
}