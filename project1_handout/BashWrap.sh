#!/bin/bash

echo "Bash script to run a mothership."


for i in {1...10}  
do
  ./mothership >> mothership_output.txt
  sleep 1 #sleeps for a sec.
done

### this following code is supposed to convert ascii to hex and then send it to ./mothership --key <Key_hex> --plaintext <Plain_text_in_hex>

for i in {1...10}  
do
  ./mothership >> mothership_output.txt
  sleep 1 #sleeps for a sec.
done
