#!/bin/bash

num=$1

if [ $((num % 2)) -eq 0 ]; then
  echo "The number $num is even"
else 
  echo "The number $num is odd"
fi     

#OR

 
 if [ $(($1%2)) -eq 0 ]; then
    echo " The number $1 is even"
 else 
   echo "The number $1 is odd"
 fi       

#NB: The answer will be printed twice 