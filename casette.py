print ("*"*54,"WELCOME TO BLUE RAY DIGITAL CASSETTES AND CD EXHIBITION","*"*54)

print ("*"*64,"CUSTOMER SATISFACTION IS OUR GOAL","*"*64)

import os 

from pickle import load, dump

import datetime

import string 

MFile ="Master.dat"

File1 = "cassettes.dat"

File2 = "Balance.dat"

File3 ="Customer.dat"

Cdate = datetime.datetime.now()                             #  Current date and time 




                                                            # Class for date

class  Cast_Date :

    def __init__(self):

        self.dd = Cdate.day

        self.mm = Cdate.month

        self.yy = Cdate.year

        




        

class Master:

    def __init__(self):

        self.Cast_Code = 0                              # cassette/CD code -(Like, 1, 2, 3 etc.)

        self.Cast_Name = ""                             # Title of the cassette/CD

        self.Cast_Comp = ""                             # cassette/CD company

        self.Cast_Price = 0                             # Price per cassette/CD

        

    def Check_Code(self, C_Code):

        MList = list()

        TRec = list()

        Flag = False         # To check if Cast_Code is in master.dat or not

        if os.path.isfile("Master.dat"):

            Mobj = open("Master.dat", 'rb')

            try:

                while True:

                    MRec = []# For extracting master.dat records                     

                    MRec = load(Mobj)

                    if (C_Code == MRec[0]):

                        TRec = MRec

                    MList.append(MRec[0])

            except EOFError:

                pass

            for i in range(len(MList)):

                if (C_Code == MList[i]):

                    Flag = True

                    break

            Mobj.close()

         # Flag for Master data entry and TRec for Cassette data entry

        return Flag, TRec

    

    # For Master data entry

    def Master_Entry(self):

        TRec = list() # A temporary list to store master record

        print("\nAdd Master Cassette/CD")

        ch='Y'

        while ch=='Y':

            self.Cast_Code = int(input("\nCassette/CD Code [Enter 6 digit code]: "))

            while len(str(self.Cast_Code))<6 or len(str(self.Cast_Code))>6:

                print ("Please Enter correct code!")

                self.Cast_Code = int(input("Cassette/CD Code [Enter 6 digit code ]: "))

            Flag, TRec = self.Check_Code(self.Cast_Code)

            if (Flag == False):

                ch=input("Enter the number of entries to be made:")

                for i in range (ch):

                    self.Cast_Name = raw_input("Cassette/CD Name :")

                    self.Cast_Comp = raw_input("Company Name:")

                    self.Cast_Price = float(input("Individual Cassette/CD price :"))

                    N,C,P=1,1,1

                    if (self.Cast_Name == 0 or len(self.Cast_Name) > 25):

                        N=0                       

                    if (self.Cast_Comp == 0 or len(self.Cast_Comp) > 25):

                        C=0

                    if (self.Cast_Price <= 0):

                        P=0

                    while N==0 or C==0 or P==0:

                        if (self.Cast_Name == 0 or len(self.Cast_Name) > 25):

                            print("Cassette/CD Name should not greater than 25")                                               

                            self.Cast_Name = raw_input("Cassette/CD Name :")

                            N=1      

                        elif (self.Cast_Comp ==0 or len(self.Cast_Comp)  > 25):                                       

                            print("Company Name should not greater than 25")

                            self.Cast_Comp = raw_input("Company Name:")

                            C=1

                        elif (self.Cast_Price <= 0):

                                print("Enter valid price for Cassette/CD")

                                self.Cast_Price = float(input("Individual Cassette/CD price:"))

                                P=1




                    else:

                        with open(MFile, 'ab+') as Mobj:

                            if not Mobj:

                                print (MFile, "is not created")

                            else:

                                # Appends data into a sequence object                                     




                                MList = list()

                                MList.append(self.Cast_Code)

                                MList.append(self.Cast_Name)

                                MList.append(self.Cast_Comp)

                                MList.append(self.Cast_Price)                                       

                               # Write data into binary file




                                dump(MList, Mobj)




                               

                              

            else:

                    

                print ("\ncode", self.Cast_Code,"is already in 'Master.dat' file")

                ch = raw_input("\n\nAdd new Cassette/CD code? <Y?N>: ")                                

                ch = ch.upper()

                if ch=='Y':

                    self.Cast_Code =int(input("\nCassette/CD Code [Enter 6 digit code]: "))                               

                    continue

                else:

                    break







    def Master_Display(self):

        if not os.path.isfile(MFile):

            print (MFile, "file does not exist")

        else:

            Mobj = open(MFile, 'rb')

            print ("\nCassette/CD Master Report")

            print ("=" * 100)

            print (" Code", "\tCassette/CD Name"),(" "*(25-len("Cassette/CD Name"))), ("\tCompany Name"),(" "*(25-len("Company Name"))), "\t\tPrice"                                                 

            print ("-" * 100)

            try:

                while True:

                    MRec = []

                    MRec =load(Mobj)

                    print (str(MRec[0]), "\t",MRec[1],(" "*(25-len(MRec[1]))),"\t", MRec[2],(" "*(25-len(MRec[2]))), "\t\t",MRec[3])

            except EOFError:

                pass

            print ("-" * 100)

            Mobj.close()

                                      

             

