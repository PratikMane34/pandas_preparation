#palindrome for string 
def pal(string):
    string = string.lower()
    reverse_string = string[::-1]
    flag = 0
    print(reverse_string)
    for i in range(len(string)):
        if string[i] != reverse_string[i]:
            flag = 1
            return True
    return False

# a = "NITIN"
a = input("Enter your string: ")
if pal(a):
    print("Given string is not palindrome")
else:
    print("string is palindrome")



