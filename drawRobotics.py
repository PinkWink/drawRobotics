from matplotlib import pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
import numpy as np

conv2Rad = lambda x : x*np.pi/180

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
	pointEnable = kwargs.get('pointEnable', True)
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

	if pointEnable: fig.scatter(xs[1], ys[1], zs[1], color='k', s=50)
	if projOn==True:
		fig.plot(xs, ys, [0, 0], color=pc, linestyle='--')
		fig.plot([xs[0], xs[0]], [ys[0], ys[0]], [0, zs[0]], color=pc, linestyle='--')
		fig.plot([xs[1], xs[1]], [ys[1], ys[1]], [0, zs[1]], color=pc, linestyle='--')
		
def drawPointWithAxis(fig, *args, **kwargs):
	ms = kwargs.get('mutation_scale', 20)
	ars = kwargs.get('arrowstyle', '->')
	pointEnable = kwargs.get('pointEnable', True)
	axisEnable = kwargs.get('axisEnable', True)

	if len(args) == 4:
		ORG = args[0]
		hat_X = args[1]
		hat_Y = args[2]
		hat_Z = args[3]
		xs_n = [ORG[0], ORG[0] + hat_X[0]]
		ys_n = [ORG[1], ORG[1] + hat_X[1]]
		zs_n = [ORG[2], ORG[2] + hat_X[2]]
		xs_o = [ORG[0], ORG[0] + hat_Y[0]]
		ys_o = [ORG[1], ORG[1] + hat_Y[1]]
		zs_o = [ORG[2], ORG[2] + hat_Y[2]]
		xs_a = [ORG[0], ORG[0] + hat_Z[0]]
		ys_a = [ORG[1], ORG[1] + hat_Z[1]]
		zs_a = [ORG[2], ORG[2] + hat_Z[2]]
	else:
		tmp = args[0]
		ORG = tmp[:3,3:]
		hat_X = tmp[:3,0:1]
		hat_Y = tmp[:3,1:2]
		hat_Z = tmp[:3,2:3]
		xs_n = [ORG[0, 0], ORG[0, 0] + hat_X[0, 0]]
		ys_n = [ORG[1, 0], ORG[1, 0] + hat_X[1, 0]]
		zs_n = [ORG[2, 0], ORG[2, 0] + hat_X[2, 0]]
		xs_o = [ORG[0, 0], ORG[0, 0] + hat_Y[0, 0]]
		ys_o = [ORG[1, 0], ORG[1, 0] + hat_Y[1, 0]]
		zs_o = [ORG[2, 0], ORG[2, 0] + hat_Y[2, 0]]
		xs_a = [ORG[0, 0], ORG[0, 0] + hat_Z[0, 0]]
		ys_a = [ORG[1, 0], ORG[1, 0] + hat_Z[1, 0]]
		zs_a = [ORG[2, 0], ORG[2, 0] + hat_Z[2, 0]]

	if pointEnable: fig.scatter(xs_n[0], ys_n[0], zs_n[0], color='k', s=50)

	if axisEnable:
		n = Arrow3D(xs_n, ys_n, zs_n, mutation_scale=ms, arrowstyle=ars, color='r')
		o = Arrow3D(xs_o, ys_o, zs_o, mutation_scale=ms, arrowstyle=ars, color='g')
		a = Arrow3D(xs_a, ys_a, zs_a, mutation_scale=ms, arrowstyle=ars, color='b')
		fig.add_artist(n)
		fig.add_artist(o)
		fig.add_artist(a)

def RotX(phi):
    return np.array([[1, 0, 			0],
                     [0, np.cos(phi), 	-np.sin(phi)],
                     [0, np.sin(phi), 	np.cos(phi)]])

def RotY(theta):
    return np.array([[np.cos(theta), 	0, np.sin(theta)],
                     [0, 				1, 0],
                     [-np.sin(theta), 	0, np.cos(theta)]])

def RotZ(psi):
    return np.array([[np.cos(psi), 	-np.sin(psi), 	0],
                     [np.sin(psi), 	np.cos(psi), 	0],
                     [0, 			0, 				1]])
