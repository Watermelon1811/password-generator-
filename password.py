fh = open('password.txt','w')
import random 
length = 8 
password_lists='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*' 
password = '' 
i = 0 
while i<length: 
    password = password + random.choice(password_lists) 
    i=i+1 
fh.write(password)