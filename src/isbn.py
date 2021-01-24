def check_isbn(number):
    if type(number) != str or "-" not in number:
        return False
    number_list = number.split("-")
    lit = ""
    for n in number_list:
        lit += n
    if len(lit) != 13:
        return False
    count = 0
    sum = 0
    for digit in lit:
        if digit not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            return False
        if count % 2 == 0:
            sum += int(digit)
        else:
            sum += int(digit)*3
        count +=1
    if sum % 10 == 10 or sum % 10 == 0:
        return True
    else:
        return False