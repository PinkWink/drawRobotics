# Introduction to Robotics 3rd Edition by Craig
# Example 2-1.
# Figure 2.6 shows a frame {B} that is rotated relative to frame {A} about Z by 30 degrees.

from matplotlib import pyplot as plt
import drawRobotics as dR
import numpy as np

P_atB = np.array([0,2,0])

Rot_AtoB = dR.RotZ(dR.conv2Rad(30))

P_atA = np.dot(Rot_AtoB, P_atB)

print('P_atB = ', P_atB)
print('Rot_AtoB = ', Rot_AtoB)
print('P_atA = Rot_AtoB * P_atA = ', P_atA)

AORG = np.array([0,0,0])
hat_X_atA = np.array([1,0,0])
hat_Y_atA = np.array([0,1,0])
hat_Z_atA = np.array([0,0,1])

BORG = np.dot(Rot_AtoB, AORG)
hat_X_atB = np.dot(Rot_AtoB, hat_X_atA)
hat_Y_atB = np.dot(Rot_AtoB, hat_Y_atA)
hat_Z_atB = np.dot(Rot_AtoB, hat_Z_atA)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

dR.drawPointWithAxis(ax, AORG, hat_X_atA, hat_Y_atA, hat_Z_atA, pointEnable=False)
dR.drawPointWithAxis(ax, BORG, hat_X_atB, hat_Y_atB, hat_Z_atB, pointEnable=False, lineStyle='--')
dR.drawVector(ax, AORG, P_atA, arrowstyle='-|>', annotationString=' $ ^{A}P $ ')

ax.set_xlim([-1.5,1.5]), ax.set_ylim([-0.1,2]), ax.set_zlim([-0.1,1.5])
ax.set_xlabel('X axis'), ax.set_ylabel('Y axis'), ax.set_zlabel('Z axis')
ax.view_init(azim=-90, elev=90)
plt.show()