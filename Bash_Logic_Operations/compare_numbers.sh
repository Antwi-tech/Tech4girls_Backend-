#!/bin/bash

read -p "Enter First number:" number1
read -p "Enter second number:" number2

if [[ $number1 -gt $number2 ]]; then
   echo "$number1 is greater than $number2"
fi  

if [[ $number1 -lt $number2 ]]; then
   echo "$number1 is less than $number2"
fi   

if [[ $number1 -eq $number2 ]]; then
   echo "$number1 and $number2 are equal"  
fi   