class Cassettes:

    def __init__(self):

        self.Cast_Code = 0

        self.Tot_Cast = 0           # Total cassette/CD purchased

        self.dd = self.mm = self.yy = 0  # Cassette/CD purchase date

                                       

            # For cassette/CDs entry into the cassettes.dat data file

                                       




    def New_Cassettes(self):

        M = Master()

        B = Balance()

        CDt = Cast_Date()

        self.dd = CDt.dd

        self.mm = CDt.mm

        self.yy = CDt.yy

        TRec = list() #A temporary list to store master record

        

        print("Add New Stock cassette/CD");

        ch = 'Y'

        while ch == 'Y':

            Flag = False   # To check if Cast_Code is in Master.dat or not

            print("\n Date: %s-%s-%s" %  (CDt.dd,CDt.mm, CDt.yy))                                                                   

            while True:

                self.Cast_Code = int(input("\nCassette/CD Code :"))

                   # Function call to check cassette/CD code in Master.dat

                Flag,TRec = M.Check_Code(self.Cast_Code)

                if (Flag == True):

                    self.Cast_Name = TRec[1]       #title of the cassette/CD     

                    self.Cast_Comp = TRec[2]       #cassette/Cd company

                    self.Cast_Price = TRec[3]      #Price per cassette/CD     

                    print("Cassette/CD Name :",self.Cast_Name)

                    print("Company Name : ",self.Cast_Comp )                           

                    print("Individual Cassette/CD price: ",self.Cast_Price)                        

                    while True:

                        self.Tot_Cast = int(input("Enter no of stock cassettes/CDs purchased :"))

                        if (self.Tot_Cast <= 0):

                            print("Enter valid Cassette/Cd number")

                        else:

                            break

                    ch = raw_input("\n Do you want to save the record <Y/N>: ")

                    if ch == 'y' or ch== 'Y':

                        CList = list()

                        with open(File1, 'ab') as Cobj:

                            if not Cobj:

                                print (File1, "is not created")

                            else:

                                  # Appends data into a sequnce object

                                CList.append(self.Cast_Code)

                                CList.append(self.Tot_Cast)   

                                CList.append(self.dd)

                                CList.append(self.mm)                                            

                                CList.append(self.yy)

                                  #write data into the binary files




                                dump(CList, Cobj)   #B.Add_to_File(self.Cast_Code, self.Tot_Cast,self.Cast_Price, self.dd, self.mm, self.yy)

                                B.AddUpdateBalance(CList, self.Cast_Price)

                                print ("Record saved" ) 

                            ch =raw_input("\nStock more cassette/Cd record? <Y/N>: ")

                            ch = ch.upper()

                            if ch =='Y':

                                continue

                            else:

                                break

                                                    

                else:

                        print ("Please enter existing cassette no.")

               # For cassettes/CDs entry into the cassettes.dat data file




    def SetDateFormat(self,d1, m1, y1):

        fDt = ''

        d11 = str(d1)

        m11 = str(m1)

        y11 = str(y1)

        if (len(d11)==1):

            d11 = '0'+d11

        if (len(m11)==1):

            m11 = '0'+m11

        fDt = d11+'-'+m11+'-'+y11

        return fDt




    def Display_Cassettes(self):

        M = Master()

        if not os.path.isfile(File1):

            print (File1, "file does not exist ")

        else:

            Cobj = open(File1, 'rb')

            print ("\nCassette/CD entry Register")

            print ("=" * 125)

            print (" Code", "\tCassettes/CD Name"),(" "*(25-len("Cassette/CD Name"))),( "\tCompany Name"),(" "*(25-len("Company Name"))), "\t\tQuantity","\t\tPrice","\t\tDate"

            print ("-" * 125)

            try:

                while True:

                    CRec = []

                    CRec = load(Cobj)                               

                    TRec = list()

                    Flag, TRec = M.Check_Code(CRec[0])

                    nDt =self.SetDateFormat(CRec[2],CRec[3], CRec[4])                                            

                    if (Flag == True):

                        print (CRec[0],"\t", TRec[1]),(" "*(25-len(TRec[1]))),("\t",TRec[2]),(" "*(25-len(TRec[2]))),( "\t\t  "),(CRec[1]),("\t\t      "), (TRec[3],"\t\t"),(nDt)

            except EOFError:

                pass      

            print ("-" * 125)

            Cobj.close()

              # Function to set the data as: DD-MM-YYYY

   

