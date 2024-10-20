#!/bin/bash

# echo "Enter number to countdown from:"
 
read -p "Enter number to countdown from:" number

while [ $number -gt 0 ]
do 
  echo "$number"
  number=$((number-1))
done  
  echo "Countdown Complete!"
  
