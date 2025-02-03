# list datastructure
# list are mutable
# list are ordered
# list are indexed
from readline import append_history_file

fruits=['apple','banana','orange','strawberry','peach','pineapple']
fruits[0]="watermelon"
numbers=[1,2,3,4,5,6,7,8,9]
numbers2=[67,5,2,-7,0,13,5,1,8,22,-9,14]
print(numbers2)
numbers2.sort(reverse=True)
print(numbers2)
print(fruits)
print(f"I love eating {fruits[3]}")
print(numbers)
numbers.append(11)
print(numbers)

# tuple datastructure
# tuples are immutable(unchangeable)
# tuples are odered
# tuples are indexed
cars=('audi','toyota','subaru','toyota','mercedes')
# cars[1]='bmw'
print(cars)
nambari=(43,23,4,11,70,-10,-45,78,9,-64)
print(sorted(nambari))

# set datastructure
# set are unordered
# set are not indexed
computers={'hp','dell','lenovo','macbook','asus','acer'}
computers.add('toshiba')
computers.remove('lenovo')
print(computers)
num1={1,2,3,}
num2={4,5,6,}
union_set = num1.union(num2)
print(union_set)

# dictionaries data structure
student={'Name':'John','Age':5,'Gender':'Male','School':'University of Nairobi'}
print(student['Name'])
print(f"Student name: {student['Name']}")
print(f"Student age: {student['Age']}",f"Student gender: {student['Gender']}",f"Student school: {student['School']}")