class Balance:

    def __init__(self):

                  # Instance attributes of Balance.dat data file

        self.Cast_Code = 0           # cassette/Cd code to be balance

        self.Cast_Price = 0          # Total numbert of cassettes/CDs in balance    

        self.Cast_Price = 0          #Unit price of cassettes/CDs on code wise

        self.dd = self.mm = self.yy = 0  # Balance date

    def Give_Balance(self, C_Code):

        Tbalance = 0

        if not os.path.isfile(File2):

                       # When file does not exist

            return False

        else:

            Brec = list()  # A list to extract record from Balance.dat

            Tbalance = 0

            Bobj = open(File2,'rb')

            try:

                while True:

                    BRec = load(Bobj)

                    if (C_Code == BRec[0]):

                        Tbalance = BRec[1]   #E.g. Cast_Bal

                        break

            except EOFError:

                    pass

            Bobj.close()

            return Tbalance

    def AddUpdateBalance(self, CList, CPrice):

                   # To know the balance cassette in 'Balance.daat'

        Cbalance = Balance.Give_Balance(self, CList[0])

        if (Cbalance == False): # If file does not exist , add the record for firsttime

            BRec = list()

            with open(File2, 'ab') as Bobj:

                BRec.append(CList[0]) #Cast_Code

                BRec.append(CList[1]) #Cast_Bal

                BRec.append(CPrice) #Cast_Price

                BRec.append(CList[2]) # Day 

                BRec.append(CList[3]) # Month

                BRec.append(CList[4]) # Year

                dump(BRec, Bobj)







        elif (Cbalance >= 0):

            Bobj = open(File2, 'rb')

            Tobj = open("Temp.dat", 'wb')

            try:

                while True:

                    BRec = list()         # A list to extract record from Balance.dat

                    BRec = load(Bobj)

                    if (CList[0] != BRec[0]):

                                  # Write data into Temp.dat file

                        dump(BRec,Tobj)

                    else:

                        BRec[1] = Cbalance + CList[1]

                                  #self.Cast_Bal = self.Cast_Bal + Cbalance

               

                        dump(BRec, Tobj)

            except EOFError:

                pass

            Tobj.close()

            Bobj.close()

            os.remove("Balance.dat")

            os.rename("Temp.dat", "Balance.dat")




    def UpdateBalance(self, CList):

        Bobj = open(File2, 'rb')

        Tobj = open("Temp.dat", 'wb')

        try:

            while True:

                BRec = load(Bobj)

                if (CList[0] != BRec[0]):

                           # Write data into Temp.dat file

                    dump (BRec, Tobj)

                else:

                    BRec[1] = BRec[1] - CList[4]

                    dump(BRec, Tobj)

        except EOFError:

            pass

        Tobj.close()

        Bobj.close()

        os.remove("Balance.dat")

        os.rename("Temp.dat", "Balance.dat")

        print('Balance.dat updated')

    def Balance_Cassettes(self):

        M = Master()

        if not os.path.isfile(File2):

            print (File2, "file does not exist")

        else:

            TAmount = 0

            print ("\nBalance Stock Register(Cassette/CD) ")

            print ("=" * 128)

            Bobj = open(File2, 'rb')

            print (" Code","\tCassette/CD Name",(" "*(25-len("Cassette/CD Name"))), "\tCompany Name",(" "*(25-len("Company Name"))), "\t\tQuantity","\t\tPrice", "\t\tAmount") 

            print ("-" * 128)

            try:

                while True:

                    BRec = []

                    BRec = load(Bobj)                        

                    TRec = list()

                    Flag, TRec = M.Check_Code(BRec[0])

                    if (Flag == True):

                        Amount = BRec[1] * BRec[2]

                        TAmount = TAmount + Amount

                        print (BRec[0],"\t", TRec[1], (" "*(25-len(TRec[1]))),"\t",TRec[2],(" "*(25-len(TRec[2]))),"\t\t  ",BRec[1],"\t\t\t", BRec[2],"\t\t",Amount )

            except EOFError:

                pass

            print ("-" * 128)

            print ("%s Total Amount: %s %.2f" % (' ' *56,'' * 4 ,TAmount))

            Bobj.close()




