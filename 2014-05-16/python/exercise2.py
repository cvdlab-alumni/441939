from exercise1 import *

''' CONSTANTS '''

n = 4
door_w = 1.60
door_h = 2.50
hh = 1.0
light_blue = [0.62,0.73, 0.92]
light_gray = [0.85,0.85,0.85]
grass_green = [0,0.7,0.1]
trunk_brown = [0.32,0.20,0.04]
crown_green = [0,0.5,0.1]
light_red = [0.8,0.34,0.09]

''' FUNCTIONS '''

# From homework1 exercise 4
def ramp(w,l,h,n,raiser=0.2):
	unit = MKPOL([[[0,0],[0,raiser+h],[l,h],[l,raiser+h]],[[1,2,3,4]],None])
	unit = MAP([S1,S3,S2])(PROD([unit,Q(w)]))
	ramp = STRUCT(NN(n)([unit,T([1,3])([l,h])]))
	return ramp

def makeStruct(struct):
	return STRUCT(CAT(AA(MKPOLS)(evalStruct(struct))))

def step(w,p):
	controls = [[0.0,0.0],[0.0,-p],[w/2.0,-p],[w,-p],[w,0.0]]
	knots = [0,0,0,1,2,3,3,3]
	spline = BSPLINE(2)(knots)(controls)
	V,FV = larMap(spline)(larDom(knots))
	return V, [range(len(V))]

# With larcc
def curved_ramp(w1,w2,p1,p2,h,N):
	h_step = h/(N+0.0)
	p_step = (p1-p2)/(N+0.0)
	w_step = (w1-w2)/2.0/(N+0.0)

	w,p = w1, p1
	assembly = []
	for i in range(N):
		single_step = larModelProduct([step(w,p),larIntervals([1])([h_step])])
		w -= w_step*2.0
		p -= p_step
		assembly += [single_step, t(w_step,0,h_step)]

	return Struct(assembly)

def rotationalSurface(profile):
   def rotationalSurface0(point):
      u,v = point
      x,y,z = profile([u])
      return [COS(v)*x,SIN(v)*x,z]
   return rotationalSurface0

def hill(R,h):
	controls = [[R,0.0,0.0],[4*R/5.0,0.0,0.0],[R/2.0,0.0,h],[0.0,0.0,h]]
	profile = larBezierCurve(controls)
	surface = rotationalSurface(profile)
	return larMap(surface)(larIntervals([32,48])([1,2*PI]))

# From homework2 (exercise4)
def TREE1(r,h,n,R,N1,N2):
	trunk = COLOR(trunk_brown)(CYLINDER([r,h+0.05])(n))
	crown = T(3)(h+R)(COLOR(crown_green)(SPHERE(R)([N1,N2])))

	ex_framer = T([1,2])([-r*2*4.0/2,-r*2*4.0/2])(CUBOID([r*2*4,r*2*4,0.1]))
	in_framer = T([1,2])([-(r*2*4-0.03*2)/2,-(r*2*4-0.03*2)/2])(CUBOID([r*2*4-0.03*2, r*2*4-0.03*2,0.1]))
	grass = S(3)(0.2)(COLOR(crown_green)(in_framer))
	frame = DIFFERENCE([ex_framer,in_framer])

	tree = STRUCT([trunk,crown,frame,grass])

	return tree

''' Creating side A, side B and che building diagram (as master) '''

apartmentA = master
apartmentB = larApply(s(-1,1,1))(apartmentA)

master = assemblyDiagramInit([3,1,n+1+1])([
	[7.7, 2, 7.7],[7.6],[hh] + [3.7]*n + [fl_h*2]])

''' SIDE A '''

master = diagram2cell(apartmentA,master,13)
master = diagram2cell(apartmentA,master,13)
master = diagram2cell(apartmentA,master,13)
master = diagram2cell(apartmentA,master,13)

''' SIDE B'''

master = diagram2cell(apartmentB,master,1)
master = diagram2cell(apartmentB,master,1)
master = diagram2cell(apartmentB,master,1)
master = diagram2cell(apartmentB,master,1)

''' LANDING '''

# Window
window = window(window_w,window_h1,window_h2,out1_wall,h)
landing_window = assemblyDiagramInit([3,1,1])([
	[0.5,window_w,0.5],[out1_wall],[h]])
landing_window = diagram2cell(window,landing_window,1)
landing_window = removeCells([3], landing_window)

# Main door
main_door = door(door_w,door_h,out2_wall,h)
landing_door = assemblyDiagramInit([3,1,1])([
	[0.2,door_w,0.2],[out1_wall],[h]])
landing_door = diagram2cell(main_door,landing_door,1)
landing_door = removeCells([2], landing_door)

# Landing type 1
landing = assemblyDiagramInit([1,5,2])([
	[2.0],[out1_wall,1.8,3.5,1.8,out1_wall],[fl_h,h]])
inter_landing =  assemblyDiagramInit([1,1,3])([
	[2.0],[1.80],[1.55,fl_h,1.55]])
landing = diagram2cell(landing_window,landing,9)
landing = diagram2cell(inter_landing,landing,3)
landing = removeCells([14,12,4,6,2,3], landing)

