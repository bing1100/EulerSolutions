#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

#What is the sum of the digits of the number 2^1000?

# Play around with strings and lists and we can easily get the answer
def find(exp):
    sum=0
    str_num=str(2**exp)
    s_num_list=list(str_num)
    for digit in s_num_list:
        sum+=int(digit)
    return sum