class Customer:

    def __init__(self):

                               # Instance attributes of Customer.dat data file                                                    

        self.Cast_Code = 0    # cassette/CD code

        self.C_Name = ''      # Customer name

        self.C_Addresss = ''  # Customer address

        self.C_MPhone = 0     # Customer mobile no.

        self.No_Of_Cast = 0   # Number of Cassette/Cd

        self.dd = self.mm = self.yy = 0 # sale date

    def Cassette_Sale(self):

     

        M =Master()

        B = Balance()

        CDt = Cast_Date()

        self.dd = CDt.dd 

        self.mm = CDt.mm

        self.yy = CDt.yy

        Cbalance = 0

        print("Customer sales cassette/CD")

        ch ='Y'

        while ch=='Y':

            TRec = list() # A temporary list to store master record                                              

            Flag = False  # To check if Cast_Code is in Master.dat or not                                              

            print ("Date: %s-%s-%s" % (CDt.dd, CDt.mm,CDt.yy))    

            while True:

                self.Cast_Code = int(input("\nCassette/CD Code (Enter 6 digit code): "))

                       # Function call to check cassette/Cd code in Master.dat    

                Flag, TRec = M.Check_Code(self.Cast_Code)

                Cbalance = B.Give_Balance(self.Cast_Code)

                if (Flag == True):

                    self.Cast_Name = TRec[1]   #Title of the cassette/CD

                    self.Cast_Comp = TRec[2]   #cassette/CD company  

                    self.Cast_Price = TRec[3]   #Price per cassette/CD company 

                    print ("Cassette/CD Name :", self.Cast_Name)     

                    print ("Company Name :", self.Cast_Comp )     

                    print ("Individual Cassette/CD price : ",self.Cast_Price)    

                    print ("\nEnter Customer details") 

                    self.C_Name = raw_input("Customer name: ").upper()                                               

                    self.C_Address = raw_input("Custoer address: ")                                                

                    self.C_MPhone = raw_input("Customer mobile no: ")                                               

                    while True:

                        self.No_Of_Cast = int(input("\nEnter sales cassettes/CDs nos.: "))                                              

                        if (self.No_Of_Cast > Cbalance):            

                            print ("Out of Stock")

                        else:

                            break




                    ch = raw_input("\nSales confirm <Y/N>: ").upper()                                   

                    if ch == 'Y':

                        CustList = list()

                        with open(File3, 'ab') as CustObj:                                  

                            if not CustObj :

                                print (File3, "is not Created")

                            else:

                                      # Appends data into a sequence object

                                CustList.append(self.Cast_Code)   

                                CustList.append(self.C_Name)

                                CustList.append(self.C_Address)

                                CustList.append(self.C_MPhone)

                                CustList.append(self.No_Of_Cast)

                                CustList.append(self.dd)

                                CustList.append(self.mm)

                                CustList.append(self.yy)      

                                B.UpdateBalance(CustList)

                                dump(CustList, CustObj)

                    ch=raw_input("\nMore sale? <Y/N>:")

                    ch=ch.upper()

                    if ch!='Y':

                        break

            #Function to search individual customer on mobile no.

   
    def MonthlySales_Report(self):

        M=Master()

        if not os.path.isfile(File2):

            print (File3, "file does not exist")

        else:

            monthNo = int(input('\nEnter month number:'))

            yearNo = int(input('\nEnter year:'))                     

            CDt = Cast_Date()

            self.dd = CDt.dd

            self.mm = CDt.mm

            self.yy = CDt.yy

            D=Cassettes()

            if (monthNo <= 12 and monthNo <= self.mm and yearNo <= self.yy):

                MonthName = self.Month_Name(monthNo)

                TAmount = 0

                        #Function called to set the date as DD-MM-YY

                nDt = D.SetDateFormat(self.dd, self.mm, self.yy)

                print ("\nCustomer Sales Status Report - Date:", nDt)

                print ("For the month of", MonthName, yearNo)

                print ("-" * 160)

                CustObj = open(File3, 'rb')

                print ("Name","\t\t", "Mobile No.","\t\t" ,"Cassette/CD Cide and Name","\t\t", "Date","\t\t", "Qty", "\t\t", "Unit price", "\t\t","Amount")

                print ("-"*160)

                try:

                    while True:
                        CustRec = []

                        CustRec = load(CustObj)

                        TRec = list()

                        Flag, TRec = M.Check_Code(CustRec[0])

                        UPrice = TRec[3]

                        Amount = (UPrice + (UPrice * 0.20)) * CustRec[4] #An additional 20% of Unit Price

                        nDt = D.SetDateFormat(CustRec[5], CustRec[6], CustRec[7])

                        TAmount+=Amount

                        if (monthNo == CustRec[6] and yearNo == CustRec[7]):

                            Clength = str(CustRec[0])+'-'+TRec[1]

                            nName = ''

                            for i in range(len(Clength)):   #Extracts only 24 characters

                                nName = nName + Clength[i]

                                if i == 23:

                                    break

                            print (CustRec[1],"\t   ", CustRec[3],"\t\t        ", nName,"\t\t\t",nDt, "\t",CustRec[4], "\t\t",UPrice,"\t\t       ", Amount)

                except EOFError:

                    pass

                    print ("-" * 160)

                    print('Note. Amount is calculated as 20% extra on unit price.')

                    print ("%s Total Sales Amount: %s %.2f" % (' ' * 50, ' ' * 4, TAmount))

                    CustObj.close()

            else:
                print ("Month number and year is not valid")

                    #Function to display close wise monthly sales report.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      

                                         

    def CodeWiseMonthlySales_Report(self):

        M=Master()

        D=Cassettes()

        TRec = list() #A temporary list to store master record                         

        Flag = False  #To check if Cast_Code is in Master.dat or not

        if not os.path.isfile(File2):

            print (File3, "file does not exist")

        else:

            CCode = int(input("\nCassette/CD Code:"))

            monthNo = int(input('\nEnter month number:'))                     

            yearNo = int(input('\nEnter year:'))

            CDt = Cast_Date()

            self.dd = CDt.dd

            self.mm = CDt.mm

            self.yy = CDt.yy                    

                    #Function to call to check cassette/CD code in Master.dat

            Flag, TRec = M.Check_Code(CCode)

            if (monthNo <= 12 and  monthNo <= self.mm and yearNo <= self.yy and Flag == True):

                CName = TRec[1]  #Tittle of the casette/CD

                CComp = TRec[2]  #casette/CD company

                CPrice = TRec[3] #Price per cassette/CD              

                        #Function Call for a character month

                MonthName = self.Month_Name (monthNo)               

                TAmount = 0

                        #Function Called to set date as DD-MM-YY

                nDt = D.SetDateFormat(self.dd, self.mm, self.yy)

                print ("\nCode wise Sales Report - Date:", nDt)

                print ("For the month of", MonthName, yearNo)

                print ("Cassette/CD Code:  %d  Name: %s" % (CCode, CName) )            

                

                print ("-" * 120)

                CustObj = open(File3, 'rb')                

                print ("Name","\t\t", "Mobile No.","\t\t" , "Date","\t\t", "Qty", "\t\t","\t\t", "Unit price", "\t\t","Amount")

                print ("-" * 120)

                ctr = 0

                try:

                    while True:

                        CustRec = []

                        CustRec = load(CustObj)

                        TRec = list()

                        Flag, TRec = M.Check_Code(CustRec[0])

                        UPrice = TRec[3]

                        Amount = (UPrice + (UPrice * 0.20)) * CustRec[4] #An additional 20% of Unit Price

                        nDt = D.SetDateFormat(CustRec[5], CustRec[6], CustRec[7])

                        TAmount+=Amount

                        if (monthNo == CustRec[6] and yearNo == CustRec[7]) and (CCode == CustRec[0]):

                            ctr += 1  

                            print (CustRec[1],"\t\t\t", CustRec[3],"\t\t\t", nDt, CustRec[4],"\t\t\t", UPrice,"\t\t\t", Amount)

                except EOFError:

                    pass

                print ("-" * 120)

                if (ctr == 0):

                    print ('No record found on such Code No. , Month and Year')

                else:

                    print ('Note. Amount is calculated as 20% extra on unit price.')

                    print ("%s Total Sales Amount: %s %.2f" % (' ' * 50, ' ' * 4, TAmount))

                CustObj.close()

            else:

                print ("Either Code not found or Month no. and year is not valid")

                 #Function to search individual customer on mobile no.




    


    def Month_Name(self,mNo):

        self.mDict = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}

        self.nName = ''                                   

        for key, value in self.mDict.items():

            if (key == mNo):

                self.nName = value

                break 

        return self.nName




