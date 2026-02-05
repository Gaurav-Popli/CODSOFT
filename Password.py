import random
char="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?"

length=(int)(input("Please Enter the length of password you want to generate:"))
password=""
for a in range(length):
    password+=random.choice(char)

print("Your Generated Password Is:\n",password)