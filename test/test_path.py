import numpy as np
from PIL import Image
import plan

im = Image.open("test_map.pgm")
im.show()
mymap = np.asarray(im)

x = mymap.shape[1]//2
y = mymap.shape[0]//2

route = plan.plan(mymap, x, y)
assert len(route) > 1, "Less than two points in the route"
assert len(route) == len(set(route)), "Duplicate points in route"


