
from matplotlib import image, pyplot


pic = image.imread('bogere.jpg')
added_pic = pic * 2
print(pic.shape)
print(added_pic.shape)
pyplot.imshow(pic)
pyplot.imshow(added_pic)
pyplot.show()