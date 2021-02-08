#1. Write a Python program to print the following string in a specific format
Option=int(input("Choose Program No from given list." +
"0: For All one by one\n"+
"1: To print the string in a specific format\n"+
"2: Accepts the radius of a circle from the user and compute the area\n"+
"3: Accepts a sequence of comma-separated no from the user and generates a " +
    "list and a tuple with those numbers\n" +
"4: To accept a filename from the user and print the extension of that\n"+
"5: Program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20\n" +
"6: Function to find the maximum and minimum numbers from a sequence of numbers\n."+ 
    "Note: Do not use built-in functions.\n"+
"7: Program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'.\n"+
    "Use the characters exactly once\n"+
"8: Program to get all possible two digit letter combinations from a digit (1 to 9) string.\n"+
    "string_maps = {1:abc,2: def,3: ghi,4: jkl,5: mno,6: pqrs,7:tuv,8: wxy,9:z}\n" +
"9: Program to find the number of notes (Sample of notes: 10, 20, 50, 100, 200 and 500 ) " +
    "against a given amount. Range - Number of notes(n) : n (1 <= n <= 1000000)\n"+
"10: Write a Python program to count the number of characters (character frequency) in a string.\n"+
    "Sample String : google.com'\n"+
    "Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}\n"+
"11: Program to add 'ing' at the end of a given string (length should be at least 3)." +
    " the given string already ends with 'ing' then add 'ly' instead. If the string " +
    "length of the given string is less than 3, leave it unchanged\n" +
"12 :Program to create a list by concatenating ['item1','item2'] a given list which goes from 1 to n." +
"13: Program to compute the difference between two lists.\n"+
"14: Program to create and display all combinations of letters,selecting each letter from a different key in a dictionary.\n" +
"15: Program to replace the last value of tuples in a list.\n" +
"16 to 19: Program to construct the patterns\n" +
"20: Program to print Pascal’s Triangle.\n"))


if Option==1 or Option==0:
    list1=["Twinkle, twinkle, little star,",
    "How I wonder what you are!" ,
    "Up above the world so high, " ,
    "Like a diamond in the sky. "]

    a=0
    while a<len(list1)+2:
        print("\t "*(a%len(list1)-1 if a%len(list1)==3 else a%len(list1)), list1[a%len(list1)])
        a+=1

#Accepts the radius of a circle from the user and compute the area
if Option==2 or Option==0:
    n=0
    flag=False
    while flag==False:
        radius=int(input("Enter the radius of circle (r) :"))
        if radius>0:
            flag=True
        else:
            print("Enter valid radius")

    print("Area of circle having radius ", radius , " is :",(22/7)*(radius**2))

#3. Accepts a sequence of comma-separated no from the user and generates a list and a tuple with those numbers.
if Option==3 or Option==0:
    flag=False
    while flag==False:
        str1=input("Enter Sequence of comma-separated No :")
        if len(str1)>0:
            flag=True
        else:
            print("Enter valid Sequence of comma-separated No")

    list1=list(str1.split(","))
    tuple1=tuple(str1.split(","))
    print("List :", list1 , "\nTuple :",tuple1)

#Write a Python program to accept a filename from the user and print the extension of that
if Option==4 or Option==0:
    n=0
    flag=False
    while flag==False:
        str1=input("Enter the file name with extension :")
        if str1.rindex(".")>0:
            flag=True
        else:
            print("Enter valid file name with extension")
    
    str1=str1[str1.rindex("."):len(str1)]
    print("File Extension is : ", str1)

#"5: Program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20\n" +
if Option==5 or Option==0:
    no1=int(input("Enter First No :"))
    no2=int(input("Enter Second No :"))
    sum=no1+no2
    if sum>=15 and sum<=20:
        sum=20
    print("Sum of ",no1, " and ",no2," is (except sum beteen 15 to 20 is 20) :", sum)

# 6: Function to find the maximum and minimum numbers from a sequence of numbers\n."+ 
#     "Note: Do not use built-in functions.\n"+
if Option==6 or Option==0:
    n=0
    flag=False
    while flag==False:
        n=int(input("Enter size of list :"))
        if n>0:
            flag=True
            list1=[]
        else:
            print("Enter valid Size of list")
        
        while n>0:
            list1.append(int(input("Enter element " + str(len(list1)+1) +" of list :")))
            n-=1

    def findMaxMin(li):
        if len(li)>0:
            max1=li[0]
            min1=li[0]
            for var in li:
                if var>max1:
                    max1=var
                if var<min1:
                    min1=var
            return min1,max1

    t1=findMaxMin(list1)

    if len(t1)>0:
        print(t1,"Minimum :", t1[0]," and maximum: ",t1[1])
    else:
        print("List is empty")


# "7: Program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'.\n"+
#     "Use the characters exactly once\n"+
if Option==7 or Option==0:
    t1="aeiou"
    t1=list(t1)
    count=0
    count2=0

    def permutation(li, start, end,count2): 
        if start==end-1:
            global count 
            count=count+1
            print(count,": ",''.join(li) )
        else: 
            for j in range(start,end): 
                li[start], li[j] = li[j], li[start] 
                permutation(li, start+1, end,count2+1)
                li[start], li[j] = li[j], li[start] 

    permutation(t1,0,len(t1),count2)


