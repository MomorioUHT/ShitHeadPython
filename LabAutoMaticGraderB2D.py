result = ''
labcase,yours = [],[]

amount = int(input())
for i in range(0,amount):
    labcase.append(input())
for i in range(0,amount):
    yours.append(input())

for i in range(0,len(labcase)):
    if labcase[i] == yours[i]: result += "P"
    else:
        if labcase[i].lower() == yours[i].lower(): result += "C"
        elif labcase[i].replace(" ", "") == yours[i].replace(" ", ""): result += "S"
        else: result += "-"

correct,wrong = 0,0
for i in result: 
    if i == "P": correct += 1
    else: wrong += 1
percentage = (correct/(correct+wrong))*100

print(f"Lab Result: [{result}]")
print(f"Meaning: {correct} Passed {wrong} Failed")
print(f"Percentage: {percentage:.2f}")