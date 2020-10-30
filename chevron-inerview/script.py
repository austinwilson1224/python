# function takes positive base-10 integer and returns number of 1s in binary representation




def number_of_1s(number):
    if number > 1:
        return number_of_1s(number // 2)

    return number // 2

number_of_1s(8)



def convert_to_binary(num):


    result = "" 
    # convert number into a binary number 
    # number % 2 


    # count the number of 1s in the binary number 

    result = "111100"
    count = 0

    for digit in range(len(result)):
        #print(digit)
        # print
        if (result[digit] == "1"): 
            count += 1
    return count

print(number_of_1s(1))

#  0
#  1
#  2 = 10 
#  3 = 11
#  4 = 100