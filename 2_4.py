# num1 = 1
# num2 = 10
# num3 = 1000
# sum_of_all_numbers = num1 + num2 + num3
# print("Sum is {0:n}".format (sum_of_all_numbers))

list_of_numbers = [1, 10, 1000]
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
num = float(input("Enter the first grade:"))
grades.append(num)
num = float(input("Enter the second grade:"))
grades.append(num)
num = float(input("Enter the third grade:"))
grades.append(num)
num = float(input("Enter the fourth grade:"))
grades.append(num)
num = float(input("Enter the fifth grade:"))
grades.append(num)
minimumGrade = min(grades)
grades.remove(minimumGrade)
minimumGrade = min(grades)
grades.remove(minimumGrade)
average = sum(grades) / len(grades)
print("Average Grade: {0: .2f}".format (average))
