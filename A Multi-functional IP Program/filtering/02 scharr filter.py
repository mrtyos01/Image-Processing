"""
@authors:
    Kibru
    Morteza
    Michael
"""
from skimage import data, io
from skimage import filters

camera = data.camera()
edges = filters.scharr(camera)

io.imshow(camera)
io.show()
edges = filters.sobel(camera)
io.imshow(edges)
io.show()