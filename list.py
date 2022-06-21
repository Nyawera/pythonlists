# Write a function that takes one urgument as a list a=[2,3,4,8]
# and remove the second last item from that list
# and returns the whole list without the removed item.




def nums(a):
    del a [-2]
    return a 
    print(nums[2,3,4,8])

    # Write a python program that has a list 
    # and counts the number occurrences of Monday

day =["Monday","Tuesday","Friday","Monday"] 

# # #method1
def monday_occurances():
    days = ["Monday","Tuesday","Friday","Monday"]
    print(days.count("Monday"))
monday_occurances()    

# # #method2
days = ["Monday","Tuesday","Friday","Monday"]
print(days.count("Monday"))

# # # Write a python function named smallest that accepts a list of unsorted integers
# # # and returns the smalest numbers in the list.Example:
# # #     smallest([3,6,8,2,4,1,5,7])

def smallest(smallest):
    smallest.sort()
    print(smallest[0])
    return smallest
smallest([3,6,8,2,4,1,7,5,7])

# # Write a function named divisible_by_seven that;using the range
# # function and a for loop returns a list containing all the numbers between 100 and 200
# # that are divisible by 7.


def divisible_by_seven():
    tut=[]
    for num in range(100,200):
        if num%7==0:
            tut.append(num)
        print(tut)
    
divisible_by_seven()

#method2
def divisible_by_seven():
    x =[n for n in range (100,200) if n%7==0]
    return x
print(divisible_by_seven())
      

# # Write a python program that takes two inputs(as integers) from a user and adds the 
# # 2 numbers,checks if the sum is greater than 10,less than 10 or equal 10 
# # and prints a staement after each check.
def conditions():
    a = int(input("Enter first Number "))
    b = int(input("Enter second Number"))
    sum = a+b
    if sum > 10:
        print("greater than")
    elif sum < 10:
        print("less than")
    elif sum==10:
        print("Equal to")
conditions()        

    # Write a function that takes one urgument which is a list ,a=[1,2,3,4,5]
# and returns True if 4 is present in the 
# list and False is 4 is not in the list.



a = [1,2,3,4,5]
def takes(a):
    for num in a:
     if 4 in a:
        print("4 is present")
     else:
        print("4 is not")
takes([1,2,3,4,5])


# Write a function that takes one urgument which is a list 
# fruits=["apples","pineapples","grapes"] and removes the last fruit from
# from the list returns the list without the removed fruit.

    
fruits = ["apples","pineapples","grapes"]
def remove_fruit(fruits):
    fruits.pop()
    print(fruits)
remove_fruit(["apples","pineapples","grapes"])

# Write a pyton program that takes in a list of cars,
# cars=["Ford","BMW","Volvo"] and returns a sorted list

car = ["Ford","BMW","Volvo"]
def cars(): 
    car.sort()
    print(car)
cars()
  




     

    


    


   