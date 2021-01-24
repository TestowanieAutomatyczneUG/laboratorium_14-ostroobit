def distance(str1, str2):
    if str1 == "" and str2 == "":
        return 0
    elif len(str1) > len(str2):
        raise ValueError("Strands' lengths must be equal!")
    elif len(str2) > len(str1):
        raise ValueError("Strands' lengths must be longer")
    elif len(str1) == 0:
        raise ValueError("First strand cannot be empty!")
    elif len(str2) == 0:
        raise ValueError("Second strand cannot be empty!")
    else:
        result = 0
        for x in range(len(str1)):
            if str1[x] != str2[x]:
                result += 1
        return result
