from matplotlib import pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
import numpy as np

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

def drawVector(fig, pointA, pointB, **kwargs):
	ms = kwargs.get('mutation_scale', 20)
	ars = kwargs.get('arrowstyle', '-|>')
	lc = kwargs.get('lineColor', 'k')
	pc = kwargs.get('projColor', 'k')
	projOn = kwargs.get('proj', True)

	if pointA.size == 3:
		xs = [pointA[0], pointB[0]]
		ys = [pointA[1], pointB[1]]
		zs = [pointA[2], pointB[2]]
	else:
		xs = [pointA[0,3], pointB[0,3]]
		ys = [pointA[1,3], pointB[1,3]]
		zs = [pointA[2,3], pointB[2,3]]

	out = Arrow3D(xs, ys, zs, mutation_scale=ms, arrowstyle=ars, color=lc)
	fig.add_artist(out)

	if projOn==True:
		fig.plot(xs, ys, [0, 0], color=pc, linestyle='--')
		fig.plot([xs[0], xs[0]], [ys[0], ys[0]], [0, zs[0]], color=pc, linestyle='--')
		fig.plot([xs[1], xs[1]], [ys[1], ys[1]], [0, zs[1]], color=pc, linestyle='--')
		
def drawCoordinator(fig, *args, **kwargs):
	ms = kwargs.get('mutation_scale', 20)
	ars = kwargs.get('arrowstyle', '-|>')

	if len(args) == 4:
		ORG = args[0]
		hat_X = args[1]
		hat_Y = args[2]
		hat_Z = args[3]
		xs_n, ys_n, zs_n = [ORG[0], hat_X[0]], [ORG[1], hat_X[1]], [ORG[2], hat_X[2]]
		xs_o, ys_o, zs_o = [ORG[0], hat_Y[0]], [ORG[1], hat_Y[1]], [ORG[2], hat_Y[2]]
		xs_a, ys_a, zs_a = [ORG[0], hat_Z[0]], [ORG[1], hat_Z[1]], [ORG[2], hat_Z[2]]
	else:
		tmp = args[0]
		ORG = tmp[:3,3:]
		hat_X = tmp[:3,0:1]
		hat_Y = tmp[:3,1:2]
		hat_Z = tmp[:3,2:3]
		xs_n, ys_n, zs_n = [ORG[0, 0],hat_X[0, 0]],[ORG[1, 0], hat_X[1, 0]],[ORG[2, 0], hat_X[2, 0]]
		xs_o, ys_o, zs_o = [ORG[0, 0],hat_Y[0, 0]],[ORG[1, 0], hat_Y[1, 0]],[ORG[2, 0], hat_Y[2, 0]]
		xs_a, ys_a, zs_a = [ORG[0, 0],hat_Z[0, 0]],[ORG[1, 0], hat_Z[1, 0]],[ORG[2, 0], hat_Z[2, 0]]

	n = Arrow3D(xs_n, ys_n, zs_n, mutation_scale=ms, arrowstyle=ars, color='r')
	o = Arrow3D(xs_o, ys_o, zs_o, mutation_scale=ms, arrowstyle=ars, color='g')
	a = Arrow3D(xs_a, ys_a, zs_a, mutation_scale=ms, arrowstyle=ars, color='b')
	ax.add_artist(n)
	ax.add_artist(o)
	ax.add_artist(a)

# main
AORG = np.array([0, 0, 0])
hat_X_atA = np.array([1, 0, 0])
hat_Y_atA = np.array([0, 1, 0])
hat_Z_atA = np.array([0, 0, 1])

P_atA = np.array([0.5, 0.5, 0.5])
P_atB = np.array([1, 1, 1])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

drawCoordinator(ax, AORG, hat_X_atA, hat_Y_atA, hat_Z_atA)
drawVector(ax, P_atA, P_atB, proj=True)
drawVector(ax, np.array([2,1,0]), P_atB, proj=True)

ax.set_xlim([-0.1,2.5]), ax.set_ylim([-0.1,2.5]), ax.set_zlim([-0.1,2.5])
ax.set_xlabel('X axis'), ax.set_ylabel('Y axis'), ax.set_zlabel('Z axis')
plt.show()