#BUBBLE SORT

def bubble_sort(ls,limit):
    for i in range(len(ls)):
        for j in range(len(ls)-i-1):
            if ls[j] > ls[j+1]:
                temp = ls[j]
                ls[j] = ls[j+1]
                ls[j+1] = temp

ls = []
while True:
    limit = eval(input("Enter how many elements would you like to enter:"))
    for i in range(0,limit):
        element = eval(input()) 
        ls.append(element)     
    print("List:",ls)
    print("\nSorting using bubble sort...")
    bubble_sort(ls,limit)
    print("\nSorted list:",ls)
    c = str(input("\nDo you want to continue?(y/n):"))
    if (c == 'y' or c == 'Y'):
         continue
    else:
        print("bye..")
        break