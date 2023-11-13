# two sum problem'


def ret_sum(lst,target):
    dic = {}
    for i in range(len(lst)):
       if target - lst[i] in dic:
           return [dic[target - lst[i]],i]
       
       dic[lst[i]] = i

    return -1

lst = [1,3,4,7,8,2]
print(ret_sum(lst,9))


# caesar cipher
alphabets = 'abcdefghijklomnpqrstuvwxyz'
text = 'zy'
encrypt = ''

def shift_amount(i):
    return i % 26

for char in text:
    index = alphabets.find(char)
    encrypt = encrypt + alphabets[shift_amount(index+4)]

print(encrypt)
