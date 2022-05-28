import numpy as np
from sklearn import dataloader
a = np.array(dataloader.iris())
b = 'good'
if isinstance(a,b):
  a = a**2
else:
  b = 'merit'
