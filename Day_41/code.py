from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [5,7,11]
y = [15,6,10]

x2 = [5,11,5]
y2 = [5,13,9]

plt.scatter(x, y)#, align='center')

plt.scatter(x2, y2, color='g')#, align='center')


plt.title('Test')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()