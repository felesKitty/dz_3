
def my_func(arg_01, arg_02, arg_03):
    try:
        my_list = list(map(float, [arg_01, arg_02, arg_03]))
        my_list.remove(min(my_list))
        return sum(my_list)
    except (TypeError, ValueError):
        return "It's an error. Enter only a numbers!"

print(my_func(input(), input(), input()))