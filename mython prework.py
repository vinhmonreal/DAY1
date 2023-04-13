#Question 1
import abc


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
        

def find_outlier(l):
    even = 0
    odd = 0
    even_list = []
    odd_list = []
    for num in l:
        if num % 2 == 0:
            even += 1
            even_list.append(num)
        else:
            odd += 1
            odd_list.append(num)
    if even > odd:
        for num in odd_list:
            return (num)
    else:
        for num in even_list:
            return (num)

def sum_two_smallest_numbers(l):
    list = []
    list.append(min(l))   
    l.remove(min(l))
    list.append(min(l))
    total = sum(list)
    return total




def is_triangle(a, b, c):
    if a == 0 or b== 0 or c== 0:
        return False
    import math 
    cosA = (b**2 + c**2 - a**2) / (2 * b * c)
    cosB = (a**2 + c**2 - b**2) / (2 * a * c)
    cosC = (a**2 + b**2 - c**2) / (2 * a * b)
    if cosA >= -1 and cosB >= -1 and cosC >= -1 and cosA <= 1 and cosB <= 1 and cosC <= 1 and a + b != c and a + c!= b and b + c!= a and math.acos(cosA) + math.acos(cosB) + math.acos(cosC) >= 3.1415926535897 and math.acos(cosA) + math.acos(cosB) + math.acos(cosC) <= 3.1415926535897999:
        return True
    else:
        return False
    
  
def digital_root(n):
    string = str(n)
    if len(string) == 1:
        return n
    else:
        list =[]
        for i in string:
            list.append(int(i))
        return digital_root(sum(list))

def is_pangram(s):
    string = s.lower()
    list =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in string:
        if i in list:
            list.remove(i)
    if len(list) == 0:
        return True
    else:
        return False

def persistence(n):
    string = str(n)
    list = []
    count = 0

    for item in string:
        list.append(item)
    print(list)
    while len(list) > 1:
        total = 1
        for item in list:
            total = total * int(item)
        count += 1
        string = str(total)
        list = []
        print(string)
            
        print(list)
        for item in string:
            
            list.append(item)
        print(list)
    len(list)
    print(count)
    return count
 
 


def info():
    data = dict()
    while True:
        respond = input("What do you want to do? ")
        if respond == "quit":
            print(data)
            break
        name = input("What is your name? ")
        address = input("What is your address? ")
        age = int(input("What is your age? "))
        sex = input("What is your sex? ")
        data[name] = {
            'address' : address,
            'age' : age,
            'sex' : sex
            }        

        
def shoping_cart():
    data = {
        'apple' : '$ .50',
        'banana' :'$ .40',
        'mandarin' :'$ .30',
        'mango' :'$ .80',
        'avocado' :'$ .70',
        'jackfruit' :'$ 10',
    }
    list = []
    dict = {}
    while True:
        respond = input("Do you want to add / remove / view / checkout / quit? ")
        if respond.lower() == "quit":
            print('Goodbye')
            break
        elif respond.lower() == "view":
            if len(dict) > 0:
                print(dict)
            else:
                print("No items in the cart")
        elif respond.lower() == "add":
            print('Our Available Items')
            print(data)
            product = input("What do you want to add?")
            if product in data:
                if product not in dict.keys():
                    quantity = int(input("How many do you want to add? "))
                    total = caculator(product, quantity)
                    dict[product] = {'quantity' : quantity, 'price' : total}
                else:
                    quantity = int(input("How many do you want to add? "))
                    total = caculator(product, quantity)
                    dict[product] = {'quantity' : int(dict[product]['quantity']) + quantity, 'price' : int(dict[product]['price']) + total}
            else:
                print("That item is not available")    
        elif respond.lower() == "remove":
            if len(dict) > 0:
                print(dict)
                remove_item = input("What do you want to remove from your list?")
                if remove_item in dict:
                    del dict[remove_item.lower()]
                    print("Removed Successfully")
                else:
                    print("Invalid Item")
            else:
                print("No items in the cart")
        elif respond.lower() == "checkout":
            if len(dict) == 0:
                print("Your cart is empty")
            else:
                print(dict)
                total_purchase = 0
                for value in dict.values():
                    total_purchase += value['price']
                print(f" Your total is {total_purchase} dollars.")
                confirm = input("Yes or No? ")
                if confirm.lower() == "yes":
                    print('Thank you for shopping with us!')
                    return total_purchase
                elif confirm.lower() == "no":
                    print('Canceled')
            
def caculator(product, quantity):
    total = 0
    if product == 'apple':
        total = total + (quantity * 0.50)
    elif product == 'banana':
        total = total + (quantity * 0.40)
    elif product =='mandarin':
        total = total + (quantity * 0.30)
    elif product =='mango':
        total = total + (quantity * 0.80)
    elif product == 'avocado':
        total = total + (quantity * 0.70)
    elif product == 'jackfruit':
        total = total + (quantity * 10)
    else:
        print("Invalid product")
    total = round(total, 2)
    print(total , end = " dollars \n")
    return total
    
shoping_cart()
        
        
        
    
    