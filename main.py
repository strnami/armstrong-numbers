def is_armstrong(number,my_num=0):
    list = [int(x) for x in str(number)]
    for num in list:
        my_num = my_num + num**(len(list))
    if my_num == number:
        return True
    return False
