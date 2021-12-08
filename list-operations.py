#TO PERFORM FOR LIST OPERATIONS

def remove_element():
    rem = str(input("Enter the element would you like to remove:"))
    if (rem in ls):
        ls.remove(rem)
        print('Element removed succesfully..')
    else:
        print("Item does not exist.")
    
def add_element():
    add = str(input("Enter an element to add:"))
    ls.append(add)
    print("Element added succesfully..")

def modify_element():
    index = eval(input("Enter index number of the element you want to modify:"))
    mod = str(input("Enter the modified value:"))
    ls[index] = mod
    print("Element modified succesfully..")

def get_index():
    for i in range(len(ls)):
        print("->",ls[i],"at index",str(i))

ls = []
limit = eval(input("Creating the list: \nHow many elements would you like to enter:"))
print("Enter the elements:")
for i in range(0,limit):
    element = str(input()) 
    ls.append(element)

while True:
        ans = eval(input("""What would you like to do?:
1. Add an element
2. Remove an element
3. Get index number of the elements
4. Modify an element
5. Display the list
6. Reverse the list 
7. Sort the list
8. Delete the list
9. Exit
Choose: """))
        
        if ans == 1:
            add_element()
            print("Your list is:\n")
            print(ls)
            
        elif ans == 2: 
            remove_element()
            print("Your list is:\n")
            print(ls)
            
        elif ans == 3:
            print("The indexes are:")
            get_index()
            
        elif ans == 4:
            modify_element()
            print("Your list is:\n")
            print(ls)

        elif ans == 5:
            print("Your list is:\n")
            print(ls)
            
        elif ans == 6:
            ls.reverse()
            print("List reversed successfully..")
            print("Your list is:\n")
            print(ls)
                
        elif ans == 7:
            ls.sort()
            print("List sorted successfully..")
            print("Your list is:\n")
            print(ls)
            
        elif ans == 8:
            del ls
            print("List deleted successfully..") 
            
        elif ans == 9:
            print("bye..")
            break 
            
        else:
            print("Incorrect input!")
            
        c = str(input("\nDo you want to continue?(y/n):"))
        if (c == 'y' or c == 'Y'):
            continue
        else:
            print("bye..")
            break