# "8: Program to get all possible two digit letter combinations from a digit (1 to 9) string.\n"+
#     "string_maps = {1": "abc,2": "def,3": "ghi,4": "jkl,5": "mno,6": "pqrs,7": "tuv,8": "wxy,9": "z}\n" +
if Option==8 or Option==0:
    string_maps = {1: "abc",2: "def",3: "ghi",4: "jkl",5: "mno",6: "pqrs",7: "tuv",8: "wxy",9: "z"}
    count=0
    
    def Combination(li):
        count=0
        for j in li.values():
            for k in li.values():
                count+=1
                print(
                    count,": ",j, k)

    Combination(string_maps)
# "9: Program to find the number of notes (Sample of notes: 10, 20, 50, 100, 200 and 500 ) " +
#     "against a given amount. Range - Number of notes(n) : n (1 <= n <= 10,00,000)\n"+

if Option==9 or Option==0:
    n=0
    flag=False
    while flag==False:
        n=int(input("Enter the amount betwween 1 to 10,00,000 :"))
        if n>0 and n<=1000000:
            flag=True
            list1=[]
        else:
            print("Enter valid amount between 1 to 10,00,000")
    list1.append("Amount is : " + str(n))
    
    if n>=500:
        list1.append("500 x " + str(n//500))
        n=n%500
    if n>=200:
        list1.append("200 x " + str(n//200))
        n=n%200
    if n>=100:
        list1.append("100 x " + str(n//100))
        n=n%100
    if n>=50:
        list1.append("50 x " + str(n//50))
        n=n%50
    if n>=20:
        list1.append("20 x " + str(n//20))
        n=n%20
    if n>=10:
        list1.append("10 x " + str(n//10))
        n=n%10
    if n>=5:
        list1.append("5 x " + str(n//5))
        n=n%5
    if n>=1:
        list1.append("1 x " + str(n))
        n=0                        
    print(*list1,sep="\n")
   
# "10: Write a Python program to count the number of characters (character frequency) in a string.\n"+
#     "Sample String : google.com'\n"+
#     "Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}\n"+
# ""))
if Option==10 or Option==0:
    n=0
    flag=False
    while flag==False:
        n=(input("Enter String:")).upper()
        if n!="":
            flag=True
            list1={}
        else:
            print("Enter valid String")
    
    for char in n:
        flag=False
        for dict1 in list1.items():
            if char==dict1[0]:
                list1.update({dict1[0]:dict1[1]+1})
                flag=True
                break
        if flag==False:
            list1[char]=1

    for key, value in list1.items():
        print(key, ' : ', value)
   

# 11. Write a Python program to add 'ing' at the end of a given string (length should
# be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
# string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'
if Option==11 or Option==0:
    n=0
    flag=False
    while flag==False:
        n=(input("Enter String at least 3 character:"))
        if len(n)>0:
            flag=True
        else:
            print("Enter valid String")

    if len(n)<=3:
        n=n+""
    elif n.count("ing")>0:
        n=n+"ly"
    else:
        n=n+"ing"

    print(n)

 
#12. Write a Python program to create a list by concatenating a given list which
# range goes from 1 to n.
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
if Option==12 or Option==0:
    n=0
    flag=False
    while flag==False:
        str1=input("Enter list comma-separated :")
        if len(str1)>0:
            flag=True
        else:
            print("Enter valid comma-separated list")

    flag=False
    while flag==False:
        n=int(input("Enter range >= 1 :"))
        if n>0:
            flag=True
        else:
            print("Enter valid range")

    list1=[]
    for val in str1.split(","):
        a=1
        while a<=n:
            list1.append(val+str(a))
            a+=1
    
    print(*list1,sep="\n")


# Write a Python program to compute the difference between two lists.
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green",
# "blue"]
# Expected Output:
# Color1-Color2: ['white', 'orange', 'red']
# Color2-Color1: ['black', 'yellow']
if Option==13 or Option==0:
    flag=False
    while flag==False:
        str1=input("Enter comma-separated first List :")
        if len(str1)>0:
            flag=True
        else:
            print("Enter valid comma-separated first list")

    flag=False
    while flag==False:
        str2=input("Enter comma-separated Second List :")
        if len(str2)>0:
            flag=True
        else:
            print("Enter valid comma-separated second list")

    list1=str1.split(",")
    list2=str2.split(",")
    print("List 1: ", list1)
    print("List 2: ", list2)

    for val in list1:
        for key in list2:
            if val==key:
                list1.remove(val)
                list2.remove(key)
   
    print("List1-List2",list1)
    print("List2-List1",list2)

# 14. Write a Python program to create and display all combinations of letters,
# selecting each letter from a different key in a dictionary.
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd
if Option==14 or Option==0:
    n=0
    flag=False
    while flag==False:
        n=int(input("Enter no of values in dictionary :"))
        if n>0:
            flag=True
        else:
            print("Enter valid no")
    
    dict1={}
    a=1
    while a<=n:
        str1=input("Enter " + str(a) + " element of Dictionary (str) :")
        dict1.update({a:list(str1)})
        a+=1

    count=0
    def mergeList(li1,li2):
        for i in li1:
            for j in li2:
                global count
                count+=1
                print(count,"-> ",i+j)

    a=1
    while a<=len(dict1):
        list1=dict1[a]
        b=a+1
        while b<=len(dict1):
            list2=dict1[b]
            mergeList(list1,list2)
            b+=1 
        a+=1


# 15. Write a Python program to replace the last value of tuples in a list.
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
if Option==15 or Option==0:
    list1=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
    t1=(70, 80, 100)
    
    print("List before update : ", list1)
    list1[len(list1)-1]=t1
    print("List after update : ", list1)
    
# 16. Write a Python program to construct the following pattern, using a nested for
# loop.
# For n = 9
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# 17. Write a Python program to construct the following pattern, using a nested for
# loop.
# For n = 5
# * * * *
# * *
# * * * * *
#  * *
# * * * *
# 18. Write a Python program to construct the following pattern, using a nested for
# loop.
# For n = 3
# 1 1
# 1 2 2 1
# 1 2 3 2 1
# For n = 5
# 1 1
# 1 2 2 1
# 1 2 3 3 2 1
# 1 2 3 4 4 3 2 1
# 1 2 3 4 5 4 3 2 1
# 19. Write a Python program to construct the following pattern using any loop.
# For n = 5
# *
# * *
# * * *
# * * * *
# * * * * *
if Option==16 or Option==17 or Option==18 or Option==19 or Option==0 :
    n=0
    flag=False
    while flag==False:
        n=int(input("Enter height of Piramid (Odd No): "))
        if n%2!=0:
            flag=True
        else:
            print("Not a valid No")

    # No Pattern
    a=1
    while a<=n:
        b=1
        while b<=a:
            print(b,end=" ")
            b=b+1
        print()
        a=a+1

    # * Pattern 1
    print("\nPattern 1")
    a=1
    while a<=n:
        b=n
        while b>=a:
            print("*",end=" ")
            b=b-1
        print()
        a=a+1

    # * Pattern 2
    print("\nPattern 2")
    a=1
    c=0
    while a<=n:
        if a>int(n/2)+1:
            c=n-a+1
        else:
            c=a
            b=1
    
        while b<=c :
            print("* ",end=" ")
            b=b+1
        print()
        a=a+1

    # * Pattern 3
    print("\nPattern 3")
    a=1
    c=n-1
    while a<=n:
        b=1
        while b<=n :
            if b<=c:
                print(" ",end=" ")
            else:
                print("*",end=" ")
            b=b+1
        print()
        a=a+1
        c-=1

    # * Pattern 4
    print("\nPattern 4")
    mid=int(n/2)+1
    a=1
    c=1
    while a<=n:
        b=1
        while b<=c+abs(mid-a) :
            if b<=abs(mid-a):
                print(" ",end=" ")
            else:
                print("*",end=" ")
            b=b+1
        print()
        a=a+1
        if a>mid:
            c-=2
        else:
            c+=2


    # * Pattern 5
    print("\nPattern 5")
    first=0
    mid=int(n/2)
    last=n-1

    a=0
    while a<n:
        b=0
        while b<n:
            if (a==first and (b==first or b>=mid)) or (a==mid) or (a==last and (b<=mid or b==last)) or (a<mid and (b==first or b==mid)) or a>mid and (b==last or b==mid):
                print("* ",end=" ")
            else:
                print("  ",end=" ")
            b=b+1
        a=a+1
        print("")

    print("\nPattern 6")
    a=1
    c=1

    b1=2*n-3
    d=b1
    while c<=n:
        a=1
        while a<=c:
            print('{0:3}'.format(a),end="")
            a+=1
        while d>0:
            print('{0:3}'.format("  "),end="")
            d-=1
        a-=1
        while a>=1:
            if a==n:
                a-=1
                continue
            print('{0:3}'.format(a),end="")
            a-=1
        b1-=2
        d=b1
        print()
        c+=1

# 20. Write a Python program to print Pascal’s Triangle
if Option==20 or Option==0 :
    n=0
    flag=False
    while flag==False:
        n=int(input("Enter height of Piramid (Odd No): "))
        if n%2!=0:
            flag=True
        else:
            print("Not a valid No")


    a=[]
    for i in range(n):
        a.append([])
        a[i].append(1)
        for j in range(1,i):
            a[i].append(a[i-1][j-1]+a[i-1][j])
        if(n!=0):
            a[i].append(1)
    for i in range(n):
        print("   "*(n-i),end=" ",sep=" ")
        for j in range(0,i+1):
            print('{0:6}'.format(a[i][j]),end=" ",sep=" ")
        print()