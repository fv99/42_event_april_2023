#include <stdio.h>
#include <string.h>

int card_value(char card) {
    switch (card) {
        case '2': case '3': case '4': case '5': case '6': case '7': case '8': case '9':
            return card - '0';
        case 'T': case 'J': case 'Q': case 'K':
            return 10;
        case 'A':
            return 11;
        default:
            return 0;
    }
}

int blackjack_value(const char *hand) {
    int value = 0, aces = 0;
    for (size_t i = 0; i < strlen(hand); ++i) {
        int card_val = card_value(hand[i]);
        if (hand[i] == 'A') {
            aces++;
        }
        value += card_val;
    }

    while (value > 21 && aces > 0) {
        value -= 10;
        aces--;
    }

    return value;
}

int main() {
    char hand[15];
    printf("Enter the cards in the blackjack hand (e.g., A8 or D34):\n");
    scanf("%s", hand);

    int value = blackjack_value(hand);
    printf("The value of the hand is: %d\n", value);

    return 0;
}
