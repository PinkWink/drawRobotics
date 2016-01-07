import sympy as sp

th1 = sp.Symbol('th1')
d2 = sp.Symbol('d2')
th3 = sp.Symbol('th3')
L1 = sp.Symbol('L1')
L2 = sp.Symbol('L2')

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

Trans_0to1 = D_q(0,0,L1)
Trans_1to2 = RotZ(th1)
Trans_2to3 = RotX(90*sp.pi/180) * D_q(0,0,d2)
Trans_3to4 = D_q(0,0,L2) * RotZ(th3)

Trans_0to2 = sp.simplify(Trans_0to1*Trans_1to2)
Trans_0to3 = sp.simplify(Trans_0to2*Trans_2to3)
Trans_0to4 = sp.simplify(Trans_0to3*Trans_3to4)

print('Trans_0to1 = ')
sp.pprint(Trans_0to1)
print('\n Trans_1to2 = ')
sp.pprint(Trans_1to2)
print('\n Trans_2to3 = ')
sp.pprint(Trans_2to3)
print('\n Trans_3to4 = ')
sp.pprint(Trans_3to4)

print('\n Trans_0to2 = ')
sp.pprint(Trans_0to2)
print('\n Trans_0to3 = ')
sp.pprint(Trans_0to3)
print('\n Trans_0to4 = ')
sp.pprint(Trans_0to4)