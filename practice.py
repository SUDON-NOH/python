# Q.1
subj = ['국어', '영어', '수학']
point = [80, 75, 55]

print(sum(point)/3)

# Q.2
num = 13
print(num % 2 == 0)

even_odd = ['짝수', '홀드']
print("%d : %s" %(num,even_odd[num % 2]))

number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))


# Q.3
pin = "881120-1068234"
yyyymmdd = pin[:6]
print(yyyymmdd)
num = pin[7:]
print(num)


# Q.4
pin = "881120-2068234"
gender = ['남성', '여성']
print("%d : %s" % (int(pin[7]), gender[int(pin[7]) - 1]))


# Q.5
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

# Q.6
a = [1, 3, 5, 4, 2]
a.sort()
print(a)
a.sort(reverse = True)
print(a)

# Q.7
a = ['Life', 'is', 'too', 'short']
result = ' '.join(a)
print(result)

# Q.8
a = (1, 2, 3)
b = a + (4,)
print(b)

# Q.9
a = dict()
print(a, type(a))

a['name'] = 'python'
print(a)
a[('a')] = 'python'
print(a)
# a[[1]] = 'python'
# print(a)
a[250] = 'python'
print(a)

# Q.10

a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(result)
print(a)

# Q.11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)

# Q.12
a = b = [1, 2, 3]
a[1] = 4
print(b)
print(id(a) == id(b))
print(hex(id(a)), hex(id(b)))

