from exercise3 import *

''' COLORS '''
TRUNKCOL = [0.32,0.20,0.04]
LAMPCOL = p_col
LAMPCROWCOL = [0.8,0.8,0.8]
CROWNCOL = [0,0.5,0.1]
BULBCOL = YELLOW
WATER = BLUE

def TREE1(r,h,n,R,N1,N2):
	trunk = COLOR(TRUNKCOL)(CYLINDER([r,h+0.05])(n))
	crown = T(3)(h+R)(COLOR(CROWNCOL)(SPHERE(R)([N1,N2])))

	ex_framer = T([1,2])([-r*2*4.0/2,-r*2*4.0/2])(CUBOID([r*2*4,r*2*4,0.1]))
	in_framer = T([1,2])([-(r*2*4-0.03*2)/2,-(r*2*4-0.03*2)/2])(CUBOID([r*2*4-0.03*2, r*2*4-0.03*2,0.1]))
	grass = S(3)(0.2)(COLOR(CROWNCOL)(in_framer))
	frame = COLOR(SIDEWALKCOL)(DIFFERENCE([ex_framer,in_framer]))

	tree = STRUCT([trunk,crown,frame,grass])

	return tree

def LAMP(r,h,n,R,N1,N2):
	base = COLOR(LAMPCOL)(CONE([R, R*2])(n))
	trunk = COLOR(LAMPCOL)(CYLINDER([r,h])(n))
	crown = T(3)(h)(COLOR(LAMPCROWCOL)(CYLINDER([R*0.8,r*1.2])(n)))
	light = T(3)(h+R)(MATERIAL(GLASS)(SPHERE(R)([N1,N2])))
	bulb = T(3)(h+r*1.2+R*0.6/2)(COLOR(BULBCOL)(SPHERE(R*0.6)([N1,N2])))
	lamp = STRUCT([base,bulb,trunk,crown,light])

	return lamp

def ACQUARIUM(size,th):
	x,y,z = size
	base = CUBOID([x,y,z])
	hole = T([1,2,3])([th,th,0.2*z])(CUBOID([x-th*2, y-th*2, 0.8*z]))
	water = COLOR(WATER)(S(3)(0.8)(hole))
	water_surface = MATERIAL(GLASS)(T([1,2,3])([th,th,0.81*z])(CUBOID([x-th*2, y-th*2])))

	acquarium = STRUCT([DIFFERENCE([base,hole]),water,water_surface])
	return acquarium

tree = TREE1(0.10,3,25,1.5,16,16)
trees = STRUCT([T([1,2])([-13,-18]),tree] + NN(11)([T(1)(6), tree]))

lamp = LAMP(0.04,2.5,25,0.2,16,16)
lamps = STRUCT([T([1,2])([-13,-7]),lamp] + NN(11)([T(1)(6), lamp]))

acquarium = T([1,2])([35,-2-0.1])(ACQUARIUM([6,2,1.2],0.1))

graden_trees = STRUCT([T([1,2,3])([33,5,4+0.08]),tree] + NN(5)([T(1)(4), tree]))

big_tree = T([1,2,3])([29.20+0.5,20,4])(TREE1(0.20,5,25,3,16,16))

district = STRUCT([estate,trees, lamps,acquarium,graden_trees,big_tree])

VIEW(district)