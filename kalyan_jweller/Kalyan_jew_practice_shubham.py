class kalyan_jew:
    status = True
    while status:
        name=input(" Enter a customer name : ")
        number=True
        while number:
            try:
                contact_num=input("Enter your num : ")
                if contact_num.isdigit() and len(contact_num)==10:
                    number=False
                else:
                    print("invalid")
                    contact_num=input("Contact Number is invalid pleaze add 10 digit number :")
            except Exception as e:
                contact_num=input("Contact Number is invalid please add 10 digit number :")
        age1=True
        while age1:
            try:
                age = input("Enter an Age : ")
                if age.isdigit() and len(age)==2:
                    age1=False
                else:
                    print("Invalid")
                    age = input("Enter an Age : ")
            except Exception as e:
                age = input("Enter an Age : ")
        gender=True
        while gender:        
            try:
                Gender = input(" Gender is ")
                if Gender=='Male' or Gender=='Female' or Gender == 'Trans':
                    gender=False
                else:
                    print("Invalid Gender ")
                    Gender = input(" Please Enter a valid Gender : ")
            except Exception as e:
                Gender = input(" Gender is ")
        choice = input(" Enter detail are ok? : Press 'y' or 'yes' ")
        if choice=='yes' or choice=='y':
            status=False
        else:
            continue    
    # def product(self,prod_name):
    #     prod_name={}
    #     self.prod_name= ("Hello sir, what yu want to purchase ? ",prod_name)
    # class base_class(object):
    #     def __init__(self):
    #         self.A="ring"
    #         self.B="Chain"
    #         self.C="Mangalsutra"
    #         self.D="Coin"

    # my_instance = base_class()
    # print(my_instance.__dict__)

    def __init__(self,price=0, gst_charge=0,making_charges=0,discount=0,y=0):
            
        #print("Product name is : ")
        self.price = price
        self.gst_charge = gst_charge
        self.making_charges = making_charges
        self.discount=discount
        self.y=y

    def product(self):
        print("-------Product purchsed--------")
        print("""1. Ring, Price - 25000(22 kr, 1 grm)
                 2. Remove ring quantity 
                 3. Chain       - 35000(22kr, 1gm)
                 4. remove chain quantity
                 5. Bangles     - 14000(22kr, 1gm)
                 6. remove Bangles quantity
                 7. Coin        - 45000(22kr,1gm)
                 8. 4. remove Coin quantity
                 9. Exist""")
        
        
        while(1):
            c=int(input("enter a purchsed product : "))
            if (c==1):
                d=int(input("Enter a quantity :"))
                self.price=self.price+25000*d
            elif (c==2):
                d=int(input("Enter a quantity :"))
                self.price=self.price-25000*d
            elif (c==3):
                d=int(input("Enter a quantity :"))
                self.price=self.price+35000*d
            elif (c==4):
                d=int(input("Enter a quantity :"))
                self.price=self.price-35000*d
            elif (c==5):
                d=int(input("Enter a quantity : "))
                self.price=self.price+14000*d
            elif (c==6):
                d=int(input("Enter a quantity :"))
                self.price=self.price-14000*d
            elif (c==7):
                d=int(input("Enter a quantity : "))
                self.price=self.price+45000*d
            elif (c==8):
                d=int(input("Enter a quantity :"))
                self.price=self.price-45000*d
            elif (c==9):
                break
            else:
                print("please enter a vlid key ")
        self.making_charges=d*2000
        self.gst_charge=d*19

    def display(self):
        
        # self.gst_charge = int(input("enter a gst : ",self.gst_charge,"Rupees"))
        # self.making_charges = int(input(" Enter a making chrge : ", self.making_charges))
        y=self.price+self.gst_charge+self.making_charges
        self.total=("Total amount is : ",y)
        
        status = True 
        display_age = input("Enter an Age : ")
        while status:
            try:
                if len(display_age)==2:
                    status=False
                else:
                    print("Invalid")
                    display_age = input("else Enter an Age : ")
            except Exception as e:
                print("Exception : ",e)
                display_age = input("Exception Enter an Age : ")

        gender=True
        d_Gender = input(" Gender is ")
        while gender:        
            try:
                if d_Gender=='Male' or d_Gender=='Female' or d_Gender == 'Trans':
                    gender=False
                else:
                    print("Invalid Gender ")
                    d_Gender = input(" Please Enter a valid Gender : ")
            except Exception as e:
                print("Exception in Gender : ",e)
                d_Gender = input(" Gender is ")
        if int(display_age)>65:
            if d_Gender == 'Male' :
                if self.total<=200000:
                    self.total=self.total*0.8
                    self.discount=self.total*0.2
                elif 200000<self.total<=300000 :
                    self.total=self.total*0.7
                    self.discount=self.total*0.3
                elif self.total>300000:
                    self.total=self.total*0.5
                    self.discount=self.total*0.5
            elif d_Gender == 'Female':
                if self.total<=200000:
                    self.total=self.total*0.75
                    self.discount=self.total*0.25
                elif 200000<self.total<=300000 :
                    self.total=self.total*0.65
                    self.discount=self.total*0.35
                elif self.total>300000:
                    self.total=self.total*0.5
                    self.discount=self.total*0.5
        else:
            pass
        print(self.price)
        print(self.gst_charge)
        print(self.making_charges)
        print(self.discount)
        print(self.total)



def main():
    x = kalyan_jew()
    print(x.name)
    print(x.contact_num)
    print(x.age)
    print(x.gender)


    while(1):

        print("""
               1. product detail
               2. Total price
               3. Exit""")
        b=int(input("\nEnter the number."))
        if b==1:
            x.product()
        elif b==2:
            x.display()
        elif b==3:
            break
        else:
            print(" Invalid input ")
main()

        


        
        
    
    


    








            
        
            