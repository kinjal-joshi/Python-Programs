#LINEAR SEARCH AND BINARY SEARCH

def linear_search():  
        flag = 0
        for x in range(len(ls)):
            if int(target) == ls[x]:
                flag = 1
                break      

        if flag == 0:
            print("\nNumber not found")
        else:
            print("\nNumber found at position",x+1)

def binary_search(ls,target):
        beg = 0
        end = limit - 1
        mid = 0
        while beg <= end:
            mid = (end+beg)//2
            if ls[mid] < int(target): 
                beg = mid + 1
            elif ls[mid] > int(target): 
                end = mid - 1 
            else:
                return mid
        return -1   

while True:
    ans = eval(input("""Search number through:
1. Linear search
2. Binary search
Choose: """))

    if ans == 1:
        ls = []
        limit = eval(input("Enter how many elements would you like to enter:"))
        for i in range(0,limit):
            element = eval(input()) 
            ls.append(element)     
        print("List:",ls)
        target = input("\nEnter the number you want to search:")
        linear_search()   


    elif ans == 2: 
        ls = []
        limit = eval(input("Enter how many elements would you like to enter:"))
        for i in range(0,limit):
            element = eval(input()) 
            ls.append(element)     
        print("List:",ls)
        ls.sort()
        print("Sorted list:",ls)
        target = input("\nEnter the number you want to search:")
        pos = binary_search(ls, int(target))  
        if pos >= 0:  
            print("\nNumber found at position", int(pos+1))
        else:
            print("\nNumber not found") 

    else:
        print("Incorrect input!")
    c = str(input("\nDo you want to continue?(y/n):"))
    if (c == 'y' or c == 'Y'):
        continue
    else:
        print("bye..")
        break