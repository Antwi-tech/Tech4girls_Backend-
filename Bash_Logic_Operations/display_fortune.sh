#!/bin/bash

echo "Ready for a fortune to be displayed by a cow?"
read -p "y for yes, n for no. Enter: " y


My_fortune=$(fortune)

if [ "$y" == "y" ]; then
    echo $My_fortune
    echo "$My_fortune" | cowsay
fi

if [ "$y" == "n" ]; then
    echo "Then later"
fi
