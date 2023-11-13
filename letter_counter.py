import matplotlib.pyplot as plt
words = """
There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, 
or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't 
anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary,
 making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures,
   to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.
"""

letter_count=  {}
for letter in words:
    #letter_count.get() will return repeating number if found else 0.
    letter_count[letter.lower()] = letter_count.get(letter,0)+1

# print(letter_count)

#but there is a cache all the ltters are included but we want only alphabets.
letter_alphabets = {}

for key,value in letter_count.items():
    if key.isalpha():
        letter_alphabets[key] = value

print(letter_alphabets)

x,y = zip(*letter_alphabets.items())

# plt.bar(x,y)
# plt.show()

# zip methods
a = [1,2,3,5]
b = ['hii','hello','my','mello']

pack = list(zip(a,b))

x,y = zip(*pack)
print(pack)
print(x)

# you can do the same with counter
from collections import Counter

print(Counter(words))
new_dict = dict(Counter(words.lower()))

new_alpha_dect = {key:value for key,value in new_dict.items() if key.isalpha()}
print(new_alpha_dect)