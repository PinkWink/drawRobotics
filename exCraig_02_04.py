# Introduction to Robotics 3rd Edition by Craig
# Example 2-4.
# P1_atA. We wish rotate it about hat_Z by 30 degrees and 
# translate it 10 units in hat_X_A, and 5 units in hat_Y_A.
# Find P2_atA, where P1_atA = [3, 7, 0].

import matplotlib.pyplot as plt
import drawRobotics as dR
import numpy as np

P1_atA = np.array([3, 7, 0, 1])

Dq = np.array([10,5,0])

operatorT = np.r_[np.c_[dR.RotZ(dR.conv2Rad(30)), Dq], [np.array([0,0,0,1])] ]

P2_atA = np.dot(operatorT, P1_atA)

AORG = np.array([0,0,0])
hat_X_A, hat_Y_A, hat_Z_A = np.array([1,0,0]), np.array([0,1,0]), np.array([0,0,1])

print('P1_atA = ', P1_atA)
print('Dq = ', Dq)
print('operatorT = ', operatorT)
print('P2_atA = ', P2_atA)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

dR.drawPointWithAxis(ax, AORG, hat_X_A, hat_Y_A, hat_Z_A, pointEnable=False, vectorLength=3)

dR.drawVector(ax, AORG, P1_atA, arrowstyle='-|>', proj=False, annotationString=' $ ^{A}P_{1} $ ')
dR.drawVector(ax, AORG, Dq, arrowstyle='-|>', proj=False, annotationString='Dq')
dR.drawVector(ax, Dq, P2_atA, arrowstyle='-|>', proj=False)
dR.drawVector(ax, AORG, P2_atA, arrowstyle='-|>', proj=False, lineStyle='--', annotationString=' $ ^{A}P_{2} $ ')

ax.set_xlim([0,15]), ax.set_ylim([0,14]), ax.set_zlim([-0.1,5])
ax.set_xlabel('X axis'), ax.set_ylabel('Y axis'), ax.set_zlabel('Z axis')
ax.view_init(azim=-90, elev=90)
plt.show()