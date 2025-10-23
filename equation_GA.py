#!/usr/bin/env python
# coding: utf-8

# In[11]:


import random
import math

pop = []
pop_num = 6
chro_num = 1
gen_num = 3
chro_fitness = {}

def initialize_pop():
    for i in range(pop_num):
        gen = []
        for i in range(gen_num - 1):
            gen.append(random.randint(-20,20))
        gen.append(random.randint(-100,100))
        pop.append(gen)

def cal_fitness():
    for i in range(pop_num):
        x = pop[i][0]
        y = pop[i][1]
        z = pop[i][2]
        val = 2*pow(x,2) + 3*pow(y,2) + z - 2*x*y + 10*x*z -5
        chro_fitness[i] = (abs(val))

def crossover(f_chro,s_chro):
     for i in range(gen_num):
        temp = f_chro[1]
        f_chro[1] = s_chro[1]
        s_chro[1] = temp
        
def selection(chro_fitness, pop):
    chro_fitness = sorted(chro_fitness.items(), key=lambda x:x[1])
    temp = []
    temp.append(pop[chro_fitness[0][0]])
    temp.append(pop[chro_fitness[1][0]])
    temp.append(pop[chro_fitness[2][0]])
    temp.append(pop[chro_fitness[0][0]])
    temp.append(pop[chro_fitness[1][0]])
    temp.append(pop[chro_fitness[0][0]])
    pop = temp
    for f_chro, s_chro in zip(pop[:3], pop[3:]):
        crossover(f_chro,s_chro)

def mutation():
    rand_index = random.sample(range(0,6), 3)
    for i in rand_index:
        j = random.randint(0,2)
        if j == 2:
            pop[i][j] = random.randint(-100,100) 
        else:
            pop[i][j] = random.randint(-20,20)
    
def check_if_zero():
    for i in range(pop_num):
        if(chro_fitness[i] == 0):
            return i
    return -1

def calc():
    initialize_pop() 
    print('initial population :',pop)
    count = 0
    while(True):
        cal_fitness()
        i = check_if_zero()
        if(i != -1):
            print('x: {0} , y: {1} , z: {2}'.format(pop[i][0], pop[i][1], pop[i][2]))
            print('count: {0}'.format(count))
            break
        selection(chro_fitness, pop)
        mutation()
        count += 1
        
calc()


# In[ ]:





# In[ ]:




