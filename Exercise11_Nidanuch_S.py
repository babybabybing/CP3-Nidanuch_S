number = int(input())
space = number
for x in range(number):
        space = space - 1
        print(" "*space,"*"*((x*2)+1))