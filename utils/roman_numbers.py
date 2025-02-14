
def roman_to_integer(roman:str) -> int:
    roman_map={
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    } 
    integer = 0
    for i in range(1, len(roman)):
        breakpoint()
        if roman_map.get(roman[i]) < roman_map.get(roman[i+1]):
            integer = (roman_map.get(roman[i+1]) - roman_map.get(roman[i])) + integer
            i += 2
        else:
            integer = integer + roman_map.get(roman[i])
            i += 1
    return integer
