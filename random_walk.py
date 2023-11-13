import matplotlib.pyplot as plt
from random import choice

step_option = [-1,1]
step_choice = choice(step_option)

# will generate random choice btw -1 and 1.
print(step_choice)

def walk(num):
     walks = []
     step_choice = choice([1,-1])
     walks.append(step_choice)
     for i in range(1,num):
          steps = choice([1,-1]) + walks[i-1]
          walks.append(steps)

     return walks


lst = walk(1000)
print(lst)

# plotting more than 1 walk
def plot(num,walk_list):
     lab_list = list(range(1,num+1))
     for i in range(0,num):
          x = list(range(1,walk_list+1))

          plt.plot(x,walk(walk_list),label = 'Plot Number'+ ' ' + str(lab_list[i]))
          plt.legend(loc = 'lower left')
     plt.show()


plot(5,1000)