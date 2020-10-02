
"-----------------------------------------------------------------------------------------------------ROUGH WORK------------------------------------------------------------------------------------------------------------------------------------"
"""

+------------+----------------------------------+------------------------------------------------------------------------------------------+-----------------------+-----------------------+
 |Admn0 |Student name            |Name of the book                                                            |Date  of issue|Date of return|
+------------+-----------------------------------+------------------------------------------------------------------------------------------+-----------------------+-----------------------+
 |1111    |AAAAAAAAAAAAAAA|AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA|2018/02/34      |2019/02/34     |
+----------- +----------------------------------+------------------------------------------------------------------------------------------+-----------------------+-----------------------+
 |             |                                    |                                                                                            |                        |                        |
+----------- +----------------------------------+------------------------------------------------------------------------------------------+-----------------------+-----------------------+


remove multiple times



"""
"---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"

  

from funtion import *


"---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
import datetime 
"-----------------------------------------------------------------------------------------------------EMPTY INFORMATION--------------------------------------------------------------------------------------------------------------------"
admn=[]
name=[]
bookname=[]
doi=[]
dor=[]
"---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"



ch=1
while(ch!="0"):
    print("|"*333)
    print("MENU")
    print("1. show list of books ")                                                                                                    #completed
    print("2. issue a book ")                                                                                                             #completed
    print("3. return a book")                                                                                                             #completed
    print("4. information of students those who don't rerurn the book")
    print("5.information of all the student")
    print("0.exit ")                                                                                                                             #completed
    ch=input("enter your choice :  ")
    if(ch=="1"):
        
        print("***************************************************")
        print("catagories of books")
        print("1. Epic ")
        print("2.novels")
        print("3.Best selling books of sceince ")
        print("4.CBSE sceince books ")
        print("5.Encyclopedias")
        print("6.story books ")
        print("0.exit ")
        print("***************************************************")
        ch1=input("enter your choice : ")
        if(ch1=="1"):
            #collecting_data("LFAMOUSR.dat")
            for x in range (len(collecting_data("FAMOUSR.dat"))):
                print(x+1,".",collecting_data("FAMOUSR.dat")[x])
        elif(ch1=="2"):
            for x in range(len(collecting_data("NOVEL.dat"))):
                print(x+1,".",collecting_data("NOVEL.dat")[x])
        elif(ch1=="3"):
            for x in range (len(collecting_data("FSCIENCE.dat"))):
                print(x+1,".",collecting_data("FSCIENCE.dat")[x])
        elif(ch1=="4"):
            for x in range (len(collecting_data("SCIENCE.dat"))):
                print(x+1,".",collecting_data("SCIENCE.dat")[x])
        elif(ch1=="5"):
            for x in range (len(collecting_data("ENCYCLOPEDIA.dat"))):
                print(x+1,".",collecting_data("ENCYCLOPEDIA.dat")[x])
        elif(ch1=="6"):
            for x in range (len(collecting_data("STORYBOOKS.dat"))):
                print(x+1,".",collecting_data("STORYBOOKS.dat")[x])
        elif(ch1=="0"):
            print("ok")
        else:
            print ("anpadh hai kya ")
            '--------------------------------------------------------------------------------------------------issue a book--------------------------------------------------------------------------------------'
    elif(ch=="2"):
        admn1=input("enter the admission number : ")
        if(admn1.isdigit()):
            if(admn1 not in collecting_data("admn.dat")):
                name1=spaces(input("enter your  name : "))
                namebook1=spaces(input("enter the name of book you want to issue : "))
                if(namebook1 in collecting_data("TB.dat")):
                    print(name1,"book is available ")
                    #####
                    
                    x=str(datetime.datetime.now())
                    exchanging_data("name.dat",collecting_data("name.dat")+[name1])
                    exchanging_data("admn.dat",collecting_data("admn.dat")+[admn1])
                    exchanging_data("doi.dat",collecting_data("doi.dat")+[x])
                    exchanging_data("dor.dat",collecting_data("dor.dat")+["does not return the book"])
                    exchanging_data("bookname.dat",collecting_data("bookname.dat")+[namebook1])
                    d=collecting_data("TB.dat")
                    d.remove(namebook1)
                    exchanging_data("TB.dat",d)
                    del d
                    for create in ["FAMOUSR.dat","NOVEL.dat","SCIENCE.dat","FSCIENCE.dat","ENCYCLOPEDIA.dat","STORYBOOKS.dat"]:
                        if(namebook1 in collecting_data(create)):
                            d=collecting_data(create)
                            d.remove(namebook1)
                            exchanging_data(create,d)
                            del d
                else:
                    print(name1,"not available")
            else:
                for x in range(len(collecting_data("admn.dat"))):
                    if(collecting_data("admn.dat")[x]==admn1):
                        break
                name1=collecting_data("name.dat")[x]
                namebook1=spaces(input("enter the name of book you want to issue : "))
                if(namebook1 in collecting_data("TB.dat")):
                    print(name1,"book is available")
                    
                    x=str(datetime.datetime.now())
                    exchanging_data("name.dat",collecting_data("name.dat")+[name1])
                    exchanging_data("admn.dat",collecting_data("admn.dat")+[admn1])
                    exchanging_data("doi.dat",collecting_data("doi.dat")+[x])
                    exchanging_data("dor.dat",collecting_data("dor.dat")+["does not return the book"])
                    exchanging_data("bookname.dat",collecting_data("bookname.dat")+[namebook1])
                    d=collecting_data("TB.dat")
                    d.remove(namebook1)
                    exchanging_data("TB.dat",d)
                    del d
                    for create in ["FAMOUSR.dat","NOVEL.dat","SCIENCE.dat","FSCIENCE.dat","ENCYCLOPEDIA.dat","STORYBOOKS.dat"]:
                        if(namebook1 in collecting_data(create)):
                            d=collecting_data(create)
                            d.remove(namebook1)
                            exchanging_data(create,d)
                            del d
                    
                else:
                    print(name1,"not available")
        else:
            print("admission number must be in 4 digits")
    elif(ch=="3"):
        admn1=input("enter the admission number")
        bookname1=spaces(input("enter the name of book"))
        if(bookname1 not in collecting_data("TB.dat") and bookname1 in collecting_data("LTB.dat") ):
            for x in range(len(collecting_data("bookname.dat"))):
                if(collecting_data("dor.dat")[x]=="does not return the book" and collecting_data("bookname.dat")[x]==bookname1):
                    break
            if(collecting_data("admn.dat")[x]==admn1):
                print("Ok")
                #bookname.append(bookname1)
                exchanging_data("TB.dat",collecting_data("TB.dat")+[bookname1])
                y=datetime.datetime.now()
                d=collecting_data("dor.dat");d[x]=y
                exchanging_data("dor.dat",d)
                for ABCD in ["FAMOUSR.dat","NOVEL.dat","SCIENCE.dat","FSCIENCE.dat","ENCYCLOPEDIA.dat","STORYBOOKS.dat"]:
                    if(bookname1 in collecting_data("L"+ABCD)):
                        exchanging_data(ABCD,collecting_data(ABCD)+[bookname1])
            else:
                print("you are not ower of the book and can not able to return the book")
        else:
            print("you can't aply to return the book")
    elif(ch=="4"):
        no=[]
        for x in range(len(collecting_data("name.dat"))):
            if(collecting_data("dor.dat")[x]=="does not return the book"):
                no.append(x)
        print("Those who don't return the book ")
        for x in no:
            print("--------------------------------------------")
            print("Admission number : ",collecting_data("admn.dat")[x])
            print("Name of student : ",collecting_data("name.dat")[x])
            print("Book name : ",collecting_data("bookname.dat")[x])
            print("Date of book ",collecting_data("doi.dat")[x])
        print("--------------------------------------------")
    elif(ch=="2603"):
        #FAMOUSR,NOVEL,SCIENCE,FSCIENCE,ENCYCLOPEDIA,STORYBOOKS,TB
        exchanging_data("FAMOUSR.dat",collecting_data("LFAMOUSR.dat"))
        exchanging_data("NOVEL.dat",collecting_data("LNOVEL.dat"))
        exchanging_data("SCIENCE.dat",collecting_data("SCIENCE.dat"))
        exchanging_data("FSCIENCE.dat",collecting_data("LFSCIENCE.dat"))
        exchanging_data("ENCYCLOPEDIA.dat",collecting_data("LENCYCLOPEDIA.dat"))
        exchanging_data("STORYBOOKS.dat",collecting_data("LSTORYBOOKS.dat"))
        exchanging_data("TB.dat",collecting_data("LTB.dat"))
        
        exchanging_data("name.dat",[])
        exchanging_data("doi.dat",[])
        exchanging_data("dor.dat",[])
        exchanging_data("admn.dat",[])
        exchanging_data("bookname.dat",[])
    elif(ch=="5"):
        for x in range(len(collecting_data("admn.dat"))):
            print("--------------------------------------------")
            print("Admission number : ",collecting_data("admn.dat")[x])
            print("Name of student : ",collecting_data("name.dat")[x])
            print("Book name : ",collecting_data("bookname.dat")[x])
            print("Date of book ",collecting_data("doi.dat")[x])
            if(collecting_data("dor.dat")[x]=="does not return the book"):
                print("Book status  ","Not Returned")
            else:
                print("Book status  ","Returned on ",collecting_data("dor.dat")[x])
        print("--------------------------------------------")
