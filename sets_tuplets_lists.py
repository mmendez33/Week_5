#collections = single variable used to store multiple variables
#list = [] ordered and changeable. Duplicates OK
# set = {} unordered and immutable, but Add/Remove  OK. NO duplicates
# Table = {} ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple", "orange", "banana", "conconut"]

# print(fruits[::2])

# print(dir(fruits)) 

# print(help(fruits))

#print(len(fruits))

# print("pineapple"in fruits)

# for fruit in fruits
#print(fruit)

# fruits[1]= "pineapple"  #i can reassign values using this 

fruits.remove("apple") #removes value
fruits.insert("pineapple")#inserts a value
fruits.sort()# sorts it
fruits.reverse() #reverses it 
fruits.clear()