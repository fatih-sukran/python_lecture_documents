
Animals1=['Dog','Turtle','Rabbit','Parrot','Cat']
Animals2=['Mouse','Fish','Hamster','Lion']
List3=[80, 30, 15, 32, 93]

print('1) display the number of elements in Animals1 list.')
print(len(Animals1))

print('2) display the second element in Animals2 list.R')
print(Animals2[1])

print('3) return the items from the beginning to, but NOT including, "Parrot" in Animals1.')
print([item for item in Animals1 if (item != 'Parrot')])

print('4) return the items from the fourth element from the end of the list until' 
                          'the second element from the end of the list Animals1.')
print(Animals1[3:len(Animals1) - 2]) #hatalı bak

print('5) replace the third element of Animals2 with "Snake" and "Fox"')
Animals2 = Animals2[:2] + ['Snake', 'Fox'] + Animals2[2:]
print(Animals2)

print('6) insert "Eagle" as third element into Animals2 list')
Animals2.insert(2, 'Eagle')
print(Animals2)

print('7) merge the two lists using extend() method')
Animals1.extend(Animals2)
print(Animals1)

print('8) delete "Rabbit" from Animals1')
Animals1.remove('Rabbit')
print(Animals1)

print('9) remove the last element from Animals2')
Animals2.pop()
print(Animals2)

print('10) print Animals1 list using for loop')
for animal in Animals1:
    print(animal, end=', ')
print()

print('11) print Animals2 list using while loop')
i = 0
while(i < len(Animals2)):
    print(Animals2[i], end=', ')
    i = i + 1
print()

print('12) create a new list called Animals3 using list comprehension and '
            'including elements from Animals1 list encluding letter \'e\'')
Animals3 = [animal for animal in Animals1 if 'e' in animal]
print(Animals3)

print('13) create a new list called Animals4 using list comprehension and returning' 
      'all elemenets from Animals2 but returning "Elephant" instead of "Hamster". ')
Animals4 = [animal if animal != 'Hamster' else 'Elephant' for animal in Animals2]
print(Animals4)

print('14) sort List3 based on how close the number is to 30')
List3.sort(key= lambda x: abs(x - 30))
print(List3)

print('15) reverse list Animals2 regardless of the alphabet.')
Animals2.reverse()
print(Animals2)

print('16) merge lists Animals2 and List3 using append() method')
for item in List3:
    Animals2.append(item)
print(Animals2)

print('17) merge lists Animals1 and List3 using extend() method')
Animals1.extend(List3)
print(Animals1)

print('18) merge lists Animals1 and Animals2 using \'+\' operator.')
Animals1 = Animals1 + Animals2
print(Animals1)

print('19) delete the third element from List3')
del List3[2]
print(List3)

print('20) delete the whole list Animals1.')
del Animals1