# Top landing
top_landing = assemblyDiagramInit([1,5,2])([
	[2.0],[out1_wall,1.8,3.5,1.8,out1_wall],[fl_h,h]])
top_landing = diagram2cell(landing_window,top_landing,1)
top_landing = diagram2cell(landing_window,top_landing,8)
top_hole = assemblyDiagramInit([2,2,1])([
	[1.0,1.0],[2.0,2.0],[fl_h]])
top_landing = diagram2cell(top_hole,top_landing,3)
top_landing = removeCells([2,3,5,15,18,17,1], top_landing)

# Ground landing (with main door)
ground_landing = assemblyDiagramInit([1,5,2])([
	[2.0],[out1_wall,1.8,3.5,1.8,out1_wall],[fl_h,h]])
ground_landing = diagram2cell(landing_door,ground_landing,9)
ground_landing = diagram2cell(inter_landing,ground_landing,3)
ground_landing = removeCells([13,4,6], ground_landing)

master = diagram2cell(ground_landing,master,3)
master = diagram2cell(landing,master,3)
master = diagram2cell(landing,master,3)
master = diagram2cell(top_landing,master,3)

''' External decorations '''

external_ramp = curved_ramp(4,2,2,1,1+fl_h,8)
land = CUBOID([40,40,-0.5])
hill = hill(5,2.5)
tree = TREE1(0.10,3,25,1.2,16,16)
trees = STRUCT(NN(4)([T(1)(4),tree]))
sidewalk = CUBOID([2.0,-20,0.1625])
top = CUBOID([7.7+2+7.7+0.5,7.6+0.5,0.8])

# APPLE
controls = [[0,0,2],[11.4,0,3.5],[19.4,0,-12.1],
            [46.4,0,-8.2],[60,0,35],[57.6,0,51.7],
            [37.8,0,82],[10.1,0,76.8],[0,0,60]]
profile = larBezierCurve(controls)
apple = larMap(rotationalSurface(profile))(larIntervals([32,48])([1,2*PI]))
apple = larApply(s(0.05,0.05,0.05))(apple)

''' Orientation '''

master = larApply(s(1,-1,1))(master)
master = larApply(t(0,7.6,0))(master)

''' VIEWS '''

# Landing
# VIEW(draw(landing))
# VIEW(addCellNumbers(landing,RED))

# Top landing
# VIEW(draw(top_landing))
# VIEW(addCellNumbers(top_landing,RED))

# Ground landing
# VIEW(draw(ground_landing))
# VIEW(addCellNumbers(ground_landing,RED))

# Landing block
landing_block = assemblyDiagramInit([1,1,n])([
	[2],[7.6],[3.7]*n])
landing_block = diagram2cell(ground_landing,landing_block,0)
landing_block = diagram2cell(landing,landing_block,0)
landing_block = diagram2cell(landing,landing_block,0)
landing_block = diagram2cell(top_landing,landing_block,0)
landing_block = larApply(s(1,-1,1))(landing_block)
landing_block = larApply(t(7.7,7.6,0))(landing_block)
# VIEW(draw(landing_block))
# VIEW(addCellNumbers(landing_block,RED))

# Ramps in PYPLASM
# ramp(w,l,h,n,raiser=0.2):
ramp = ramp(1.0,0.4,0.20555556,9,0.3)
ramp1 = T([1,2])([1.0+7.7,1.8+0.25])(R([1,2])(PI/2)(ramp))
ramps1 = STRUCT([ramp1]+[T(3)(3.7),ramp1]*2)
ramp2 = T([1,2,3])([1.0+7.7,1.8*2+1.85+0.1,1.55+0.3])(R([1,2])(-PI/2)(ramp))
ramps2 = STRUCT([ramp2]+[T(3)(3.7),ramp2]*2)
ramps = [ramps1,ramps2]
# VIEW(STRUCT(ramps + [draw(landing_block)]))

# Decorations
# VIEW(makeStruct(external_ramp))

# Complete building
ramps = T(3)(hh)(STRUCT(ramps))
external_ramp = T(1)(7.7-1.0)(makeStruct(external_ramp))
land = T([1,2])([-10,-20])(land)
hill = T([1,2])([20,-10])(draw(hill))
trees1 = T(1)(7.7-0.4)(R([1,2])(-PI/2)(trees))
trees2 = T(1)(2.0+0.4*2)(trees1)
tree = T([1,2,3])([20,-10,2.5-0.5])(tree)
sidewalk = T(1)(7.7)(sidewalk)
top = T([1,2,3])([-0.25,-0.25,3.7*4+1.0+fl_h*2])(top)
apple = T([1,2,3])([8.7,3.80,3.7*4+1.0+fl_h*2+0.5])(draw(apple))

building = STRUCT([
	COLOR(RED)(apple),      # roof decoration
	draw(master),
	COLOR(light_blue)(ramps),
	COLOR(light_gray)(external_ramp),
	COLOR(grass_green)(land),
	COLOR(grass_green)(hill),
	trees1, trees2, tree,sidewalk,
	COLOR(light_red)(top)
	])
VIEW(building)
VIEW(addCellNumbers(master,RED))