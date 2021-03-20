#with a given interger number n, write a program to generate a dic that contains (i,i*i) such that is an integral number between 1 and n (both included).
# and then the program should print the dict

n = int(input("enter number: "))

new_dec = dict()
i = 0
while(i < n+1):
    new_dec[i] = i*i
    i = i+1
print(new_dec)
