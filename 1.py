print("\033c")

import math 

def find_multiplier(numb): 
    while numb % 2 == 0: 
        print(2) 
        numb = numb / 2 
    for i in range(3, int(math.sqrt(numb)) + 1, 2): 
        while numb % i == 0: 
            print(i) 
            numb = numb / i 
    if numb > 2: 
        print(numb) 
 
numb = int(input("Введите натуралное число для его разложения на множители: ")) 

find_multiplier(numb) 