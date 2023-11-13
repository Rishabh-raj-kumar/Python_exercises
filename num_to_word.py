
num = '4'

print(num.isdigit())

if num.isdigit() == 0:
    print('one')

print(num)

numb = int(input('Enter the number (less than 10000) : '))

if numb == 323:
    print('One hundered twenty three')

count = 0
lst = []
sum = 0
while numb > 1:
    num = numb % 10
    sum = sum + int(num)
    lst.append(int(num))
    numb = numb / 10

print('----------------------------------------------------------')
print('     sum : ', int(sum))
print('----------------------------------------------------------')
print('     In list : ', lst[::-1])
print('----------------------------------------------------------')

print('----------------------------------------------------------')
print('     length : ',len(lst))
print('----------------------------------------------------------')

lst = lst[::-1]

print('----------------------------------------------------------')
print('     In words :  ', end=" ")

if len(lst) == 1:
    if lst[0] == 1:
            print('One', end=" ")
    elif lst[0] == 2:
            print('Tw0', end=" ")
    elif lst[0] == 3:
            print('Three', end=" ")
    elif lst[0] == 4:
            print('Four', end=" ")
    elif lst[0] == 5:
            print('Five', end=" ")
    elif lst[0] == 6:
            print('Six', end=" ")
    elif lst[0] == 7:
            print('Seven', end=" ")
    elif lst[0] == 8:
            print('Eight', end=" ")
    elif lst[0] == 9:
            print('Nine', end=" ")

if len(lst) == 2:
    if lst[0] == 1:
            print('One', end=" ")
    elif lst[0] == 2:
            print('Twenty', end=" ")
    elif lst[0] == 3:
            print('Thirty', end=" ")
    elif lst[0] == 4:
            print('Fourty', end=" ")
    elif lst[0] == 5:
            print('Fifety', end=" ")
    elif lst[0] == 6:
            print('Sixty', end=" ")
    elif lst[0] == 7:
            print('Seventy', end=" ")
    elif lst[0] == 8:
            print('Eighty', end=" ")
    elif lst[0] == 9:
            print('Ninety', end=" ")

    if lst[1] == 1:
            print('One', end=" ")
    elif lst[1] == 2:
            print('Two', end=" ")
    elif lst[1] == 3:
            print('Three', end=" ")
    elif lst[1] == 4:
            print('Four', end=" ")
    elif lst[1] == 5:
            print('Five', end=" ")
    elif lst[1] == 6:
            print('Six', end=" ")
    elif lst[1] == 7:
            print('Seven', end=" ")
    elif lst[1] == 8:
            print('Eight', end=" ")
    elif lst[1] == 9:
            print('Nine', end=" ")


if len(lst) == 3:
    if lst[0] == 1:
            print('One hundred', end=" ")
    elif lst[0] == 2:
            print('Two hundred', end=" ")
    elif lst[0] == 3:
            print('Three hundred', end=" ")
    elif lst[0] == 4:
            print('Four hundred', end=" ")
    elif lst[0] == 5:
            print('Five hundred', end=" ")
    elif lst[0] == 6:
            print('Six hundred', end=" ")
    elif lst[0] == 7:
            print('Seven hundred', end=" ")
    elif lst[0] == 8:
            print('Eight hundred', end=" ")
    elif lst[0] == 9:
            print('Nine hundred', end=" ")

    if lst[1] == 1:
            print('One', end=" ")
    elif lst[1] == 2:
            print('Twenty', end=" ")
    elif lst[1] == 3:
            print('Thirty', end=" ")
    elif lst[1] == 4:
            print('Fourty', end=" ")
    elif lst[1] == 5:
            print('Fifety', end=" ")
    elif lst[1] == 6:
            print('Sixty', end=" ")
    elif lst[1] == 7:
            print('Seventy', end=" ")
    elif lst[1] == 8:
            print('Eighty', end=" ")
    elif lst[1] == 9:
            print('Ninety', end=" ")

    if lst[2] == 1:
            print('One', end=" ")
    elif lst[2] == 2:
            print('Two', end=" ")
    elif lst[2] == 3:
            print('Three', end=" ")
    elif lst[2] == 4:
            print('Four', end=" ")
    elif lst[2] == 5:
            print('Five', end=" ")
    elif lst[2] == 6:
            print('Six', end=" ")
    elif lst[2] == 7:
            print('Seven', end=" ")
    elif lst[2] == 8:
            print('Eight', end=" ")
    elif lst[2] == 9:
            print('Nine', end=" ")

if len(lst) == 4:
    if lst[0] == 1:
            print('One Thousand', end=" ")
    elif lst[0] == 2:
            print('Two Thousand', end=" ")
    elif lst[0] == 3:
            print('Three Thousand', end=" ")
    elif lst[0] == 4:
            print('Four Thousand', end=" ")
    elif lst[0] == 5:
            print('Five Thousand', end=" ")
    elif lst[0] == 6:
            print('Six Thousand', end=" ")
    elif lst[0] == 7:
            print('Seven Thousand', end=" ")
    elif lst[0] == 8:
            print('Eight Thousand', end=" ")
    elif lst[0] == 9:
            print('Nine Thousand', end=" ")

    if lst[1] == 1:
            print('One hundered', end=" ")
    elif lst[1] == 2:
            print('Two hundered', end=" ")
    elif lst[1] == 3:
            print('Three hundered', end=" ")
    elif lst[1] == 4:
            print('Four hundered', end=" ")
    elif lst[1] == 5:
            print('Five hundered', end=" ")
    elif lst[1] == 6:
            print('Six hundered', end=" ")
    elif lst[1] == 7:
            print('Seven hundered', end=" ")
    elif lst[1] == 8:
            print('Eight hundered', end=" ")
    elif lst[1] == 9:
            print('Nine hundered', end=" ")

    if lst[2] == 1:
            print('One', end=" ")
    elif lst[2] == 2:
            print('Twenty', end=" ")
    elif lst[2] == 3:
            print('Thirty', end=" ")
    elif lst[2] == 4:
            print('Fourty', end=" ")
    elif lst[2] == 5:
            print('Fifety', end=" ")
    elif lst[2] == 6:
            print('Sixty', end=" ")
    elif lst[2] == 7:
            print('Seventy', end=" ")
    elif lst[2] == 8:
            print('Eighty', end=" ")
    elif lst[2] == 9:
            print('Ninety', end=" ")

    if lst[3] == 1:
            print('One', end=" ")
    elif lst[3] == 2:
            print('Two', end=" ")
    elif lst[3] == 3:
            print('Three', end=" ")
    elif lst[3] == 4:
            print('Four', end=" ")
    elif lst[3] == 5:
            print('Five', end=" ")
    elif lst[3] == 6:
            print('Six', end=" ")
    elif lst[3] == 7:
            print('Seven', end=" ")
    elif lst[3] == 8:
            print('Eight', end=" ")
    elif lst[3] == 9:
            print('Nine', end=" ")

print('\n----------------------------------------------------------')