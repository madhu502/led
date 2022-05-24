# def add(a,b):
#     print(a+b)
# add(2,3)

# def add(a,b):
#     print(a+b)
# if __name__=="__main__":
#     add(2,3)

# import math
# a=dir(math)
# print (a)

# a=2.44444456
# print(round(a,2))

# import math
# a=20
# print(math.sqrt(a))


# import math
# print(math.sqrt(9))
# print(math.sqrt(25))
# print(math.sqrt(16))

# import random
# a=dir(random)
# print(a)
 
# import random 
# list1=[1,2,3,4,5,6]
# print(random.choice(list1))

# import random
# r1=random.randint(5,15)
# print("Random number between 5and 15 is %s"%(r1))

# r2=random.randint(-10,-2)
# print("Random number between -10 and -2 is %d"%(r2))

# import random
# sample_list=[1,2,3,4,5]
# print("original list:")
# print(sample_list)
# random.shuffle(sample_list)
# print("\nAfter the first shuffle:")
# print(sample_list)

# import random
# for i in range (50):
#     print(random.randint(20,50))

# import random
# a=[]
# n=int(input("Enter a number:"))
# for i in range (n):
#     a.append(random.randint(1,20))
# print("randomised list is :",a)

# import datetime 
# s=datetime.datetime.now()
# print(s)

# import datetime
# x=datetime.datetime.now()
# print(x.year)
# print(x.strftime("%A"))
# print(x.strftime("%a"))
# print(x.strftime("%w"))
# print(x.strftime("%b"))
# print(x.strftime("%B"))
# print(x.strftime("%Y"))
# print(x.strftime("%y"))
# print(x.strftime("%m"))
# print(x.strftime("%d"))

# import datetime
# x=datetime.datetime.now

# data=[1,2,3,4,5,]
# print (data)

# data=["sunil","Roshan",29]
# for i in data:
#     print(i)

# data=["sunil","Roshan",29]
# print(data[1])

# data=["sunil","Roshan",29]
# print(data[0:2])

# data=list(range(0,10,1))
# print(data)

# data=["sunil","Roshan",29]
# print(data)
# data.append(9)
# data.append("programming")
# print(data)

# data=["sunil","roshan",29]
# print (data)
# data.insert(2,"battle")
# print(data)

# mixed_list=[{1,2},[5,6,7],{"a":"r"}]
# number_tuple=(3,4)
# mixed_list.insert(1,number_tuple)
# print("updated list:",mixed_list)

# data=["sunil","roshan",29]
# print(data)
# data[0]=8
# data[1]=10
# data[2]=2
# print(data)

# data=["sunil","roshan",29]
# print(data)
# del data[1]
# print(data)

# data=["sunil","roshan",29]
# print(data)
# data.remove(29)
# print(data)

# data=['sunil','roshan',29]
# print(data)
# data.pop()
# print(data)

# data=["sunil","roshan",29]
# data2=["a","b",12]
# print(data+data2)

# data=["sunil","roshan",29]
# data2=[]
# data2=data.copy()
# print(data)
# print(data2)

# data=["sunil","roshan",29]
# data2=["a","b",12]
# data2.extend(data)
# print(data2)

# data=["sunil","roshan",29]
# data.clear()
# print(data)

# data=("sunil","roshan",21)
# print(type(data))
# print(data)

# data=("sunil","roshan",21)
# for i in  data:
#     print(i)

# data=("sunil","roshan",21)
# print(data[1])

# data=("sunil","roshan",21)
# print(data[0:2])

# data=tuple(range(0,10,1))
# print(data)

# a=("suniol","ram",21)
# print(len(a))

# nums=(1)
# nums1=(1,)
# print(type(nums))
# print(type(nums1))
# name=("sunil")
# name1=("sunil",)
# print(type(name))
# print(type(name1))

# data=("sonam","ram",21,["sunil","aakash",23])
# print(data)
# print(len(data))
# data[3].pop()
# print(data)
# data[3].append("master")
# print(data)
# data[3].remove("aakash")
# print(data)

# print('maximum is:',max(1,2,5,4,3))
# print('minimum is:',min(1,2,8,7,5))


Tuple1=("ram","shyam","mohan")
print("original tuple",Tuple1)
List1=list(Tuple1)
print("original list",List1)
List1.insert(3,"krishna")
print("changed list",List1)
Tuple2=tuple(List1)
print("adding new name in tuple:",Tuple2)
















