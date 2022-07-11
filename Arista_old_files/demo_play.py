import re
#
# text = 'For the small-scale wonder, idli packs a good punch of protein, fibre and carbohydrates. In a single idli, it has merely 39 calories'
# pattern = '\D'
# result = re.sub(pattern, '',text)
#
# print(int(result))


#
# d={'a':{'c':1,"d":2},'b':{'c':5,'d':3}}
# print(d.items())
# print(sorted(d.items(),key=lambda x:x[1]['c'],reverse=True))
b="4.5(19)"
print(b.replace('(',' ').replace(')',''))