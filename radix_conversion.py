#radix
inp_str = input("Enter the number: ")
inp_radix = input("Enter the input radix: ")
out_radix =input("Enter the output radix: ")
check_str=True

for i in inp_str:
    if i<inp_radix:
       check_str=True
        
    else:
        check_str=False
        print("invalid input")
        exit(1)

radix_inp_int=int(inp_radix)
radix_out_int=int(out_radix)
converted_int=int(inp_str,base=radix_inp_int)
print("In base 10 , entered",inp_str,"is ",converted_int)
converted_str=str(converted_int)
list=[]
while  converted_int>0:
    c=converted_int%radix_out_int
    d=str(c)
    list.append(d)
    converted_int=converted_int//radix_out_int

final_list=reversed(list)
final_str = "".join(final_list)
print("In base",radix_out_int,",",inp_str,"is written as",final_str)
