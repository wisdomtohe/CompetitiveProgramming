
# Python program to check 
# if a string is binary or not 
  
# function for checking the 
# string is accepted or not 
def check(string) : 
  
    # set function convert string 
    # into set of characters . 
    p = set(string) 
  
    # declare set of '0', '1' . 
    s = {'0', '1'} 
  
    # check set p is same as set s 
    # or set p contains only '0' 
    # or set p contains only '1' 
    # or not, if any one conditon 
    # is true then string is accepted 
    # otherwise not . 
    if s == p or p == {'0'} or p == {'1'}: 
        print("Yes") 
    else : 
        print("No") 
  

def check2(string) : 
  
    # initialize the variable t 
    # with '01' string 
    t = '01'
  
    # initialize the variable count 
    # with 0 value 
    count = 0
  
    # looping through each character 
    # of the string . 
    for char in string : 
  
        # check the character is present in 
        # string t or not. 
        # if this condition is true 
        # assign 1 to the count variable 
        # and break out of the for loop 
        # otherwise pass 
        if char not in t : 
            count = 1
            break
        else : 
            pass
          
    # after coming out of the loop 
    # check value of count is non-zero or not 
    # if the value is non-zero the en condition is true 
    # and string is not accepted 
    # otherwise string is accepted 
    if count : 
        print("No") 
    else : 
        print("Yes") 
  
          
# driver code 
if __name__ == "__main__" : 
  
    string = "101010000111"
  
    # function calling 
    check(string) 
