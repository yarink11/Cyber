raw1 = []
raw2 = []
raw3 = []
raw4 = []
raw5 = []
raw6 = []
raw7 = []
raw8 = []
raw9 = []
straightraw1 = []
straightraw2 = []
straightraw3 = []
straightraw4 = []
straightraw5 = []
straightraw6 = []
straightraw7 = []
straightraw8 = []
straightraw9 = []
cube1 = []
cube2 = []
cube3 = []
cube4 = []
cube5 = []
cube6 = []
cube7 = []
cube8 = []
cube9 = []
valid = True
straightraws1 = straightraw1,straightraw2,straightraw3
straightraws2 = straightraw4,straightraw5,straightraw6
straightraws3 = straightraw7,straightraw8,straightraw9
raws = raw1,raw2,raw3,raw4,raw5,raw6,raw7,raw8,raw9
cubes = cube1, cube2, cube3, cube4,cube5,cube6,cube7,cube8,cube9
for raw in raws:
    nums = input("Enter your 9 numbers > ")
    for x in nums:
        if x == "0":
            x = " "
        raw.append(x)
    if len(raw) < 9:
        for x in range(9- len(raw)):
            raw.append(" ")
    for i in raw:
        if i == " ":
            valid = False
        elif raw.count(i) > 1:
            valid = False
        if i == raw[0]:
            straightraw1.append(i)
        elif i == raw[1]:
            straightraw2.append(i)
        elif i == raw[2]:
            straightraw3.append(i)
        elif i == raw[3]:
            straightraw4.append(i)
        elif i == raw[4]:
            straightraw5.append(i)
        elif i == raw[5]:
            straightraw6.append(i)
        elif i == raw[6]:
            straightraw7.append(i)
        elif i == raw[7]:
            straightraw8.append(i)
        elif i == raw[8]:
            straightraw9.append(i)
        else:
            raw.remove(x)

def append_to_cubes1(straightraw):
    for r in straightraw:
        if r == " ":
            valid = False
        elif straightraw.count(r) > 1:
            valid = False
        if r == straightraw[0]:
            cube1.append(r)
        elif r == straightraw[1]:
            cube1.append(r)
        elif r == straightraw[2]:
            cube1.append(r)
        elif r == straightraw[3]:
            cube2.append(r)
        elif r == straightraw[4]:
            cube2.append(r)
        elif r == straightraw[5]:
            cube2.append(r)
        elif r == straightraw[6]:
            cube3.append(r)
        elif r == straightraw[7]:
            cube3.append(r)
        elif r == straightraw[8]:
            cube3.append(r)
def append_to_cubes2(straightraw):
    for r in straightraw:
        if r == " ":
            valid = False
        elif straightraw.count(r) > 1:
            valid = False
        if r == straightraw[0]:
            cube4.append(r)
        elif r == straightraw[1]:
            cube4.append(r)
        elif r == straightraw[2]:
            cube4.append(r)
        elif r == straightraw[3]:
            cube5.append(r)
        elif r == straightraw[4]:
            cube5.append(r)
        elif r == straightraw[5]:
            cube5.append(r)
        elif r == straightraw[6]:
            cube6.append(r)
        elif r == straightraw[7]:
            cube6.append(r)
        elif r == straightraw[8]:
            cube6.append(r)
def append_to_cubes3(straightraw):
    for r in straightraw:
        if r == " ":
            valid = False
        elif straightraw.count(r) > 1:
            valid = False
        if r == straightraw[0]:
            cube7.append(r)
        elif r == straightraw[1]:
            cube7.append(r)
        elif r == straightraw[2]:
            cube7.append(r)
        elif r == straightraw[3]:
            cube8.append(r)
        elif r == straightraw[4]:
            cube8.append(r)
        elif r == straightraw[5]:
            cube8.append(r)
        elif r == straightraw[6]:
            cube8.append(r)
        elif r == straightraw[7]:
            cube8.append(r)
        elif r == straightraw[8]:
            cube8.append(r)
for raw in straightraws1:
    append_to_cubes1(raw)
for raw in straightraws2:
    append_to_cubes2(raw)
for raw in straightraws3:
    append_to_cubes3(raw)
for cube in cubes:
    for c in cube:
        if c == " ":
            valid = False
        elif cube.count(c) > 1:
            valid = False

print(raw1[0]," ",raw1[1]," ",raw1[2]," ","|"," ",raw1[3]," ",raw1[4]," ",raw1[5]," ","|"," ",raw1[6]," ",raw1[7]," ",raw1[8])
print(raw2[0]," ",raw2[1]," ",raw2[2]," ","|"," ",raw2[3]," ",raw2[4]," ",raw2[5]," ","|"," ",raw2[6]," ",raw2[7]," ",raw2[8])
print(raw3[0]," ",raw3[1]," ",raw3[2]," ","|"," ",raw3[3]," ",raw3[4]," ",raw3[5]," ","|"," ",raw3[6]," ",raw3[7]," ",raw3[8])
print("------------|---------------|---------------")
print(raw4[0]," ",raw4[1]," ",raw4[2]," ","|"," ",raw4[3]," ",raw4[4]," ",raw4[5]," ","|"," ",raw4[6]," ",raw4[7]," ",raw4[8])
print(raw5[0]," ",raw5[1]," ",raw5[2]," ","|"," ",raw5[3]," ",raw5[4]," ",raw5[5]," ","|"," ",raw5[6]," ",raw5[7]," ",raw5[8])
print(raw6[0]," ",raw6[1]," ",raw6[2]," ","|"," ",raw6[3]," ",raw6[4]," ",raw6[5]," ","|"," ",raw6[6]," ",raw6[7]," ",raw6[8])
print("------------|---------------|---------------")
print(raw7[0]," ",raw7[1]," ",raw7[2]," ","|"," ",raw7[3]," ",raw7[4]," ",raw7[5]," ","|"," ",raw7[6]," ",raw7[7]," ",raw7[8])
print(raw8[0]," ",raw8[1]," ",raw8[2]," ","|"," ",raw8[3]," ",raw8[4]," ",raw8[5]," ","|"," ",raw8[6]," ",raw8[7]," ",raw8[8])
print(raw9[0]," ",raw9[1]," ",raw9[2]," ","|"," ",raw9[3]," ",raw9[4]," ",raw9[5]," ","|"," ",raw9[6]," ",raw9[7]," ",raw9[8])
if valid == True:
    print("valid")
else:
    print("invalid")
