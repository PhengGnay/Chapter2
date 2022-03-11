# num1 = 1
# num2 = 10
# num3 = 1000
# sum_of_all_numbers = num1 + num2 + num3
# print("Sum is {0:n}".format (sum_of_all_numbers))

# list_of_numbers = [1, 10, 1000]
# print(sum(list_of_numbers)) #sum
# print(min(list_of_numbers)) #min
# print(max(list_of_numbers)) #max
# print(len(list_of_numbers)) #len
# print(list_of_numbers.count(4)) #count
# print(list_of_numbers.index(1)) #index
# print(list_of_numbers.reverse()) #reverse
# list_of_numbers.clear() #[] (have to cancel this unless every thing under will be clear)
# print(list_of_numbers)
# list_of_numbers.append(100) 
# list_of_numbers.append(100) 
# list_of_numbers.append(100) 
# list_of_numbers.append(100) 
# list_of_numbers2 = [3, 100, 5]

# # Adding/concatenating arrays .extend
# list_of_numbers3 = list_of_numbers.extend(list_of_numbers2)
# print(list_of_numbers)

# # Adding/concatenating arrays using +
# L1 = [1, 32, 4]
# L2 = [100, 200, 300]
# L3 = L1 + L2
# print(L3)

# words = ["Spam", "Wink", "Hi"]
# words.insert(3, "Hello")
# print("Words====>", words)

grades = []  #Create the variable grades and assign it to the empty list
# num = float(input("Enter the first grade:"))
# grades.append(num)
# num = float(input("Enter the second grade:"))
# grades.append(num)
# num = float(input("Enter the third grade:"))
# grades.append(num)
# num = float(input("Enter the fourth grade:"))
# grades.append(num)
# num = float(input("Enter the fifth grade:"))
# grades.append(num)
# minimumGrade = min(grades)
# grades.remove(minimumGrade)
# minimumGrade = min(grades)
# grades.remove(minimumGrade)
# average = sum(grades) / len(grades)
# print("Average Grade: {0: .2f}".format (average))

# grades.append(1)
# grades.append(2)
# grades.append(4)
# grades.append(9)
# print("grades", grades)

# length = len(grades) #4
# print("length", length) 
# print("sliced:", grades[:]) # (1, 2, 4, 9)

# str1 = "a,b,c"
# parts = "a,b,c".split(",")
# print("parts: ",  parts)

# lines = ["To", "be", "or", "not", "to", "be"]
# print("lines before join: ", lines)
# joined = " ".join(lines) # is the seperator between each word
# print("joined: ", joined)# To be or not to be

# infile = open("Data.txt", "r")

# names = [] #using the for loop to populate the names array with names
# for line in infile: 
#     print("line: ", line.rstrip())
#     # print("line after stripping the right side: ", line.rstrip())
#     names.append(line.rstrip())
# print("names: ", names)

# names_using_list_comprehension = [line.rstrip() for line in infile] #this is equivalent to lines (74-80)
# infile.close() # Close the Data.txt file to preserve memory

# infile = open("Grades.txt", "r")
# for line in infile:
#     print("line: ", eval(line)) #turns the strings into numbers
# infile.close()

# list_of_names = ("Lucas", "John", "Adam")
# print("list_of_names", list_of_names[:])

# list1 = ["A", "B", "C"]
# list2 = list1
# list2.append("D") # we are adding D to the list
# print(list1)

