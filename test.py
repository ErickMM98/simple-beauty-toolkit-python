import matplotlib as plt
import matplotlib.pyplot as plt
from pprint import pprint
import matplotlib as mpl
plt.style.use('./simpletoolkit/styles/general.mplstyle')



import numpy as np

data = np.random.randn(50)
plt.title('A title')
plt.plot(data)
plt.show()
pprint( mpl.rcParams)