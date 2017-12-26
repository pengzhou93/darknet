import numpy as np


d_wh = 13
d_anchors =  np.array([0.57273, 0.677385, 1.87446, 2.06253, 3.33843, 5.47434, 7.88282, 3.52778, 9.77052, 9.16828])

wh = 18

anchors = np.array([0.5, 0.5, 2., 2., 5., 5., 8., 8., 11, 11.])/d_wh*wh
print np.round(anchors, 5).tolist()
