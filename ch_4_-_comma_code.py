def comma_code(list):
    ret_str = list[0]
    for i in range(1, len(list)):
        ret_str = ret_str + ', '
        if i == len(list) - 1:
            ret_str = ret_str + 'and '
        ret_str = ret_str + list[i]
    return (ret_str)

print(comma_code(['apples', 'bananas', 'tofu', 'cats'])
