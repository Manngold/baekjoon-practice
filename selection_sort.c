#include <stdio.h>
int array[1001];
int main(void) {
	int i, j, min, input, index, temp;
	scanf("%d", &input);
	for (i = 0; i < input; i++) {
		scanf("%d", &array[i]);
	}
	for (i = 0; i < input; i++) {
		min = 1001;
		for (j = i; j < input; j++) {
			if (min > array[j]) {
				min = array[j];
				index = j;
			}
		}
		temp = array[i];
		array[i] = min;
		array[index] = temp;
	}
	for (i = 0; i < input; i++) {
		printf("%d\n", array[i]);
	}
}