import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd 

x=[1,2,3,4]
y=[1,4,9,16]
#tek yer verirsen yer veriri 
# plt.plot(x,y,color="red",linewidth=5)
# plt.plot(x,y,'-g')
# plt.plot(x,y,'--')
""" fmt= [Marker][line][color] """ 
# plt.plot(x,y,'o--r')
# plt.plot(x,y,'--r')
# plt.axis([0,6,0,20]) böyle olursa  liste olarak vereblriiisn 

# plt.title("Grafik başlığı")
# plt.xlabel("X Label")
# plt.ylabel("Y Label")


# x=np.linspace(0,2,100)

# plt.plot(x,x,label="linear",color="red")
# plt.plot(x,x**2,label="quadratic",color="green")
# plt.plot(x,x**3,label="cubic",color="blue")

# plt.title("3 ÇİZGİ GRAFİĞİ")
# plt.xlabel("X Label")
# plt.ylabel("Y Label")

# plt.legend()
# plt.show()

# x=np.linspace(0,2,100)
# fig,axs=plt.subplots(3)

# axs[0].plot(x,x,color="red")
# axs[0].set_title("linear")
# axs[1].plot(x,x**2,color="blue")
# axs[1].set_title("quanratic")
# axs[2].plot(x,x**3,color="green")
# axs[2].set_title("cubic")

# plt.tight_layout()

# x=np.linspace(0,2,100)
# fig,axs=plt.subplots(2,2)
# fig.suptitle("Grafik Başlığı ")

# axs[0,0].plot(x,x,label="linear",color="red")
# axs[0,1].plot(x,x**2,label="quadratic",color="green")
# axs[1,0].plot(x,x**3,label="cubic",color="blue")
# axs[1,1].plot(x,x**4,label="cubic",color="black")


import pandas as pd

df = pd.read_csv("nba.csv")

df = df.drop(["Number"], axis = 1).groupby("Team").mean()

df.head().plot(subplots=True)
plt.legend()
plt.show() 





