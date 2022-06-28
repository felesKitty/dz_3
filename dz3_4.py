
def degree(x, y):
    try:
        res = x ** y
    except TypeError:
        return "Enter float number and negative number"
    return res

print(degree(8.22, -3))