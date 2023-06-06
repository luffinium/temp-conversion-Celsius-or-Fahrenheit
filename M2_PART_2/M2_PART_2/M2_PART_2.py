


def convertTemp (tempList, tempScale):
    if tempScale == "F":
        tempList[0] = (tempList[0] - 32) * 5/9
    elif tempScale == "C":
        tempList[1] = (tempList[1] * 9/5) + 32
    return tempList
while True:
    temp = float(input("Enter a temperature: "))
    while True:
        tempScale = input("Enter a single letter to indicate the temperature scale (C or F): ")
        if tempScale == "F" or tempScale =="C":
            break
    tempList = [0,0]
    if tempScale == "C":
        tempList[1] = temp 
    elif tempScale == "F":
        tempList[0] = temp

    print ("You entered ", temp, " degrees ", tempScale)
    outputTemp = convertTemp (tempList, tempScale)
    if tempScale == "F":
        print ("The temperature in Celsius is ",outputTemp[0])
    elif tempScale == "C":
        print ("The temperature in Fahrenheit is ",outputTemp[1])









