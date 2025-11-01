import random

n = int(input("Masukan bilangan n: "))  

count = 0  
for i in range (1, n + 1):
    while True:  
        angka = random.random()  
        
        if angka < 0.5:  
            print("data ke:", i, "=>", angka)  
            count += 1 
            break
