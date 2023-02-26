#pengkondisian diidentifikasikan menggunakan if, if else, maupun elif
a = 20

if a < 30:
    print('ini adalah if')

if a < 10:
    print('ini if pada if else')
else: 
    print('ini else pada if else')

if a > 10:
    print('ini if pada if elif else')
elif a > 20:
    print('ini elif pada if elif else')
else:
    print('ini else pada if elif else')