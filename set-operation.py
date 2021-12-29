#FUNCTION DEFINATIONS FOR SET PROGRAM

def setstats(x,y):
    print("The stats of the sets",x,"and",y,"are:\n")
    a = x.isdisjoint(y)
    if a == 1:
        print("1. The sets are disjoint.")
    else:
        print("1. The sets are not disjoint.")
    b = x.issuperset(y)
    c = y.issuperset(x)
    if b == 1 and c == 1:
        print("2.",x,"is a super set of ",y,"and",y,"is a superset of",x)
    elif b == 1 and c == 0:
        print("2.",x,'is a superset of',y,"but",y,"is not a superset of",x)
    elif b == 0 and c == 1:
        print("2.",x,'is not a superset of',y,"but",y,"is a superset of",x)
    else:
        print("2.",x,'is not a superset of',y,"and",y,"is not a superset of",x)
    d = x.issubset(y)
    e = y.issubset(x)
    if d == 1 and e == 1:
        print("3.",x,"is a subset of ",y,"and",y,"is a subset of",x)
    elif d == 1 and e == 0:
        print("3.",x,'is a subset of',y,"but",y,"is not a subset of",x)
    elif d == 0 and e == 1:
        print("3.",x,'is not a subset of',y,"but",y,"is a subset of",x)
    else:
        print("3.",x,'is not a subset of',y,"and",y,"is not a subset of",x)

def add_element(x):
    count = int(input("How many values would you like to add?"))
    while count > 0:
        obj = input("Enter element: ")
        x.add(obj)
        count -= 1
    print("Elements added successfully!")
    print("Your set is :",x)

def remove_element(x):
    element = input("Enter the element that you want to remove: ")
    x.remove(element)
    print("Element removed successfully!")
    print("Your set is :",x)
    
def intersection(x,y):
    i = x.intersection(y)
    print("The intersection of",x,"and",y,"is",i)
    
def union(x,y):
    u = x.union(y)
    print("The union of",x,"and",y,"is",u)
    
def difference(x,y):
    d = x.difference(y)
    print("The difference of",x,"and",y,"is",d)
    
def sym_diff(x,y):
    s = x.symmertric_difference(y)
    print("The symmetric difference of",x,"and",y,"is",s)


#MAIN FOR SET PROGRAM

A = {'apple','cherry'}
B = {'orange','berry','apple'} 
primarySet = None

while True:
    print("Current Sets: \n","Set A:",A,"\n Set B:",B)
    print("\nWhat would you like to do?")
    print("1. Edit the Set. \n2. Perform Set Functions. \n3. Get Set Stats. \n4. Exit")
    ans = eval(input("Enter Number: "))
    
    if ans == 1:
        editset=input("\nWhich set do you want to edit? A/B")
        if editset == 'A' or editset == 'a':
            x = A
        elif editset == 'B' or editset == 'b':
            x = B
        else:
            print("Invalid Input.")
            break
            
        editfunction=eval(input("\nWhat would you like to do? \n1. Add an element. \n2. Remove an element. \n3. Sort the set. \n4. Clear the set. \nChoose:"))
        
        if editfunction == 1:
            add_element(x)
        elif editfunction == 2:
            remove_element(x)
        elif editfunction == 3:
            print("The sorted set is:",sorted(x))
        elif editfunction == 4:
            x.clear()
            print("Your set is empty.")
        else:
            print("Invalid Input.")
            break
            
    elif ans == 2:
        funcset = input("\nWhat set is going to be your primary set?")
        if funcset.lower() == 'a':
            primarySet = 'a'
            x = A
            y = B
        elif funcset.lower() == 'b':
            primarySet = 'b'
            x = B
            y = A
        else:
            print("Invalid Input.")
            break
            
        funcval = eval(input("\nWhat would you like to do? \n1. Find Difference. \n2. Find Intersection. \n3. Find Union. \n4. Find Symmetric Difference. \nChoose:"))
        
        if funcval == 1:
            if primarySet == 'a':
                difference(x,y)
            else:
                difference(y,x)
                
            
        elif funcval == 2:
            if primarySet == 'a':
                intersection(x,y)
            else:
                intersection(y,x)
        
        elif funcval == 3:
            if primarySet == 'a':
                union(x,y)
            else:
                union(y,x)
        
        elif funcval == 4:
            if primarySet == 'a':
                sym_diff(x,y)
            else:
                sym_diff(y,x)
        
        else:
            print("Invalid Input.")
            break
            
    elif ans == 3:
        setstats(A,B)
        
    elif ans == 4:
        print("Byee!")
        break
    
    else:
        print("Invalid Input.")
        break
        
    c = str(input("\nDo you want to continue?(y/n):"))
    if (c == 'y' or c == 'Y'):
        continue
    else:
        print("bye..")
        break