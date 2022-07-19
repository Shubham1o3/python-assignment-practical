print(" Welcome to Kalyan jwellers ")

name = input("Enter a Name of Customer : ")
mobile=int(input(" Enter a Mobile Number : "))
gender=int(input("Gender press 1. Male, 2. Female :  "))
age = int(input(" Enter an Age : "))
print("Customer name : ", name)
print("Mobile number :",mobile)
if gender==1:
    print("Gender : Male")
elif gender==2:
    print("Gender : Female ")
else:
    pass
print(" Age : ", age)
current_price = 4828
print("Current price of gold is :",current_price)


for i in range(1):
    print("""
               Menu     
            1. Ring 
            2. Chain
            3. neckless
            4. bangles
            5. Total_Price
             """)
    
    n=int(input(" Number of items that custmor purchased : "))
    price1=0
    price2=0
    price3=0
    price4=0
    price=0
    for j in range(n):
        
        choice = int(input(" Enter a product tag number : "))
        quantity = int(input(" Enter a number of quantity "))
        if choice==1:
            price1=current_price*quantity
            print(f"{name} is purchasing ring of {quantity} gram and their price is {price1} rupees")
        elif choice==2:
            price2=current_price*quantity
            print(f"{name} is purchasing chain of {quantity} gram and their price is {price2} rupees")
        elif choice==3:
            price3=current_price*quantity
            print(f"{name} is purchasing neckless of {quantity} gram and their price is {price3} rupees")
        elif choice==4:
            price4=current_price*quantity
            print(f"{name} is purchasing bangles of {quantity} gram and their price is {price4} rupees")
        elif choice==5:
            price=price1+price2+price3+price4
        else:
            pass
        
    print(" price is ", price1)
    print(" price is ", price2)
    print(" price is ", price3)
    print(" price is ", price4)
    #price=price1+price2+price3+price4
price=price1+price2+price3+price4
print("price is ",price)


if gender==1 and age>=60:
    if price>=200000:
        t_price=price*0.9
        if price>=500000:
            t_price=price*0.85
            if price>=1000000:
                t_price=price*0.8
    else:
        t_price=price*1
elif gender==1 and age<=60:
    if price>=200000:
        t_price=price*0.95
        if price>=500000:
            t_price=price*0.9
            if price>=1000000:
                t_price=price*0.85
    else:
        t_price=price*1
elif gender==2 and age>=60:
    if price>=200000:
        t_price=price*0.85
        if price>=500000:
            t_price=price*0.8
            if price>=1000000:
                t_price=price*0.75
    else:
        t_price=price*1
elif gender==2 and age<=60:
    if price>=200000:
        t_price=price*0.9
        if price>=500000:
            t_price=price*0.85
            if price>=1000000:
                t_price=price*0.8
    else:
        t_price=price*1
else:
    pass


if quantity>=10:
    making_charges=589*1.1*quantity
else:
    making_charges=589

print("Customer name : ", name)
print("Mobile number :",mobile)
if gender==1:
    print("Gender : Male")
elif gender==2:
    print("Gender : Female ")
else:
    pass
print(" Age : ", age)
print("Current price is ",current_price)
print("Making charges is ",making_charges)
print(" Total purchase amount is ", t_price+making_charges)
    
                

        
        

