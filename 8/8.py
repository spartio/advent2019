file = open("input8").read()

list=[file[i:i+150] for i in range(0, len(file), 150)]
count=100
for i in list:
    if count > i.count('0'):
        count=i.count('0')
        #print(i.count('1')*i.count('2'))

list2=["2212022", "1221211", "0210210"]
i= 0
j=0
image=[]
while len(image)!=150:
    while i < len(list)-1:
        #print(list[i][j])
        if list[i][j] == "0":
            image.append(list[i][j])
            j+=1
            i=0
        elif list[i][j] == "1":
            image.append(list[i][j])
            j+=1
            i=0
        i+=1
        #print(image)
    image.append(list[i][j])
    j+=1
    i=0

s = [str(i) for i in image]
res = "".join(s)
#print(res)

import re
print(re.sub("(.{25})", "\\1\n", res, 0, re.DOTALL))

for z in range(len(res)):
    if((z+1)%25 == 0):
        print(image[z])
    else:
        print(image[z], end=" ")