while True:

    

    M=Master()

    CS=Cassettes()

    BL=Balance()

    Cust=Customer()

    print ("\n Video Library Main Menu")

    print ("-" * 50)

    print ("       1 - >  Master Cassettes/CDs" )      

    print ("       2 - >  Stock Cassettes/CDs")

    print ("       3 - >  Customer Sales")

    print ("       4 - >  Exit")

    print ("-" * 50)

    opt = input("Enter your choice(1,2,3 or 4):")                                    

    if opt=="1":
        ch=0

        while True:

            print ("\n\tMaster Cassettes Menu" )                              

            print ("-" * 50)

            print ("       1 - >  Cassettes/CDs Stock Entry")

            print ("       2 - >  View Cassettes/CDs")

            print ("       3 - >  Back to Main Menu")

            print ("-" * 50)

            ch = input("Enter your choice:")                            

            if ch=="1":

                M.Master_Entry()

            elif ch=="2":

                M.Master_Display()

            elif ch=="3":

                break

    elif opt=="2":
        ch=0

        while True:

            print

            print ("\n\tStock Cassettes Menu")                               

            print ("-" * 50)

            print ("       1 - >  Cassettes/CDs Stock Entry")

            print ("       2 - >  Display Cassettes/CDs")

            print ("       3 - >  Stock/Balance Cassettes")

            print ("       4 - >  Back to Main Menu")

            print ("-" * 50)

            ch = input("Enter your choice:")                            

            if ch=="1":

                CS.New_Cassettes()

            elif ch=="2":

                CS.Display_Cassettes()                       

            elif ch=="3":                           

                BL.Balance_Cassettes()

            elif ch=="4":

                break

    elif opt=="3":                             

        ch=0

        while True:

            print

            print ("\n\tCustomer Sales Menu")                             

            print ("-" * 50)

            print ("       1 - >  Sales Entry")

            print ("       2 - >  Monthly Sales Report")

            print ("       3 - >  Code Wise Monthly Sales") 

            print ("       4 - >  Back to Main Menu")                           

            print ("-" * 50)

            ch = int(raw_input("Enter your choice:"))                            

            if ch=="1":

                Cust.Cassette_Sale() 

            elif ch=="2":

                Cust.MonthlySales_Report()

            elif ch=="3":

                Cust.CodeWiseMonthlySales_Report()                      

            elif ch=="4":
                break

               

            

    elif opt=="4":

        print ("Thank you and have a nice day")

        break

    else:

        print ("Please enter correct option!")     

