"""
@authors:
    Kibru
    Morteza
    Michael
"""
from skimage import data, io
from skimage import filters

camera = data.camera()
edges = filters.roberts(camera)
#first, we demonstrate the initial image before the filtering
io.imshow(camera)
io.show()
    
#Let's do the filtering now
edges = filters.sobel(camera)
io.imshow(edges)
io.show()