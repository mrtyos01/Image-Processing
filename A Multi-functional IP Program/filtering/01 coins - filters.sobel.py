"""
@authors:
    Kibru
    Morteza
    Michael
"""
from skimage import data, io, filters

image = data.coins()
#first we demonstrate the initial image before the filtering
io.imshow(image)
io.show()
edges = filters.sobel(image)
io.imshow(edges)
io.show()