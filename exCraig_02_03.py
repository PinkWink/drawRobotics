# Introduction to Robotics 3rd Edition by Craig
# Example 2-3.
# There is a vector P1_atA. 
# We wish to compute the vector obtained by rotating this vector about hat_Z by 30 degrees.
# Call the new vector P2_atA.

import matplotlib.pyplot as plt
import drawRobotics as dR
import numpy as np

P1_atA = np.array([0, 2, 0])

AORG = np.array([0, 0, 0])
hat_X_A, hat_Y_A, hat_Z_A = np.array([1,0,0]), np.array([0,1,0]), np.array([0,0,1])

RotZ = dR.RotZ(dR.conv2Rad(30))

P2_atA = np.dot(RotZ, P1_atA)

print('P1_atA = ', P1_atA)
print('RotZ = ', RotZ)
print('P2_atA = ', P2_atA)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

dR.drawPointWithAxis(ax, AORG, hat_X_A, hat_Y_A, hat_Z_A, pointEnable=False)

dR.drawVector(ax, AORG, P2_atA, arrowstyle='-|>', proj=False, annotationString=' $ ^{A}P_{2} $ ')
dR.drawVector(ax, AORG, P1_atA, arrowstyle='-|>', lineColor='c', proj=False, lineStyle='--', 
																annotationString=' $ ^{A}P_{1} $ ')

ax.set_xlim([-2,2]), ax.set_ylim([-1,3]), ax.set_zlim([-0.1,5])
ax.set_xlabel('X axis'), ax.set_ylabel('Y axis'), ax.set_zlabel('Z axis')
ax.view_init(azim=-90, elev=90)
plt.show()