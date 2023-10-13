import  matplotlib.pyplot as plt
import numpy as np



#stack plot 

"""
yil=[2011,2012,2013,2014,2015]

oyuncu1=[8,10,12,7,9]
oyuncu2=[7,16,22,1,4]
oyuncu3=[3,14,16,4,14]


plt.plot([],[],color="y",label="oyuncu1")
plt.plot([],[],color="r",label="oyuncu2")
plt.plot([],[],color="b",label="oyuncu3")
plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3,colors=['y','r','b'])
plt.title("Yıllara Göre Atılan Goller")
plt.legend(loc=0)

"""

#Pie Grafiği 
"""

goal_types='Penalti','Kaleye Atılan şut','Serbest Vuruş'

golas=[12,35,7]
colors=['y','r','b']

plt.pie(golas,labels=goal_types,colors=colors,shadow=True,explode=(0.05,0.05,0.05),autopct="%1.1f%%")
"""

#bar Graiği 

# plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label="BMW",width=.5)
# plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,70,50,60],label="Audi",width=.5)

# plt.legend()
# plt.xlabel("Gün")
# plt.ylabel("Mesafe (km)")
# plt.title("Araç Bilgileri")

yaslar=np.random.randint(1,120,78)
yas_gruplari=[0,10,20,30,40,50,60,70,80,90,100]

plt.hist(yaslar,yas_gruplari,histtype="bar",rwidth=0.8)
plt.xlabel("yaş grupları")
plt.ylabel("Kişi Sayısı")
plt.title("Histigrom")
plt.show()