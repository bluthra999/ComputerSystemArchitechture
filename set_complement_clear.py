# 8 , 9 , 10
num_1 = input("Enter the binary number on  which you want to apply selective operation: ")
num_2 = input("Enter the second binary number: ")

# checks the input is binary or not 
try:
    num1_int=int(num_1,base=2)
    num2_int=int(num_2,base=2)
except:
    print("Invalid binary numbers")
    exit(1)

num1_list = list(num_1.strip(" "))
num1_len=len(num1_list)
num2_list = list(num_2.strip(" "))
num2_len=len(num2_list)
diff=abs(num1_len-num2_len)
if num1_len >= num2_len:
    for i in range(0,diff):
        num2_list.insert(0,"0")

else:
    for i in range(0,diff):
        num1_list.insert(0,"0")

#print(num1_list)
#print(num2_list)
num1_len=len(num1_list)

# selective

selective_lst=[]

for i in range(0,num1_len):
    if num1_list[i]=="0" and num2_list[i]=="0":
        selective_lst.append("0")
    else:
        selective_lst.append("1")

or_str="".join(selective_lst)
print(f"selective Set {or_str}")


# 

and_not=[]

for i in range(0,num1_len):
    if num1_list[i]=="1" and num2_list[i]=="0":
        and_not.append("1")
    else:
        and_not.append("0")

and_str="".join(and_not)
print(f"A and (not B) : {and_str}")


# complement 

complement_lst=[]

for i in range(0,num1_len):
    if num1_list[i] == num2_list[i]:
        complement_lst.append("0")
    else:
        complement_lst.append("1")

exor_str="".join(complement_lst)
print(f"Cmplement Set: {exor_str}")