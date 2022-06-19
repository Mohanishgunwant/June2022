"""1: Write a Python program to count the number of strings where the string length is 2 or more and the first and
last character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2"""

"""
List = ['abc', 'xyz', 'aba', '1221']
Newlist= [i for i in List if len(i) >= 2 and i[0] == i[-1]]
print(len(Newlist))   """



"""6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a
 given list of non-empty tuples. 
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]"""

"""List = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]"""

"""Write a Python program to remove duplicates from a list.
List = [1,5,6,9,10,11,5,6,8,11]
List2= set(List)
List3=[]
for i in List2:
    List3.append(i)
print(List3)

"""

"""Write a Python program to clone or copy a list.
List= [1,6,8,"apple","orange",10.8]
print(List)

#way1:
# List2=List.copy()
# print(List2)

# way2:
# list2=list(List)
# print(list2)

#way3:
# List2=[]
# for i in List:
#     List2.append(i)
# print(List2)

"""

"""Write a Python function that takes two lists and returns True if they have at least one common member
list1 = [1,"apple",5,9,22,18,19]
list2 = [11,15,19,55,79,"apple"]

"""

