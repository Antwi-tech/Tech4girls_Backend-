#!/bin/bash


if [ $(($1%2)) -eq 0 ]; then
    echo " The number $1 is even"
 else 
   echo "The number $1 is odd"
 fi
  

#OR

echo "Enter a number to check is it is even or odd:"


read num

if [ $(($num % 2)) -eq 0 ]; then
  echo "The number $num is even"
else 
  echo "The number $num is odd"
fi   
 
        

#NB: when executing the file, you have to enter a positional number then when executed the 
#user will have to enter another number