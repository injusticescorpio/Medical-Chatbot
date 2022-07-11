txt='110 calories'

li=txt.lower().split(' ')
for i in range(len(li)):
    if 'calories' in li[i].lower() or "cal" in li[i].lower()or "cals" in li[i].lower():
        prev=i-1
        if li[prev].isdigit():
            print(li[prev])
            break

li=[]
li.append(f"tst:{txt}")
print(li)


# if 'calories' in li:
#     print(li[li.index('calories')-1])
# elif 'cal' in li:
#     print(li[li.index('cal')-1])
