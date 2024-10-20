#!/bin/bash

read -p "Input your age: " age

if [ "$age" -lt 18 ]; then
  echo "You are a minor"
fi

if [[ "$age" -ge 18 && "$age" -le 64 ]]; then
   echo "You are an adult"
fi

if [ "$age" -ge 65 ]; then
  echo "You are a senoir"
fi  