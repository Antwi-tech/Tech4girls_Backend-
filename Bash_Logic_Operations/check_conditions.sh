#!/bin/bash


if [[ $1 -gt 10 && $2 -gt 10 ]]; then
   echo "Both numbers are greater than 10" 

elif [[ $1 -gt 10 || $2 -gt 10 ]]; then
    echo "At least one number is greater than 10."
    
else 
    echo "Neither number is greater than 10"
fi       
     