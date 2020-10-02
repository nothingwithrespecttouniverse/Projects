from pickle import dump,load
from random import choice

def spaces(S):                  # no more than 1 space in bundle
    L=S.split()
    S1=""
    for x in L:
        S1+=x+" "
    return (S1.capitalize())[0:-1]
def admission_no():
    f=open("ADMISSION_NUMBER.dat","rb")
    I=load(f)
    ma=max(I)
    f.close()
    f=open("ADMISSION_NUMBER.dat","wb")
    dump(I+[ma+1],f)
    f.close()
    return ma+1
def collecting_data(file):
    f=open(file,"rb")
    data=load(f)
    f.close()
    return data
def exchanging_data(file,data):
    f=open(file,"wb")
    dump(data,f)
    f.close()
#ATDB=Add To Data Binery
def ATDB(file,data):
    info=collecting_data(file)
    info.append(data)
    exchanging_data(file,info)
def section(cla,stram=0):
    print(cla)
    if(cla==1):
        cl="1st"
    if(cla==2):
        cl="2nd"
    if(cla==3):
        cl="3rd"
    if(cla>=4 and cla<=13):
        cl=str(cla)+"th"
    
    a=collecting_data("COUNT_SECTION.dat")[cl]["a"]
    b=collecting_data("COUNT_SECTION.dat")[cl]["b"]
    c=collecting_data("COUNT_SECTION.dat")[cl]["c"]
    if([a,b,c].count(0)==3):
        sec=choice(("a","b","c"))
    else:
        sec=choice((["a"]*(b+c))+(["b"]*(c+a))+(["c"]*(a+b)))
    d=collecting_data("COUNT_SECTION.dat")
    d[cl][sec]+=1
    exchanging_data("COUNT_SECTION.dat",d)
    return sec
def count_check():
    for x in collecting_data("COUNT_SECTION.dat"):
        print(x,"\t\t",collecting_data("COUNT_SECTION.dat")[x])
