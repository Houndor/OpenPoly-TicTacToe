def isPalindrome():
    string = str(i)
    reverse = string[3:-1:0]
    return string==reverse

def areaSquare(width):
    return width * width

def areaCircle(radius):
    PI = 3.14159
    return PI * (radius * radius)


if __name__ == ' __main__ ':
    # Display Name
    print("Calculations")
    print("1. Calculate area of a square")
    print("2. Calculate area of a circle")
    print("3. Display palindromes up to 1,000")
    print("4. Exit application")
    # Get Input
    print("Enter an Option: ")
    option = int(input())
    if option >=1 & option <=3:
        if option == 1:
            print("\n**** Area of a square ****")
            print("Enter width of square (cm): ")
            width = int(input())
            print("The area of a square of " + width + "cm = " + areaSquare(width) + "cm squared")
        elif option == 2:
            print("\n**** Area of a circle ****")
            print("Enter radius of circle (cm): ")
            radius = int(input())
            print("The area of a square of " + radius + "cm = " + areaCircle(radius) + "cm squared")
        elif option == 3:
            print("\n**** Palindromes ****")
            for i in range(0,1000):
                if isPalindrome():
                    print(i)
        elif option == 4:
            SystemExit
    else:
        print("Invalid Option")
