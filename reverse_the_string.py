word = "hello world"

rev = ''

for char in word:
    rev = char + rev

print('reversed word : ',rev)

#fibonnaci number
f,a,b =20,0,1
fib_nums = []
for i in range(f):
    fib_nums.append(a)
    a,b = b,a+b

print(fib_nums)

#odd and even
nums = 100
even = []
odd = []

for i in range(nums):
    if not i % 2:
        even.append(i)
    else:
        odd.append(i)

print('even : ',even)
print('odd : ',odd)