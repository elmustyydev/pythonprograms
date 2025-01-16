letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','()','+','=','<','>','?','/','|','|','{}']
#easy level
print("welcome to the password generator program!")
import random
n_letters = int(input("How many letters do you want :  "))
n_numbers = int(input("How many numbers do you want  :  "))
n_symbols = int(input("How many symbols do you want :  "))
password = ""
for letter in  range(0, n_letters + 1) :
    password += random.choice(letters)
for number in range(0, n_numbers + 1 ) : 
    password += random.choice(numbers) 
for symbol in range(0 , n_symbols + 1)  :
    password += random.choice(symbols) 
print(f"YOUR GENERATED PASSWORD IS {password}")

                