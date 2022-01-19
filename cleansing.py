location = input(
    "Location file : (example : C:\\Users\Falah\Downloads\SAMPLE DATA.txt)\nYour location File :")
text = open(location, "r")
ourtext = text.read().split(",")

myStack = []

index = 0
for index in range(len(ourtext)):
    myStack.append(ourtext[index])

out_str = " "

print("Cleansing & Write to Dataset file Success, Result :\n", out_str.join(myStack))
f = open(location, "w")
f.write(out_str.join(myStack))
f.close()
