import texttable  #Importing package required to display timetable.

#     Vishnu A    21BCE2154
#     IEEE-VIT CC Task

courses={   #DATABASE
'BCSE101E':['Computer programming :python',['mo07','mo08','fr10','fr11','we06'],3],
'BDSA101E':['Computer programming :DSA',['tu07','tu08','fr06','fr07','we09'],3],
'BENG101E':['Technical english',['tu10','tu11','fr09','we08','we07'],3],
'BSTS101E':['Soft skills',['th06','th07','fr08','th10','th11'],3],
'BCCS101E':['Computer programming :C',['th09','th08','we11','we10','fr05'],3],
'BCPS101E':['Computer programming :C++',['fr04','mo09','we03','mo10','tu04'],3],
'BCSE102E':['Computer programming :python',['tu07','tu08','fr10','fr11','we06'],3],
'BDSA102E':['Computer programming :DSA',['mo07','mo08','fr06','fr07','we09'],3],
'BENG102E':['Technical english',['tu10','tu11','fr08','th10','th11'],3],
'BSTS102E':['Soft skills',['th06','th07','fr09','we08','we07'],3],
'BCCS102E':['Computer programming :C',['th09','th08','we11','we10','tu04'],3],
'BCPS102E':['Computer programming :C++',['fr04','mo09','we03','mo10','fr05'],3],

'BECE101L':['Basic electronics engineering :Lecture',['tu09','mo02','th02'],2],
'BPHY101L':['Basic engineering physics :Lecture',['tu06','mo011','we01'],2],
'BEEE101L':['Basic electrical engineering: Lecture',['tu01','mo03','we02'],2],
'BCHY101L':['Basic engineering chemistry :Lecture',['tu05','mo01','th05'],2],
'BECE102L':['Basic electronics engineering :Lecture',['tu09','mo01','we01'],2],
'BPHY102L':['Basic engineering physics :Lecture',['tu01','mo02','th02'],2],
'BEEE102L':['Basic electrical engineering: Lecture',['tu05','fr01','we02'],2],
'BCHY102L':['Basic engineering chemistry :Lecture',['tu06','mo11','th05'],2],

'BECE101P':['Basic electronics engineering :Practical',['mo06','mo05','fr03','th09'],1],
'BEEE101P':['Basic electrical engineering :Practical',['tu11','th03','we05','mo09'],1],
'BPHY101P':['Basic engineering physics :Practical',['tu02','fr02','we05','th01'],1],
'BCHY101P':['Basic engineering chemistry :Practical',['mo04','fr01','we04','th04'],1],
'BECE102P':['Basic electronics engineering :Practical',['tu03','th03','mo03','th04'],1],
'BEEE102P':['Basic electrical engineering :Practical',['tu02','fr02','we05','mo09'],1],
'BPHY102P':['Basic engineering physics :Practical',['mo06','mo05','mo04','fr03'],1],
'BCHY102P':['Basic engineering chemistry :Practical',['we05','th09','we04','th04'],1],
}

c_name={k:0 for k in list(courses.keys())}  #Initializing the available course list as a dictionary
for i in courses.keys():
    l=courses[i][1]
    o=11
    for j in l:
        if int(j[2:])<o:
            o=int(j[2:])
    c_name[i]=o                 #Assigning a weightage to each course
csrt = sorted(c_name.items(), key=lambda x: x[1],reverse=True) #Sorting Course list according to weightage and credits
c_name=[""]*len(courses)
j=0
for i in csrt:
    c_name[j]=i[0]  #Conversion of dict to list
    j+=1

reg=[""]*len(courses)
reg_slot=[]

#Data template for table printing
mon=["Monday", "MO01", "MO02","MO03","MO04","MO05","MO06","MO07","MO08","MO09","MO10","MO11"]
tue=["Tuesday", "TU01", "TU02","TU03","TU04","TU05","TU06","TU7","TU08","TU09","TU10","TU11"]
wed=["Wednesday","WE01", "WE02","WE03","WE04","WE05","WE06","WE07","WE08","WE09","WE10","WE11"]
thu=["Thursday","TH01", "TH02","TH03","TH04","TH05","TH06","TH07","TH08","TH09","TH10","TH11"]
fri=["Friday","FR01", "FR02","FR03","FR04","FR05","FR06","FR07","FR08","FR09","FR10","FR11"]



def week_update(sl,str): #Function to update timtable slots
    global mon 
    global tue
    global wed
    global thu
    global fri
    ll=int(sl[2:])
    str="\n"+str
    if sl[:2]=="mo":
        mon[ll]+=str      
    elif sl[:2]=="tu":
        tue[ll]+=str       
    elif sl[:2]=="we":
        wed[ll]+=str   
    elif sl[:2]=="th":
        thu[ll]+=str   
    elif sl[:2]=="fr":
        fri[ll]+=str
        
def display():  #Function to display resulting timetable
    tableObj = texttable.Texttable()

    tableObj.set_cols_align(["l", "c", "c","c", "c", "c","c", "c", "c","c", "c", "c"])
    tableObj.set_cols_width(["10", "10", "10","10", "10", "10","10", "10", "10","10", "10", "10",])
    tableObj.add_rows([
        ["DAY", "8-8:50", "9-9:50","10-10:50","11-11:50","12-12:50","14-14:50",
        "15-15:50","16-16:50","17-17:50","18-18:50","19-19:50"],
        mon,tue,wed,thu,fri])
    print(tableObj.draw())

e=0
def wake_late(crc,f):  #Optimisation function working till credit input
    global reg
    global reg_slot
    global cr
    global e

    if (crc+courses[c_name[f]][2])<cr and not((cr-crc)<=3):
        if clash(c_name[f]):
            reg[e]=c_name[f]
            reg_slot=reg_slot+courses[c_name[f]][1]
            e+=1
            crc+=courses[c_name[f]][2]
        f+=1
        wake_late(crc,f)
    elif cr-crc==3:  #End conditions
        for i in c_name:
            if i not in reg and courses[i][2]==3 and clash(i): 
                reg[e]=i
                reg_slot=reg_slot+courses[i][1]
                crc=cr
    elif cr-crc==2:
        for i in c_name:
            if i not in reg and courses[i][2]==2 and clash(i): 
                reg[e]=i
                reg_slot=reg_slot+courses[i][1]
                crc=cr
    elif cr-crc==1:
        for i in c_name:
            if i not in reg and courses[i][2]==1 and clash(i): 
                reg[e]=i
                reg_slot=reg_slot+courses[i][1]
                crc=cr

def clash(stc):  #Function to check for slot clashes
    for i in courses[stc][1]:
        if i in reg_slot:
            return False
    return True


print()
print("\t\t--FFCS TIMETABLE OPTIMIZER--\n")
cr=int(input("Kindly enter your required amount of credits for this semester.            (Maximum credit limit:27)\n"))
print("\n")
if cr<=27:  #Credit limit checking
    wake_late(0,0)
    reg = list(filter(("").__ne__, reg)) #Sorting of registered courses
    for i in reg:
        for j in courses[i][1]:
            week_update(j,i)  #Updating slots
    print()
    print("Your otpimized timetable:\n")
    print("\t\t\t\t\t\t\t\t\tTIMETABLE")
    display()
    print()
    print("Your registered courses:\n")
    print("\t   COURSE LIST")  #Displaying registered course list
    for i in reg:
        print(i,"      :        ",courses[i][0])
    print("\n")

else:
    print("Invalid input: Maximum credit limit exceeded.")  #Error message