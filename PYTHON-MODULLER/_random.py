import random

# result=dir(random)
# result=help(random)

result=random.random() #0.0 - 1.0
result=random.random()*100
result=random.uniform(1,10)
result=random.uniform(1,100) #bunu int yaparsan
result=random.randint(1,100)

names=['ali','yağmur','deniz','cenk','ahmet','yasin']
greeting="Hello There"
result=names[random.randint(0,len(names)-1)]
result=random.choices(names) #['cenk']
result=random.choice(names)  #cenk

result=random.choice(greeting)

liste=list(range(10))
random.shuffle(liste)
result=liste

liste=range(100)

result=random.sample(liste,3)
result=random.sample(names,2)
print(result)