#APPEND

scholars = [ 'Jenifer', 'Precious', 'Matilda', 'Emefa', 'Jedidah', 'Beatrice']
scholar_set2 = [ 'Afua', 'Dede', 'Talatu', 'Amina']
scholars.append('Rhoda')
print(scholars)


#REMOVE
scholars.remove('Matilda')
print(scholars)

#POP
scholars.pop(0)
print(scholars)

scholars.pop()
print(scholars)

#SORT
scholars.sort()
print(scholars)

#REVERSE

scholars.reverse()
print(scholars)

#EXTEND

scholars.extend(scholar_set2)
print(scholars)


#SET METODS

#To add an item
random_numbers = { 34,89,65,32,1,0,74,8765}
even_numbers = {2,4,6,8,10,12}
random_numbers.add(2)
print(random_numbers)

#To remove maximum number from set
maxi= max(random_numbers)
print(maxi)
random_numbers.remove(maxi)
print(random_numbers)



#To add join two sets represented by |
new_set= random_numbers.union(even_numbers)
print(new_set)

#Intersection represented by &  
common_numbers=even_numbers.intersection(random_numbers)
print(common_numbers)

#Difference represented by -
diff= random_numbers.difference(even_numbers)
print(diff)
