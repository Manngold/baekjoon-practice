#include <stdio.h>

int main(void) {
	int sugar;
	int move = 0;
	scanf("%d", &sugar);
	sugarCarry(sugar, move);
	return 0;
}

int sugarCarry(int sugar, int move) {
	sugar == 0 ? printf("%d", move) : (sugar % 5) == 0 ? sugarCarry(0, move+(sugar/5)) : (sugar % 3) == 0 || (sugar % 3) == 1 || (sugar % 3) == 2 ? sugarCarry(sugar - 3, ++move) : printf("-1");
};

