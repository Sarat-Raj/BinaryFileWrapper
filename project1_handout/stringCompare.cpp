#include <iostream>
#include <string.h>

int main(int argc, char** argv){
 std::string str1 = argv[1];
 std::string str2 = argv[2];
 if(!str1.compare(str2))  std::cout << "both are same";
 else std::cout << "both strings arent same";
}
   
