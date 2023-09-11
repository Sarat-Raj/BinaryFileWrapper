#include <iostream>
#include <unistd.h>
#include <sys/wait.h>
#include <string.h>

int main(int argc, char** argv) {
 try{
  std::string Hex_Key = argv[1];
  std::string Hex_Text = argv[2];
  throw 505;
 }
 catch(...){ std::cout << "Needs 2 args with execution to run.";}
 // when code is compiled as g++ -o mother CPPWrap.cpp and 
 // is supposed to receive executing command as ./mother arg1 arg2 ....
 
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
  iny exit_status = WEXITSTATUS(status);
  std::cout << "Child process exited with status: " << exit_status << std::endl;
 } 
 else {
 perror("fork");
 return 1;
 }
 return 0;
 }
