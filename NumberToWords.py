unique = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
    }
tens = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
    }

try:
    number = input()
    if int(number) >= 1000 or int(number) < 0 or number == "-0": raise Exception
    else:
        number = int(number)
        if number == 0: print("zero")
        elif number < 20: print(unique[number])
        elif number < 100:
            if number%10 == 0: print(tens[number//10])    
            else: print(tens[number//10]+"-"+unique[number%10])
        elif number < 1000:
            if number%100 == 0: print(unique[number//100]+"-hundred")
            else:
                twolastdigit = number%100
                if twolastdigit < 20: print(unique[number//100]+"-hundred-"+unique[twolastdigit])
                elif twolastdigit < 100:
                    if twolastdigit%10 == 0: print(unique[number//100]+"-hundred-"+tens[twolastdigit//10])
                    else: print(unique[number//100]+"-hundred-"+tens[twolastdigit//10]+"-"+unique[twolastdigit%10])
except: print("ERROR")