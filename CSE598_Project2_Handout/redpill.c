#include <stdio.h>
#include <stdint.h> // Include for uintptr_t

int swallow_redpill() {
    unsigned char m[2 + 4];
    unsigned char rpill[] = "\x0f\x01\x0d\x00\x00\x00\x00\xc3";
    *((uintptr_t*)&rpill[3]) = (uintptr_t)m;
    ((void(*)())&rpill)();
    return (m[5] > 0xd0) ? 1 : 0;
}

int main() {
    int result = swallow_redpill();
    printf("Result: %d\n", result);
    return 0;
}

  