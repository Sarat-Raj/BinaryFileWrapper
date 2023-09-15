#include <iostream>
#include <unistd.h>
#include <sys/wait.h>
#include <string.h>
#include <stdexcept>


std::string string_to_hex(const std::string& input){
  static const char hex_digits[]="0123456789ABCDEF";
  std::string output;
  output.reserve(input.length()*2);
  for(unsigned char c: input){
    output.push_back(hex_digits[c >> 4]);
    output.push_back(hex_digits[c &15]);
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
 int value = hex_values[hex_digits];
 if(value == -1) throw std::invalid_argument("invalid hex digit");
 return value;
}

std::string hex_to_string(const std::string& input){
  const auto len = input.length();
  if(len&1)throw std::invalid_argument("odd length");
  std::string output;
  output.reserve(len/2);
  for(auto it=input.begin(); it != input.end();){
   int hi = hex_value(*it++);
   int lo = hex_value(*it++);
   output.push_back(hi << 4 | lo);
  };
}

int main(int argc, char** argv) {
 std::string Hex_Key, Hex_Text;
  try{
    Hex_Key = argv[1];
    std::cout<<argv[1];
    std::cout<<argv[2];
    Hex_Text = argv[2];
    throw 505; }
 catch(...){ std::cout << "Needs 2 args with execution to run.";}
 // when code is compiled as g++ -o mother CPPWrap.cpp and 
 // is supposed to receive executing command as ./mother arg1 arg2 ....
 Hex_Text = string_to_hex(Hex_Text);
 pid_t child_pid=fork();
 if (child_pid==0){
  execl("/home/cen598/Downloads/CSE598_Project1_Handout/project1_handout/mothership","./mothership","--key", Hex_Key, "--plaintext", Hex_Text, nullptr); // parameters needed to be are complete details of the file - path to file including file name, name of the command,arguments untill they exhaust and ends with a null pointer. 
  perror("execl");
  exit(1);
 }
 else if(child_pid>0){
 int status;
 waitpid(child_pid, &status, 0);
 if(WIFEXITED(status)){
  int exit_status = WEXITSTATUS(status);
  std::cout << "Child process exited with status: " << exit_status << std::endl;
 } 
 else {
 perror("fork");
 return 1;
 }
 }
 return 0;
}
