#include <iostream>
#include <cstdint>

int swallow_redpill() {
    unsigned char m[2 + 4];
    unsigned char rpill[] = "\x0f\x01\x0d\x00\x00\x00\x00\xc3";
    *reinterpret_cast<uintptr_t*>(&rpill[3]) = reinterpret_cast<uintptr_t>(m);
    reinterpret_cast<void(*)()>(rpill)();
    return (m[5] > 0xd0) ? 1 : 0;
}

int main() {
    int result = swallow_redpill();
    std::cout << "Result: " << result << std::endl;
    return 0;
}
