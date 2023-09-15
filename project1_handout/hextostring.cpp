#include <iostream>
#include <string.h>
#include <stdexcept>


std::string string_to_hex(const std::string& input){
  static const char hex_digits[]="0123456789ABCDEF";
  std::string output;
  output.reserve(input.length()*2);
  for(unsigned char c: input){
    output.pushback(hex_digits[c >> 4]);
    output.pushback(hex_digits[c &15]);
  }
  return output;
}
int hex_value(unsigned char hex_digits){
 static const signed char hex_values[256] = {
  -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
  -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
  -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
  0,  1,  2,  3,  4,  5,  6,  7,  8,  9, -1, -1, -1, -1, -1, -1,
  -1, 10, 11, 12, 13, 14, 15, -1, -1, -1, -1, -1, -1, -1, -1, -1,
  -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
  -1, 10, 11, 12, 13, 14, 15, -1, -1, -1, -1, -1, -1, -1, -1, -1,
  -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
  -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
  -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
  -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
  -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
  -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
  -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
  -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
  -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1};
 int value = hex_values[hex_digit];
 if(value == -1) throw std::invalid_argument("invalid hex digit");
 return value;
}

std::string hex_to_string(constant std::string& input){
  const auto len = input.lenght();
  if(len&1)throw std::invalid_argument("odd length");
  std::string output;
  output.reserve(len/2);
  for(auto it=input.begin(); it != input.end();){
   int hi = hex_val(*it++);
   int lo = hex_val(*it++);
   output.push_back(hi << 4 | lo);
  };
}

int main(int argc, char** argv) {
 try{
  std::string String_output = hex_to_string(argv[1]);
  throw 505;
 }
 catch(...){ std::cout << "Needs argument with execution to run.";}
 // when code is compiled as g++ -o mother CPPWrap.cpp and 
 // is supposed to receive executing command as ./mother arg1 arg2 ....
 cout << "string output is:" << String_output;
 return 0;
 }
