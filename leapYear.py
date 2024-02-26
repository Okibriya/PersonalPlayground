
numbers = int(input("Input year: "))

if numbers < 1800 :
    print("Input year should be more than 1800")
    numbers = int(input("Input year: "))
elif numbers % 4 == 0 :
    print("Leap Year")
else:
    print("Normal Year")

print(numbers)
