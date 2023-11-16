import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

def getImage(path):
   return OffsetImage(plt.imread(path, format="png"), zoom=.2)

paths = ['cat2.png', 'cat2.png']
x = [8, 4]
y = [5, 3]
fig, ax = plt.subplots()
for x0, y0, path in zip(x, y, paths):
   ab = AnnotationBbox(getImage(path), (x0, y0), frameon=False)
   ax.add_artist(ab)
plt.xticks(range(10))
plt.yticks(range(10))
plt.show()
