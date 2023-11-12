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
    number = str(input())
    minus = False
    if int(number) >= 1000 or int(number) <= -1000: raise Exception
    else:
        if number.startswith("-"): 
            minus = True
            number = int(number[1::])
        else: number = int(number)
        
        if number == 0: print("zero")
        
        elif number < 20: 
            if minus: print(f"negative-{unique[number]}")
            else: print(unique[number])
        elif number < 100:
            if number%10 == 0: 
                if minus: print(f"negative-{tens[number//10]}")
                else: print(tens[number//10])   
            else: 
                if minus: print(f"negative-{tens[number//10]}-{unique[number%10]}")
                else: print({tens[number//10]}-{unique[number%10]}) 
        elif number < 1000:
            if number%100 == 0: 
                if minus: print(f"negative-{unique[number//100]}-hundred")
                else: print(f"{unique[number//100]}-hundred") 
            else:
                twolastdigit = number%100
                if twolastdigit < 20: 
                    if minus: print(f"negative-{unique[number//100]}-hundred-{unique[twolastdigit]}")
                    else: print(f"{unique[number//100]}-hundred-{unique[twolastdigit]}") 
                    
                elif twolastdigit < 100:
                    if twolastdigit%10 == 0: 
                        if minus: print(f"negative-{unique[number//100]}-hundred-{tens[twolastdigit//10]}")
                        else: print(f"{unique[number//100]}-hundred-{tens[twolastdigit//10]}") 
                    else: 
                        if minus: print(f"negative-{unique[number//100]}-hundred-{tens[twolastdigit//10]}-{unique[twolastdigit%10]}")
                        else: print(f"{unique[number//100]}-hundred-{tens[twolastdigit//10]}-{unique[twolastdigit%10]}") 
except: print("ERROR")