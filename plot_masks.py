import numpy as np
from cellpose import plot, utils
import matplotlib.pyplot as plt

dat = np.load('arr_0_seg.npy', allow_pickle=True).item()
print(dat)

# plot image with masks overlaid
mask_RGB = plot.mask_overlay(dat['img'], dat['masks'],
                             colors=np.array(dat['colors']))

# plot image with outlines overlaid in red
outlines = utils.outlines_list(dat['masks'])
plt.imshow(dat['img'])
for o in outlines:
    plt.plot(o[:, 0], o[:, 1], color='r')
