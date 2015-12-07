from matplotlib import pyplot as plt
import drawRobotics as dR
import numpy as np

P_atA = np.array([2.2,2.2,1.5])
BORG = np.array( [ 	[-1, 0, 0, 1],
					[0, -1, 0, 1.5],
					[0, 0, -1, 2],
					[0, 0, 0, 1]])

AORG = np.array([0,0,0])
hat_X_atA = np.array([1,0,0])
hat_Y_atA = np.array([0,1,0])
hat_Z_atA = np.array([0,0,1])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

dR.drawPointWithAxis(ax, AORG, hat_X_atA, hat_Y_atA, hat_Z_atA, pointEnable=False)
dR.drawVector(ax, AORG, P_atA, arrowstyle='-|>')
dR.drawPointWithAxis(ax, BORG)

ax.set_xlim([-0.1,2.5]), ax.set_ylim([-0.1,2.5]), ax.set_zlim([-0.1,2.5])
ax.set_xlabel('X axis'), ax.set_ylabel('Y axis'), ax.set_zlabel('Z axis')
plt.show()