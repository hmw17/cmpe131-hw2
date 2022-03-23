

rawData = open("document.txt")
splitText = rawData.read().split()
arr = {}
for i in splitText:
    if i not in arr:
        arr[i] = 1
    else:
        arr[i] += 1
finaltext = sorted(arr.items(), key=lambda x: x[1])
finaltext.reverse()
finaltext = sorted(finaltext, key=lambda x: x[0])
finaltext = sorted(finaltext, key=lambda x: x[1], reverse=True)
for i in range(5):
    print(finaltext[i][0] + ":", finaltext[i][1])
