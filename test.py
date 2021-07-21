import pylab
from sklearn import datasets 


duke = datasets.load_digits()

print(duke.images[0])

pylab.imshow(duke.images[0])
pylab.show()