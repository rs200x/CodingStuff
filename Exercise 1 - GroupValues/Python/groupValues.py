def invert(value):
    return  value[1:] + value[0]

def upperFirst(value):
    return value[0].upper() + value[1:]

source = ["Tokyo", "London", "Rome", "Donlon", "Kyoto", "Paris"]
lowitems = []
for item in source:
    lowitems.append(item.lower())

output = []
processedItems = []
for item in lowitems[:]:
    if item in processedItems:
        continue

    matchFound = False
    inverted = item

    for i in range(len(item)-1):
        inverted = invert(inverted)
        if inverted in lowitems:
            processedItems.append(item)
            processedItems.append(inverted)
            output.append([upperFirst(item), upperFirst(inverted)])
            lowitems.remove(item)
            lowitems.remove(inverted)
            matchFound = True
    if not matchFound:
        output.append([upperFirst(item)])

print(output)