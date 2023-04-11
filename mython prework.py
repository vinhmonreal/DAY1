#Question 1
def hello_name(user_name):    
    print("hello_" + user_name)

#Question 2
def first_odds():
    x = 1
    while x < 100:
        print(x)
        x+=2        

#Question 3
def max_num_in_list(a_list):
    a_list.sort()
    print(a_list[-1])
    
#Question 4
def is_leap_year(a_year):
    if a_year % 4 == 0:
        return True
    elif a_year % 100 == 0 and a_year % 400 == 0:
        return True
    else:
        return False

#Question 5
def is_consecutive(a_list):
    x = 0 
    for number in a_list:
        x += 1
        if x == len(a_list):
            return True
        if number + 1 != a_list[x]:
            return False
        