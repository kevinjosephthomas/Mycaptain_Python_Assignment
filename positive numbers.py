def print_positive_numbers(numbers):
   
     positive_numbers = [i for i in numbers if i > 0]


     print(positive_numbers)

 

list1=[]
for i in range(1,6):
     a=int(input("Enter the numbers: "))
     list1.append(a)
print_positive_numbers(list1)
list2=[]
for i in range(1,6):
    b=int(input("Enter the number: "))
    list2.append(b)
print_positive_numbers(list2)


