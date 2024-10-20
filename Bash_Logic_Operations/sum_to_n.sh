#!/bin/bash


read -p "Enter a number: " n


sum=0 #final sum
i=1 #represents the starting point of calculation


while [ $i -le $n ]
do
    sum=$((sum + i))
    i=$((i + 1))
done

echo "The sum of numbers from 1 to $n is: $sum"
