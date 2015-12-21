# Introduction to Robotics 3rd Edition by Craig
# Example 2-2.
# Figure 2.8 shows a frame {B}, which is rotated relative to frame {A} about hat_Z by 30 degrees, 
# translated 10 units in hat_X_A, and translated 5 units in hat_Y_A. Find P_atA, where, P_atB = [3, 7, 0].

import matplotlib.pyplot as plt
import drawRobotics as dR
import numpy as np

P_atB = np.array([3, 7, 0, 1])

RotZ = dR.RotZ(dR.conv2Rad(30))
Dq = np.array([10,5,0])

AORG = np.array([ [1,0,0,0],
					[0,1,0,0],
					[0,0,1,0],
					[0,0,0,1]])
def_Bframe = np.r_[np.c_[RotZ, Dq], [np.array([0,0,0,1])]]

P_atA = np.dot(def_Bframe, P_atB)

print('def_Bframe = ', def_Bframe)
print('P_atA = ', P_atA)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

dR.drawPointWithAxis(ax, def_Bframe, vectorLength=3)
dR.drawPointWithAxis(ax, AORG, pointEnable=False, vectorLength=3)

dR.drawVector(ax, np.array([0,0,0]), P_atA, arrowstyle='-|>', annotationString = ' $ ^{A}P $ ')
dR.drawVector(ax, Dq, P_atA, arrowstyle='-|>', lineColor='c', proj=False, lineStyle='--')
dR.drawVector(ax, np.array([0,0,0]), Dq, arrowstyle='-|>', lineColor='c', 
				proj=False, lineStyle='--', annotationString = 'Dq')

dR.drawPointWithAxis(ax, Dq, np.array([1,0,0]), np.array([0,1,0]), np.array([0,0,1]), 
						pointEnable=False, lineStyle='--', vectorLength=3)

ax.set_xlim([-2.5,13.5]), ax.set_ylim([-1.5,14]), ax.set_zlim([-0.1,5])
ax.set_xlabel('X axis'), ax.set_ylabel('Y axis'), ax.set_zlabel('Z axis')
ax.view_init(azim=-90, elev=90)
plt.show()