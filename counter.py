#  5
# counter
def int_binary(num):
    list=[]
    while num>0:
        c=num%2
        d=str(c)
        list.append(d)
        num=num//2
    if(len(list) != 0):
        diff=abs(len(list)-5)
        for i in range(0,diff):
            list.append("0")
        list=reversed(list)
        num1 = "".join(list)
        print(num1)
    
        

num_1 = input("Enter the binary number: ")
# checks the input is binary or not 
try:
    num1_int=int(num_1,base=2)
except:
    print("Invalid binary number")
    exit(1)

num1_list = list(num_1.strip(" "))
num1_len=len(num1_list)
diff=abs(len(num1_list)-5)
if num1_len > 5 :
    #converts binary of bit > 5 to bit 5
    num1_list=num1_list[diff::]
else:
    # converts binary of bit < 5 to bit 5
    for i in range(0,diff):
        num1_list.insert(0,"0")

num_1 = "".join(num1_list)
num1_int=int(num_1,base=2)
num_temp=num1_int

updown=input("Enter 1 for down and 2 for up: ")

if (updown=="1"):
# down counter

    for i in range(num_temp,0,-1):
        int_binary(i)
    print("00000")   
# up counter
elif (updown=="2"):
    for i in range(num_temp,31):
        int_binary(i)

