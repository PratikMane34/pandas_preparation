#multiplication table of user's choice
def multiplication_table(no):
    print(ord(str(no)))
    return [no*i for i in range(1,11)]

#print(multiplication_table(3))

def factor(no):
    if no == 1:
        return no
    else:
        print(no)
        return no*factor(no-1)


print(factor(5))
