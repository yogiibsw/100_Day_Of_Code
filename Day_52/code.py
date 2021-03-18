#find fact of a number

def yogif(v):
    if v==0:
        return 1
    return v*yogif(v-1)
print(yogif(int(input("enter any number: "))))

