#!/usr/bin/python3

#The UPPER function is used to convert alphabets into their respective capital case
#Here is how to use it:



name='antwiwaa'
print(name.upper())

#The LOWER function is used to convert alphabets into their respective lower case
#Here is how to use it:

animal='CAT'
print(animal.lower())

#REPLACE searches through a sentence and changed it to the word that you have specified
#Or simply put, it is used for modification
#Here is how to use it:

sentence='My name is Antwiwaa'

print(sentence)
#So Antwiwaa, which is in the sentence will be excahanged with Afua
print(sentence.replace( 'Antwiwaa' , 'Afua'))

#Join can be used to put lists together with your desired symbol or word

string1=[ "My", "backend" ,"class" ,"takes","place","at" ,"Dzorwulu" ]
sentencejoined= " ".join(string1)
print(sentencejoined)

#This allows you to print the list with each item separated by comma
animals=['cat','dog','squirrel','penguin','mow']
joint= ",".join(animals)
print(joint)

#This assigns jollof to each letter and space of the sentence but not the last alphabet
lunch="I ate"
joint2= "jollof ".join(lunch)
print(joint2)

