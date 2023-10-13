import matplotlib.pyplot as plt

import numpy as np 


x=np.linspace(-10,9,20)

y=x**3 
z=x**2
"""
figure=plt.figure()

axes_cube=figure.add_axes([0.1,0.1,0.8,0.8])

axes_cube.plot(x,y,"b")
axes_cube.set_xlabel("X axis ")
axes_cube.set_ylabel("Y axis")
axes_cube.set_title("Cube")


axes_square=figure.add_axes([0.15,0.6,0.3,0.3])
axes_square.plot(x,z,"r")
axes_square.set_xlabel("X axis ")
axes_square.set_ylabel("Y axis")
axes_square.set_title("Square")

"""

# figure=plt.figure()
# axes=figure.add_axes([0,0,1,1])
# axes.plot(x,z,label="Square")
# axes.plot(x,y,label="Cube")
# axes.legend(loc=0) 
# plt.show()


fig , axes =plt.subplots(nrows=2,ncols=1,figsize=(4,4))
axes[0].plot(x,y)
axes[0].set_title("Square")
axes[1].plot(x,z)
axes[1].set_title("Cube")

# fig.savefig("figure1.png")
fig.savefig("figure1.pdf")

plt.tight_layout()
plt.legend(loc=0)
plt.show()