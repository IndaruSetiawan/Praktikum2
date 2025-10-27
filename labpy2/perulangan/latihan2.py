import random

n = int(input("Masukan bilangan n: "))  

count = 0  
for i in range (n):
    while True:  
        angka = random.random()  
        
        if angka < 0.5:  
            print(angka)  
            count += 1 
            break
