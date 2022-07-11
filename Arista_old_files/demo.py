from bs4 import BeautifulSoup
d=[[(1, 'arjun', '+919074774118', 'Chengannur,Kerala'), 0.001], [(2, 'Kiara', '9270537531', 'Mannar,Kerala'), 10.3], [(6, 'Jivika', '+914131459014', 'Chengannur,Kerala'), 0.001], [(10, 'Nishith', '+911334476321', 'Adoor,Kerala'), 26.7], [(17, 'Advika', '06375938330', 'Pathanamthitta,Kerala'), 24.3], [(18, 'Damini', '09280328494', 'Changanassery,Kerala'), 17.6], [(19, 'Jhanvi', '+910808064462', 'Kallissery,kerala'), 2.7]]
print(d[0][1])
d=sorted(d,key=lambda x:x[1])
for i in d:
    print(i[0][2])