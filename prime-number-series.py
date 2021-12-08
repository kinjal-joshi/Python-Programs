#TO PRINT A SERIES OF PRIME NUMS ACCORDING TO THE USER
while True:
    print("""1.Prime numbers upto a certain number\n2.Number of prime numbers to be displayed\n3.Prime numbers between intervals""")
    ans=str(input("\nChoose: "))

    if ans=="1":
        limit = eval(input("\nPrime numbers uptil: "))

        for x in range(2,limit+1):
            flag=0
            for y in range(2,x):
                if(x%y==0):
                    flag=1
                    break
            if flag==0:
                print("-",x, end="\n")

    elif ans=="2":
        limit = eval(input("\nEnter limit for prime num:"))

        while limit>0:
            for num in range(2,100):
                flag = 0
                for x in range(2,num):
                    if num % x == 0:
                        flag=1
                        break
                if flag==0:
                    print("-",num, end="\n")
                    limit -= 1
                if limit == 0:
                    break

    elif ans=="3":
        lower=int(input("\nEnter lower limit: "))
        upper=int(input("Enter upper limit: "))

        for x in range(lower,upper+1):
            flag=0
            for y in range(2,x):
                if(x%y==0):
                    flag=1
                    break
            if flag==0:
                print("-",x, end="\n")
    else:
        print("Invalid input! Try again.")
        
    c = str(input("\nDo you want to continue?(y/n):"))
    if (c == 'y' or c == 'Y'):
        continue
    else:
        print("bye..")
        break