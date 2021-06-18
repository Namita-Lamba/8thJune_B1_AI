# QUESTION 2

print(5**9)  # o/p 1953125

print(3//2)  # o/p 1

print(7//3)  # o/p 2

print(7/3)  # o/p 2.333333

print(6==6)  # o/p True

a=20; a+=30; a%=3; print(a)  #o/p 2

print(True*False)  # o/p 0

print(True & False)  # o/p False

print(True and False)  # o/p False

print(((6>3) and (7<4) or (18==3)) and (9>3))  # o/p False

print(True is False)  # o/p False

print(((True==False) or (False>True)) and (False<=True))  # o/p False

# QUESTION 3

s1='Nice to have it';s2='here';print(" ".join([s1,s2])) #  o/p Nice to have it here

# QUESTION 4

a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][-1])

# QUESTION 5

a[0]=s1
a+=[s2]

# QUESTION 6

color_list_1 = set(['white','black','red'])
color_list_2 = set(['red','green'])
print(color_list_1 - color_list_2)  #  o/p {'black','white'}

# QUESTION 7

p = set((input('enter a string')))
s = set('abcdefghijklmnopqrstuvwxyz')

if p==s:
    print('String is pangram')
else:
    print('String is not pangram')

# QUESTION 8

n=eval(input('enter a number'))
e=eval('{0}+{0}{0}+{0}{0}{0}'.format(n))
print(e)

# QUESTION 9

print(','.join(sorted(input('enter a comma seperated words : ').split(','))))

# QUESTION 10

d={'Student':['Rahul','Kishore','Vidhya','Raakhi'], 'Marks': [57,87,67,79]}
m= d['Marks'].index(max(d['Marks']))
print(d['Student'][m])