import matplotlib.pyplot as plt
import drawRobotics as dR
import numpy as np
from matplotlib.widgets import Slider

axcolor = 'lightgoldenrodyellow'

th1Init, th2Init, th3Init, th4Init, th5Init, th6Init = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

a2 = 1.5
a3 = 0.5
d3 = 0.5
d4 = 1.5

ORG_Base = np.array([[1,0,0,0], [0,1,0,0], [0,0,1,-2], [0,0,0,1]])
ORG_0 = np.array([[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]])

def RotZ(a):
	return np.array( [	[np.cos(a), -np.sin(a), 0, 0], 
						[np.sin(a), np.cos(a), 0, 0], 
						[0, 0, 1, 0],
						[0, 0, 0, 1] ] )

def RotX(a):
	return np.array( [	[1, 0, 0, 0], 
						[0, np.cos(a), -np.sin(a), 0],
						[0, np.sin(a), np.cos(a), 0],
						[0, 0, 0, 1] ] )

def D_q(dq1,dq2,dq3):
	return np.array([[1,0,0,dq1],[0,1,0,dq2],[0,0,1,dq3],[0,0,0,1]])


def calcORGs(q1, q2, q3, q4, q5, q6):
	th1 = dR.conv2Rad(q1)
	th2 = dR.conv2Rad(q2)
	th3 = dR.conv2Rad(q3)
	th4 = dR.conv2Rad(q4)
	th5 = dR.conv2Rad(q5)
	th6 = dR.conv2Rad(q6)

	Trans_0to1 = RotZ(th1)
	Trans_1to2 = np.dot(RotX(dR.conv2Rad(-90)), RotZ(th2))
	Trans_2to3 = np.dot(np.dot(D_q(a2,0,0), D_q(0,0,d3)), RotZ(th3))
	Trans_3to4 = np.dot(np.dot(np.dot(RotX(dR.conv2Rad(-90)), D_q(a3,0,0)), D_q(0,0,d4)), RotZ(th4))
	Trans_4to5 = np.dot(RotX(dR.conv2Rad(90)), RotZ(th5))
	Trans_5to6 = np.dot(RotX(dR.conv2Rad(-90)), RotZ(th6))

	Trans_0to2 = np.dot(Trans_0to1, Trans_1to2)
	Trans_0to3 = np.dot(Trans_0to2, Trans_2to3)
	Trans_0to4 = np.dot(Trans_0to3, Trans_3to4)
	Trans_0to5 = np.dot(Trans_0to4, Trans_4to5)
	Trans_0to6 = np.dot(Trans_0to5, Trans_5to6)

	ORG_1 = np.dot(Trans_0to1, ORG_0)
	ORG_2 = np.dot(Trans_0to2, ORG_0)
	ORG_3 = np.dot(Trans_0to3, ORG_0)
	ORG_4 = np.dot(Trans_0to4, ORG_0)
	ORG_5 = np.dot(Trans_0to5, ORG_0)
	ORG_6 = np.dot(Trans_0to6, ORG_0)

	return ORG_1, ORG_2, ORG_3, ORG_4, ORG_5, ORG_6

def drawObject(ORG_1, ORG_2, ORG_3, ORG_4, ORG_5, ORG_6):
	dR.drawPointWithAxis(ax, ORG_0, lineStyle='--', vectorLength=1, lineWidth=2)
	dR.drawPointWithAxis(ax, ORG_1, vectorLength=0.5)
	dR.drawPointWithAxis(ax, ORG_2, vectorLength=0.5)
	dR.drawPointWithAxis(ax, ORG_3, vectorLength=0.5)
	dR.drawPointWithAxis(ax, ORG_4, vectorLength=0.5)
	dR.drawPointWithAxis(ax, ORG_5, vectorLength=0.5)
	dR.drawPointWithAxis(ax, ORG_6, vectorLength=0.5)

	dR.drawVector(ax, ORG_Base, ORG_0, arrowstyle='-', lineColor='c', proj=False, lineWidth=5)
	dR.drawVector(ax, ORG_0, ORG_1, arrowstyle='-', lineColor='k', proj=False, lineWidth=3)
	dR.drawVector(ax, ORG_1, ORG_2, arrowstyle='-', lineColor='k', proj=False, lineWidth=3)
	dR.drawVector(ax, ORG_2, ORG_3, arrowstyle='-', lineColor='k', proj=False, lineWidth=3)
	dR.drawVector(ax, ORG_3, ORG_4, arrowstyle='-', lineColor='k', proj=False, lineWidth=3)
	dR.drawVector(ax, ORG_4, ORG_5, arrowstyle='-', lineColor='k', proj=False, lineWidth=3)
	dR.drawVector(ax, ORG_5, ORG_6, arrowstyle='-', lineColor='k', proj=False, lineWidth=3)

	ax.set_xlim([-2,3]), ax.set_ylim([-2,3]), ax.set_zlim([-2,2])
	ax.set_xlabel('X axis'), ax.set_ylabel('Y axis'), ax.set_zlabel('Z axis')

def update(val):
	th1 = s1Angle.val
	th2 = s2Angle.val
	th3 = s3Angle.val
	th4 = s4Angle.val
	th5 = s5Angle.val
	th6 = s6Angle.val

	ORG_1, ORG_2, ORG_3, ORG_4, ORG_5, ORG_6 = calcORGs(th1, th2, th3, th4, th5, th6)

	ax.cla()

	drawObject(ORG_1, ORG_2, ORG_3, ORG_4, ORG_5, ORG_6)
	
ORG_1, ORG_2, ORG_3, ORG_4, ORG_5, ORG_6 = calcORGs(th1Init, th2Init, th3Init, th4Init, th5Init, th6Init)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(bottom=0.25)

th1Angle = plt.axes([0.125, 0.16, 0.34, 0.03], axisbg=axcolor)
th2Angle = plt.axes([0.125, 0.10, 0.34, 0.03], axisbg=axcolor)
th3Angle = plt.axes([0.125, 0.04, 0.34, 0.03], axisbg=axcolor)
th4Angle = plt.axes([0.55, 0.16, 0.34, 0.03], axisbg=axcolor)
th5Angle = plt.axes([0.55, 0.10, 0.34, 0.03], axisbg=axcolor)
th6Angle = plt.axes([0.55, 0.04, 0.34, 0.03], axisbg=axcolor)

s1Angle = Slider(th1Angle, r'$ \theta_1 $', -180.0, 180.0, valinit=th1Init)
s2Angle = Slider(th2Angle, r'$ \theta_2 $', -180.0, 180.0, valinit=th2Init)
s3Angle = Slider(th3Angle, r'$ \theta_3 $', -180.0, 180.0, valinit=th3Init)
s4Angle = Slider(th4Angle, r'$ \theta_4 $', -180.0, 180.0, valinit=th4Init)
s5Angle = Slider(th5Angle, r'$ \theta_5 $', -180.0, 180.0, valinit=th5Init)
s6Angle = Slider(th6Angle, r'$ \theta_6 $', -180.0, 180.0, valinit=th6Init)

drawObject(ORG_1, ORG_2, ORG_3, ORG_4, ORG_5, ORG_6)

s1Angle.on_changed(update)
s2Angle.on_changed(update)
s3Angle.on_changed(update)
s4Angle.on_changed(update)
s5Angle.on_changed(update)
s6Angle.on_changed(update)

ax.view_init(azim=-150, elev=30)
plt.show()