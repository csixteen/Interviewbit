#include <stdio.h>

unsigned int reverse(unsigned int A) {
    int count;
    unsigned int res = 0;
    for(count = 0; count < 32; count++) {
        res |= ((A & 1) << (31 - count));
        A >>= 1;
    }
    return res;

int main(int argc, char **argv) {
    return 0;
}
