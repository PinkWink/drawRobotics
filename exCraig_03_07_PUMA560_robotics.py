import sympy as sp

conv2Rad = lambda x : x*sp.pi/180

th1 = sp.Symbol('th1')
th2 = sp.Symbol('th2')
th3 = sp.Symbol('th3')
th4 = sp.Symbol('th4')
th5 = sp.Symbol('th5')
th6 = sp.Symbol('th6')

a2 = sp.Symbol('a2')
a3 = sp.Symbol('a3')

d3 = sp.Symbol('d3')
d4 = sp.Symbol('d4')

def RotZ(a):
	return sp.Matrix( [	[sp.cos(a), -sp.sin(a), 0, 0], 
						[sp.sin(a), sp.cos(a), 0, 0], 
						[0, 0, 1, 0],
						[0, 0, 0, 1] ] )

def RotX(a):
	return sp.Matrix( [	[1, 0, 0, 0], 
						[0, sp.cos(a), -sp.sin(a), 0],
						[0, sp.sin(a), sp.cos(a), 0],
						[0, 0, 0, 1] ] )

def D_q(a1,a2,a3):
	return sp.Matrix([[1,0,0,a1],[0,1,0,a2],[0,0,1,a3],[0,0,0,1]])

Trans_0to1 = RotZ(th1)
Trans_1to2 = RotX(conv2Rad(-90))*RotZ(th2)
Trans_2to3 = D_q(a2,0,0)*D_q(0,0,d3)*RotZ(th3)
Trans_3to4 = RotX(conv2Rad(-90))*D_q(a3,0,0)*D_q(0,0,d4)*RotZ(th4)
Trans_4to5 = RotX(conv2Rad(90))*RotZ(th5)
Trans_5to6 = RotX(conv2Rad(-90))*RotZ(th6)

Trans_0to2 = sp.simplify(Trans_0to1*Trans_1to2)
Trans_0to3 = sp.simplify(Trans_0to2*Trans_2to3)
Trans_0to4 = sp.simplify(Trans_0to3*Trans_3to4)
Trans_0to5 = sp.simplify(Trans_0to4*Trans_4to5)
Trans_0to6 = sp.simplify(Trans_0to5*Trans_5to6)

print('Trans_0to1 = ')
sp.pprint(Trans_0to1)
print('\n Trans_1to2 = ')
sp.pprint(Trans_1to2)
print('\n Trans_2to3 = ')
sp.pprint(Trans_2to3)
print('\n Trans_3to4 = ')
sp.pprint(Trans_3to4)
print('\n Trans_4to5 = ')
sp.pprint(Trans_4to5)
print('\n Trans_5to6 = ')
sp.pprint(Trans_5to6)

print('Trans_0to1 = ')
sp.pprint(Trans_0to1)
print('\n Trans_0to2 = ')
sp.pprint(Trans_0to2)
print('\n Trans_0to3 = ')
sp.pprint(Trans_0to3)
print('\n Trans_0to4 = ')
sp.pprint(Trans_0to4)
print('\n Trans_0to5 = ')
sp.pprint(Trans_0to5)
print('\n Trans_0to6 = ')
sp.pprint(Trans_0to6)
