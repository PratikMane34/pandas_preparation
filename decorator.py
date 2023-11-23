def dec(func):
    def wrapper(a):
        print("=== inside decorator function ===")
        return a.lower()
    return wrapper

@dec
def upper_case(a):
    return a


a = "Main function called"
print(upper_case(a))