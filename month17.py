import matplotlib.pyplot as plt
import numpy

multi17=[1135, 965, 1096, 1098, 1308, 1342, 1274, 1242, 1296, 1277, 1218, 1269]
collision17=[17551, 15835, 19336, 17829, 21012, 21369, 19593, 19134, 19604, 20358, 19661, 19751]
name_list = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

bar1=plt.bar(range(len(name_list)), multi17, label='multi-car',fc = 'b')
bar2=plt.bar(range(len(name_list)), collision17, bottom=multi17, label='total collision',fc = 'y')
plt.xticks(numpy.arange(0.4, 12.5, 1), name_list)
plt.legend()
i=0
for rect in bar2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '{:.1%}'.format(float(multi17[i])/collision17[i]), ha='center', va='bottom')
    i+=1
plt.show()
