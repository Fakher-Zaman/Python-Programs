num = input("Enter Something Here: ")

def float_check(num):
    try:
        float(num)
        return True
    except:
        return False

print(float_check(num))