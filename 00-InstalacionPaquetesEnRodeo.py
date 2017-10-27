! pip install ggplot

from ggplot import *

diamonds.head()

ggplot(diamonds, aes(x='carat', y='price', color='cut')) + geom_point()
