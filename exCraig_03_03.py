import matplotlib.pyplot as plt
import drawRobotics as dR
import numpy as np
from matplotlib.widgets import Slider

axcolor = 'lightgoldenrodyellow'

L1 = 1.5
L2 = 1.5

ORG_0 = np.array([[1,0,0,0],
				[0,1,0,0],
				[0,0,1,0],
				[0,0,0,1]])

def calcORGs(a1, a2, a3):
	th1 = dR.conv2Rad(a1)
	th2 = dR.conv2Rad(a2)
	th3 = dR.conv2Rad(a3)

	Trans_0to1 = np.r_[np.c_[dR.RotZ(th1), np.zeros(3)], [[0,0,0,1]]]
	Trans_1to2 = np.dot(dR.D_q(L1,0,0), np.r_[np.c_[dR.RotZ(th2), np.zeros(3)], [[0,0,0,1]]])
	Trans_2to3 = np.dot(dR.D_q(L2,0,0), np.r_[np.c_[dR.RotZ(th3), np.zeros(3)], [[0,0,0,1]]])

	Trans_0to2 = np.dot(Trans_0to1, Trans_1to2)
	Trans_0to3 = np.dot(Trans_0to2, Trans_2to3)

	ORG_1 = np.dot(Trans_0to1, ORG_0)
	ORG_2 = np.dot(Trans_0to2, ORG_0)
	ORG_3 = np.dot(Trans_0to3, ORG_0)

	return ORG_1, ORG_2, ORG_3

ORG_1, ORG_2, ORG_3 = calcORGs(0,0,0)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(bottom=0.25)

th1Angle = plt.axes([0.125, 0.16, 0.77, 0.03], axisbg=axcolor)
th2Angle = plt.axes([0.125, 0.10, 0.77, 0.03], axisbg=axcolor)
th3Angle = plt.axes([0.125, 0.04, 0.77, 0.03], axisbg=axcolor)

s1Angle = Slider(th1Angle, r'$ \theta_1 $', -90.0, 90.0, valinit=0)
s2Angle = Slider(th2Angle, r'$ \theta_2 $', -90.0, 90.0, valinit=0)
s3Angle = Slider(th3Angle, r'$ \theta_3 $', -90.0, 90.0, valinit=0)

dR.drawPointWithAxis(ax, ORG_0, lineStyle='--', vectorLength=1)
dR.drawPointWithAxis(ax, ORG_1, vectorLength=1)
dR.drawVector(ax, ORG_1, ORG_2, arrowstyle='-', lineColor='k', proj=False, lineWidth=3)
dR.drawPointWithAxis(ax, ORG_2, vectorLength=1)
dR.drawVector(ax, ORG_2, ORG_3, arrowstyle='-', lineColor='k', proj=False, lineWidth=3)
dR.drawPointWithAxis(ax, ORG_3, vectorLength=1)

def update(val):
	th1 = s1Angle.val
	th2 = s2Angle.val
	th3 = s3Angle.val

	ORG_1, ORG_2, ORG_3 = calcORGs(th1, th2, th3)

	ax.cla()

	dR.drawPointWithAxis(ax, ORG_0, lineStyle='--', vectorLength=1)
	dR.drawPointWithAxis(ax, ORG_1, vectorLength=1)
	dR.drawVector(ax, ORG_1, ORG_2, arrowstyle='-', lineColor='k', proj=False, lineWidth=3)
	dR.drawPointWithAxis(ax, ORG_2, vectorLength=1)
	dR.drawVector(ax, ORG_2, ORG_3, arrowstyle='-', lineColor='k', proj=False, lineWidth=3)
	dR.drawPointWithAxis(ax, ORG_3, vectorLength=1)

	ax.set_xlim([-4,4]), ax.set_ylim([-4,4]), ax.set_zlim([-3,3])
	ax.set_xlabel('X axis'), ax.set_ylabel('Y axis'), ax.set_zlabel('Z axis')

s1Angle.on_changed(update)
s2Angle.on_changed(update)
s3Angle.on_changed(update)

ax.set_xlim([-4,4]), ax.set_ylim([-4,4]), ax.set_zlim([-3,3])
ax.set_xlabel('X axis'), ax.set_ylabel('Y axis'), ax.set_zlabel('Z axis')
ax.view_init(azim=-90, elev=90)
plt.show()