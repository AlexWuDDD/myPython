import sys, argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ON = 255
OFF = 0

vals = [ON, OFF]


def randomGrid(N):
    """return a grid of NxN random values"""
    return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)

"""
x = np.array([[0, 0, 255], [255, 255, 0], [0, 255, 0]])  # 定义3X3二位数组
plt.imshow(x, interpolation="nearest")
plt.show()
"""
# 从列表[0,255]中选择一个值
# 每个值出现的概率由参数p=[0,1, 0.9]指定, p中的值相加必须等于1
# choice方法创建了16个值的一维数组，所以用.reshape使它成为一个二位数组
print(np.random.choice([0, 255], 4*4, p=[0.1, 0.9]).reshape(4, 4))


def addGlider(i, j, grid):
    """adds a glider with top left cell at (i ,j)"""
    glider = np.array([[0, 0, 225],
                       [255, 0, 255],
                       [0, 255, 255]])
    grid[i:i+3, j:j+3] = glider

"""
N = 4
grid = np.zeros(N*N).reshape(N, N)
addGlider(1, 1, grid)
plt.imshow(grid, interpolation="nearest")
plt.show()
"""


def update(frameNum, img, grid, N):
    # copy grid since we require 8 neighbors for calculator
    # and we go line by line
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            # compute 8-neighbor sum using toroidal boundry conditions
            # x and y wrap around so that simulation
            # takes place on a toroidal surface
            total = int(grid[i, (j-1) % N] + grid[i, (j+1) % N] +
                        grid[(i-1) % N, j] + grid[(i+1) % N, j] +
                        grid[(i-1) % N, (j-1) % N] + grid[(i-1) % N, (j+1) % N] +
                        grid[(i+1) % N, (j-1) % N] + grid[(i+1) % N, (j+1) % N]) / 255
            # apply Conway's rules
            if grid[i, j] == ON:
                if(total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON
    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img


# main() function
def main():
    # set grid size
    N = 100

    # set animation update interval
    updateInterval = 50

    # declare grid
    grid = randomGrid(N)

    # set up the animation
    fig, ax = plt.subplots();
    img = ax.imshow(grid, interpolation="nearest")
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
                                  frames=10,
                                  interval=updateInterval,
                                  save_count=50)
    # number of frames?
    plt.show()


# call main
if __name__ == '__main__':
    main()
