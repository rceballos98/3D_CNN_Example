import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# data generating script
def place_cube(matrix, origin, r):
    #dim = matrix.shape()
    matrix[
    origin[0]-r:origin[0]+r,
    origin[1]-r:origin[1]+r,
    origin[2]-r:origin[2]+r,
    ] = 1
    return matrix

def dist(x, y):
    return math.sqrt(
        (x[0]-y[0])**2+
        (x[1]-y[1])**2+
        (x[2]-y[2])**2
        )

def place_sphere(matrix, origin, r):
    for index, x in np.ndenumerate(matrix):
        if dist(index, origin) <= r:
            matrix[index] = 1
    return matrix

def random_shapes(m_size,num):
    shapes = np.zeros((m_size,m_size,m_size,num))
    shape_types = np.random.randint(low = 0,high = 2,size= num)
    
    for i in range(num):
        r = np.random.randint(low = 3,high = np.floor(m_size/2-1))
        org = np.random.randint(low = r + 1,high = m_size - r - 1, size = 3)
        if shape_types[i] == 0:
            shapes[:,:,:,i] = place_cube(shapes[:,:,:,i],org,r)
        elif shape_types[i] == 1:
            shapes[:,:,:,i] = place_sphere(shapes[:,:,:,i],org,r)
            
    return shapes, shape_types
        

def matching_shapes(m_size, num):
    cubes = np.zeros((m_size,m_size,m_size,num))
    spheres = np.zeros((m_size,m_size,m_size,num))
    for i in range(num):
        r = np.random.randint(low = 3,high = np.floor(m_size/2-1))
        org = np.random.randint(low = r + 1,high = m_size - r - 1, size = 3)
        cubes[:,:,:,i] = place_cube(cubes[:,:,:,i],org,r)
        spheres[:,:,:,i] = place_sphere(spheres[:,:,:,i],org,r)
    return cubes, spheres

# m_size = 16
# r = 4
# org = int(m_size/2)
# matrix = np.zeros((m_size,m_size,m_size))
# matrix = place_sphere(matrix,(org,org,org), r)

# # Plot
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# z,x,y = np.where(matrix == 0)
# ax.scatter(x, y, -z, zdir='z', c= 'black', s = 0.1)
# z,x,y = matrix.nonzero()
# ax.scatter(x, y, -z, zdir='z', c= 'red', s = 3)
# plt.show()

m_size = 16
num = 50

# cubes, spheres = make_data(m_size,num)


# #Binary data
# np.save('cubes.npy', cubes)
# np.save('spheres.npy', spheres)

# #Human readable data
# np.savetxt('cubes.txt', cubes)
# np.savetxt('spheres.txt', spheres)

# cubes = np.load('cubes.npy')
# spheres = np.load('spheres.npy')

# # Plot matching shapes
# for i in range(num):
#   matrix = cubes[:,:,:,i]
#   fig = plt.figure()
#   ax = fig.add_subplot(111, projection='3d')
#   z,x,y = np.where(matrix == 0)
#   ax.scatter(x, y, -z, zdir='z', c= 'black', s = 0.1)
#   z,x,y = np.where(matrix == 1)
#   ax.scatter(x, y, -z, zdir='z', c= 'red', s = 3)
    
#   plt.draw()

#   matrix = spheres[:,:,:,i]
#   fig2 = plt.figure()
#   ax = fig2.add_subplot(111, projection='3d')
#   z,x,y = np.where(matrix == 0)
#   ax.scatter(x, y, -z, zdir='z', c= 'black', s = 0.1)
#   z,x,y = np.where(matrix == 1)
#   ax.scatter(x, y, -z, zdir='z', c= 'red', s = 3)
    
#   plt.show()

shapes, labels = random_shapes(m_size,num)

# Plot rand shapes
for i in range(num):
    matrix = shapes[:,:,:,i]
    print(labels[i])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    z,x,y = np.where(matrix == 0)
    ax.scatter(x, y, -z, zdir='z', c= 'black', s = 0.1)
    z,x,y = np.where(matrix == 1)
    ax.scatter(x, y, -z, zdir='z', c= 'red', s = 3)
    
    plt.show()






