
#one's and two's complement
# 4th (a and b)

# Get the binary string
inp_str = input("Enter the binary number: ")

# Convert the string to a list of characters for the 1s complement
ones_list = []
for i in inp_str:
    if i == "0":
        ones_list.append("1")
    elif i == "1":
        ones_list.append("0")
    else:
        print(f"The string {inp_str} is not a valid binary number")
        exit(1)

ones_str = "".join(ones_list)
print(f"1s complement = {ones_str}")

# Now we have to add one to this list
# We reverse the list so the for loop goes through the bits from
# least significant bit to most significant bit.
temp_str = reversed(ones_list)
twos_list = []
carry = 1
for c in temp_str:
    if carry == 0:
        twos_list.append(c)
    elif c == "0":
        twos_list.append("1")
        carry = 0
    else:
        twos_list.append("0")
        carry = 1

# If the last bit caused a carry append "1"
if carry == 1:
    twos_list.append("1")

# And finally reverse the list again
twos_list = reversed(twos_list)
twos_str = "".join(twos_list)
print(f"2s complement = {twos_str}")