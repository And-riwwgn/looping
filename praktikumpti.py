#1. variable 


#2 operator -> +,-,/,*

#3.perulangan --> looping
#for statment

for baris in range(5):
    for kolom in range (4):
         print("*", end="")
    print()

print("======================")
baris2 = 0  # Start from 0 to allow iteration
tengah = 5
kolom2 = 0

while baris2 < 5:
    kolom2 = 0  
    if baris2 % 2 == 1:  
        while kolom2 < 5:
            if kolom2 == int(tengah / 2):  
                print("*", end="")
            else:
                print(" ", end="")  
            kolom2 += 1
    else:  
        while kolom2 < 5:
            print("*", end="") 
            kolom2 += 1
    print()  
    baris2 += 1  
