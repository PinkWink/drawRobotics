import matplotlib.pyplot as plt
import drawRobotics as dR
import numpy as np
from matplotlib.widgets import Slider

axcolor = 'lightgoldenrodyellow'

L1 = 0.5
L2 = 0.2

th1Init = 0
th3Init = 0
d2Init = 1

ORG_0 = np.array([[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]])

def calcORGs(a1, a2, a3):
	th1 = dR.conv2Rad(a1)
	d2 = a2
	th3 = dR.conv2Rad(a3)

	Trans_0to1 = dR.D_q(0,0,L1)
	Trans_1to2 = np.r_[np.c_[dR.RotZ(th1), np.zeros(3)], [[0,0,0,1]]]
	Trans_2to3 = np.dot( np.r_[np.c_[dR.RotX(dR.conv2Rad(90)), np.zeros(3)], [[0,0,0,1]]], dR.D_q(0,0,d2) )
	Trans_3to4 = np.dot( dR.D_q(0,0,L2), np.r_[np.c_[dR.RotZ(th3), np.zeros(3)], [[0,0,0,1]]] )

	Trans_0to2 = np.dot(Trans_0to1, Trans_1to2)
	Trans_0to3 = np.dot(Trans_0to2, Trans_2to3)
	Trans_0to4 = np.dot(Trans_0to3, Trans_3to4)

	ORG_1 = np.dot(Trans_0to1, ORG_0)
	ORG_2 = np.dot(Trans_0to2, ORG_0)
	ORG_3 = np.dot(Trans_0to3, ORG_0)
	ORG_4 = np.dot(Trans_0to4, ORG_0)

	return ORG_1, ORG_2, ORG_3, ORG_4

def drawObject(ORG_1, ORG_2, ORG_3, ORG_4):
	dR.drawPointWithAxis(ax, ORG_0, lineStyle='--', vectorLength=1, lineWidth=2)
	dR.drawPointWithAxis(ax, ORG_1, vectorLength=0.5)
	dR.drawPointWithAxis(ax, ORG_2, vectorLength=0.5)
	dR.drawPointWithAxis(ax, ORG_3, vectorLength=0.5)
	dR.drawPointWithAxis(ax, ORG_4, vectorLength=0.5, lineWidth=2)

	dR.drawVector(ax, ORG_0, ORG_1, arrowstyle='-', lineColor='c', proj=False, lineWidth=10)
	dR.drawVector(ax, ORG_1, ORG_2, arrowstyle='-', lineColor='k', proj=False, lineWidth=8)
	dR.drawVector(ax, ORG_2, ORG_3, arrowstyle='-', lineColor='k', proj=False, lineWidth=4)
	dR.drawVector(ax, ORG_3, ORG_4, arrowstyle='-', lineColor='k', proj=False, lineWidth=2)

	ax.set_xlim([-2,3]), ax.set_ylim([-2,3]), ax.set_zlim([-0.1,2])
	ax.set_xlabel('X axis'), ax.set_ylabel('Y axis'), ax.set_zlabel('Z axis')

def update(val):
	th1 = s1Angle.val
	d2 = s2Length.val
	th3 = s3Angle.val

	ORG_1, ORG_2, ORG_3, ORG_4 = calcORGs(th1, d2, th3)

	ax.cla()

	drawObject(ORG_1, ORG_2, ORG_3, ORG_4)
	
ORG_1, ORG_2, ORG_3, ORG_4 = calcORGs(th1Init, d2Init, th3Init)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(bottom=0.25)

th1Angle = plt.axes([0.125, 0.16, 0.77, 0.03], axisbg=axcolor)
d2Length = plt.axes([0.125, 0.10, 0.77, 0.03], axisbg=axcolor)
th3Angle = plt.axes([0.125, 0.04, 0.77, 0.03], axisbg=axcolor)

s1Angle = Slider(th1Angle, r'$ \theta_1 $', -180.0, 180.0, valinit=th1Init)
s2Length = Slider(d2Length, r'$ d_2 $', 0.5, 2.0, valinit=d2Init)
s3Angle = Slider(th3Angle, r'$ \theta_3 $', -180.0, 180.0, valinit=th3Init)

drawObject(ORG_1, ORG_2, ORG_3, ORG_4)
	
s1Angle.on_changed(update)
s2Length.on_changed(update)
s3Angle.on_changed(update)

ax.view_init(azim=-150, elev=30)
plt.show()