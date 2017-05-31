#Cory Althoff - Selt-Taught Programmer
#Chapeter 4 Practice

#Practice Functions

def even_odd(x):

    if x % 2 == 0:

        print("even\n")

    else:

        print("odd\n")

even_odd(2)

print("----------------------\n")

#end

#Take input and convert string input to int data type   
n = input("type a number:\n")
n = int(n)

def even_odd_again(n):
    if n % 2 == 0:
        print("n is even.\n")
    else:
        print("n is odd.\n")


#call the function
even_odd_again(n)



print("----------------------\n")

#end


print("Division Calculator\n")
print("-------------------\n")

try:

    a = input("Type the numerator:\n")
    b = input("Type the denominator:\n")

    a = int(a)
    b = int(b)

    print(a/b)

except (ZeroDivisionError, ValueError):
    print("Invalid input.\n")

print("----------------------\n")

#end



