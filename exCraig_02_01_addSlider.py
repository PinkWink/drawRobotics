# Introduction to Robotics 3rd Edition by Craig
# Example 2-1.
# Figure 2.6 shows a frame {B} that is rotated relative to frame {A} about Z by 30 degrees.

import matplotlib.pyplot as plt
import drawRobotics as dR
import numpy as np
from matplotlib.widgets import Slider

axcolor = 'lightgoldenrodyellow'
initAngle = 30

P_atB = np.array([0,2,0])

AORG = np.array([0,0,0])
hat_X_atA = np.array([1,0,0])
hat_Y_atA = np.array([0,1,0])
hat_Z_atA = np.array([0,0,1])

def calcBCoordi(rotAngle, ORG, hat_X, hat_Y, hat_Z):
	Rot_AtoB = dR.RotZ(dR.conv2Rad(rotAngle))
	
	P_atA = np.dot(Rot_AtoB, P_atB)
	
	BORG = np.dot(Rot_AtoB, AORG)
	hat_X_atB = np.dot(Rot_AtoB, hat_X)
	hat_Y_atB = np.dot(Rot_AtoB, hat_Y)
	hat_Z_atB = np.dot(Rot_AtoB, hat_Z)

	return BORG, hat_X_atB, hat_Y_atB, hat_Z_atB, P_atA

BORG, hat_X_atB, hat_Y_atB, hat_Z_atB, P_atA = calcBCoordi(initAngle, AORG, hat_X_atA, hat_Y_atA, hat_Z_atA)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(bottom=0.25)

axAngle = plt.axes([0.125, 0.15, 0.77, 0.03], facecolor=axcolor)
sAngle = Slider(axAngle, 'Angle', -90.0, 90.0, valinit=initAngle)

dR.drawPointWithAxis(ax, AORG, hat_X_atA, hat_Y_atA, hat_Z_atA, pointEnable=False)
dR.drawPointWithAxis(ax, BORG, hat_X_atB, hat_Y_atB, hat_Z_atB, pointEnable=False, lineStyle='--')
dR.drawVector(ax, AORG, P_atA, arrowstyle='-|>', annotationString=' $ ^{A}P $ ')

def update(val):
	updateAngle = sAngle.val

	BORG, hat_X_atB, hat_Y_atB, hat_Z_atB, P_atA = calcBCoordi(updateAngle, AORG, hat_X_atA, hat_Y_atA, hat_Z_atA)

	ax.cla()
	dR.drawPointWithAxis(ax, AORG, hat_X_atA, hat_Y_atA, hat_Z_atA, pointEnable=False)
	dR.drawPointWithAxis(ax, BORG, hat_X_atB, hat_Y_atB, hat_Z_atB, pointEnable=False, lineStyle='--')
	dR.drawVector(ax, AORG, P_atA, arrowstyle='-|>', annotationString=' $ ^{A}P $ ')

	ax.set_xlim([-2,2]), ax.set_ylim([-1,2]), ax.set_zlim([-2,2])

sAngle.on_changed(update)

ax.set_xlim([-2,2]), ax.set_ylim([-1,2]), ax.set_zlim([-2,2])
ax.set_xlabel('X axis'), ax.set_ylabel('Y axis'), ax.set_zlabel('Z axis')
ax.view_init(azim=-90, elev=90)
plt.show()