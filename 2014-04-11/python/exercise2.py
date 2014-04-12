from exercise1 import *

''' COSTANTS '''
GLASS = [0.18,0.21,0.99,0.1,  0,0,0.8,0.5,  1,1,1,0.1,  1,1,1,0.1,  100]
WINDOW_COL = [0.28,0.13,0.0]
DOOR_COL = [0.60,0.28,0.0]

''' FUNCTIONS '''

def WINDOW(n, size, border, glass_thk):
	x,y,z = size

	base = CUBOID([x,y])

	hole_x = (x-(n+1.0)*border)/n
	hole_y = y-2*border
	hole = CUBOID([hole_x,hole_y])
	holes = STRUCT([hole]+NN(n-1)([T(1)(hole_x+border),hole]))
	holes = T([1,2])([border,border])(holes)

	glass = T(3)((z-glass_thk)/2)(EXTRUDE(glass_thk)(holes))
	frame = EXTRUDE(z)(DIFFERENCE([base, holes]))

	return glass,frame

def DOOR(size, border, thkness):
	x,y,z = size

	base = CUBOID([x,y])

	hole_x = (x-border*2)
	hole_y = y-border
	hole = T(1)(border)(CUBOID([hole_x,hole_y]))

	door = T(3)((z-thkness)/2)(EXTRUDE(thkness)(hole))
	frame = EXTRUDE(z)(DIFFERENCE([base, hole]))
	return door, frame

''' NORTH '''

# FACES
n1a_face = INSL(PROD)([Q(29.2), Q(0.4), Q(1.20)])
n1b_face = INSL(PROD)([QUOTE([0.40,-28.4,0.40]), Q(0.4), QUOTE([-1.20,1.40])])
n1c_face = INSL(PROD)([Q(29.2), Q(0.4), QUOTE([-2.60,1.40])])
n2a_face = INSL(PROD)([Q(29.2), Q(0.4), QUOTE([-4.0,1.20])])

# WINDOWS
glass, frame = WINDOW(2,[28.4/9,1.40, 0.40], 0.05,0.01)
glass = R([2,3])(PI/2)(glass)
frame = R([2,3])(PI/2)(frame)
na_window = STRUCT([MATERIAL(GLASS)(glass), COLOR(WINDOW_COL)(frame)])
na_windows = T([1,2,3])([0.4,0.4,1.20])(STRUCT([na_window]+NN(8)([T(1)(28.4/9),na_window])))

# DOOR HOLES

# STRUCT
na_face = STRUCT([T([2,3])([-0.80,4.0]), n1a_face, n1b_face,n1c_face,n2a_face, na_windows])
nb_face = T([2,3])([4.4,8.0])(INSL(PROD)([QUOTE([-6.24,3.44,-12.96,3.44]),Q(0.4),Q(3.2)]))
north = STRUCT([na_face,nb_face])

''' CURVED '''

domain = PROD([QUOTE([-1.2+0.4,0.40]),INTERVALS(PI/2)(20)])
quarter = MAP(CIRCLE)(domain)
curve1 = T(1)(1.2)(R([1,2])(PI)(quarter))
curve2 = T(1)(18.64)(R([1,2])(-PI/2)(quarter))
side1 = PROD([Q(0.40), Q(2.80)])
side2 = T(1)(18.64+1.2-0.4)(side1)
front_side = T([1,2])([1.2,-1.2])(PROD([Q(18.64-1.2),Q(0.40)]))

# DOOR HOLES
Td = T([1,2,3])([6.24,3.44+1.40,1.20])
Rd = COMP([R([1,2])(PI/2),R([2,3])(PI/2)])
d1_hole = Td(CUBOID([0.4,1.0,1.80]))
d1, f1 = DOOR([1.0,1.80,0.40], 0.05, 0.1)
d1 = Td(STRUCT([COLOR(DOOR_COL)(Rd(d1)), COLOR(WINDOW_COL)(Rd(f1))]))

d2_hole = T(1)(19.44)(d1_hole)
d2 = T(1)(19.44)(d1)

#STRUCT
curved = T([1,2,3])([6.24,3.44,1.20])(PROD([STRUCT([curve1,curve2,side1,side2,front_side]),Q(4.0-0.40-1.20)]))
curved = STRUCT([DIFFERENCE([curved,d1_hole,d2_hole]),d1,d2])

''' SOUTH '''

# FACES
s0a_face = INSL(PROD)([Q(29.2), Q(-0.4), Q(2.40)])
s0b_face = INSL(PROD)([QUOTE([6.24,-3.44,-12.96,-3.44,3.12]), Q(-0.4), QUOTE([-2.40,1.20])])
s0c_face = INSL(PROD)([QUOTE([6.24,-3.44,12.96,-3.44,3.12]), Q(-0.4), QUOTE([-3.60,0.40])])
s1a_face = INSL(PROD)([QUOTE([6.24,-3.44,12.96,-3.44,3.12]), Q(-0.4), Q(1.90)])
s1b_face = INSL(PROD)([QUOTE([6.24,-3.44,-12.96,-3.44,3.12]), Q(-0.4), QUOTE([-1.9,0.7])])
s1c_face = INSL(PROD)([QUOTE([6.24,-3.44,12.96,-3.44,3.12]), Q(-0.4), QUOTE([-2.60,1.40])])

# WINDOWS
glass, frame = WINDOW(4,[12.96,1.20, 0.40], 0.05, 0.01)
glass = R([2,3])(PI/2)(glass)
frame = R([2,3])(PI/2)(frame)
s0_window = STRUCT([MATERIAL(GLASS)(glass), COLOR(WINDOW_COL)(frame)])
s0_windows = T([1,3])([6.24+3.44,2.40])(s0_window)

glass, frame = WINDOW(4,[12.96,0.70, 0.40], 0.05, 0.01)
glass = R([2,3])(PI/2)(glass)
frame = R([2,3])(PI/2)(frame)
s1_window = STRUCT([MATERIAL(GLASS)(glass), COLOR(WINDOW_COL)(frame)])
s1_windows = T([1,3])([6.24+3.44,1.90])(s1_window)

# STRUCT
s0_face = [s0a_face, s0b_face, s0c_face,s0_windows]
s1_face = [s1a_face, s1b_face, s1c_face,s1_windows]
s2_face = INSL(PROD)([QUOTE([6.24,-3.44,12.96,-3.44,3.12]), Q(-0.4), Q(2.80)])
s3_face = T(2)(12.84)(INSL(PROD)([QUOTE([-6.24,3.44,-12.96,3.44,-3.12]), Q(-0.4), QUOTE([-1.20,10.0])]))
south = STRUCT([s3_face,T(2)(6.24)]+s0_face+[T(3)(4)]+s1_face+[T(3)(4),s2_face])

''' WEST '''

# FACES
w1a_face = INSL(PROD)([Q(-0.4), Q(7.04), Q(1.2)])
w1b_face = INSL(PROD)([Q(-0.4), QUOTE([2.60,-2.80,1.64]), Q(1.4)])
w1c_face = INSL(PROD)([Q(-0.4), Q(7.04), Q(2.60)])
w2_face = INSL(PROD)([Q(-0.4), Q(2.60), Q(2.0)])
wa_face = STRUCT([T(3)(4.0),w1a_face,T(3)(1.2),w1b_face, T(3)(1.4),w1c_face,T(3)(2.60),w2_face])

w01a_face = INSL(PROD)([Q(-0.4), Q(6.60), Q(6.8)])
w2_face = T(2)(-1.84)(INSL(PROD)([Q(-0.4), Q(8.44), Q(3.2)]))
wb_face = STRUCT([T(3)(1.2),w01a_face,T(3)(6.8),w2_face])

wc_face = T(1)(-16.40)(wb_face)

# WINDOWS
glass, frame = WINDOW(2,[2.8,1.40, 0.40], 0.05,0.01)
glass = R([1,2])(PI/2)(R([2,3])(PI/2)(glass))
frame = R([1,2])(PI/2)(R([2,3])(PI/2)(frame))
wa_window = STRUCT([MATERIAL(GLASS)(glass), COLOR(WINDOW_COL)(frame)])
wa_windows = T([1,2,3])([29.20-0.4,-0.80+2.60,4+1.2])(wa_window)

# DOOR HOLES
Td = T([1,2,3])([-16.40+26.08-0.4,-1.84+6.24+0.50,8.0])
Rd = COMP([R([1,2])(PI/2),R([2,3])(PI/2)])
door1_hole = Td(CUBOID([0.4,0.80,2.20]))
door1, frame1 = DOOR([0.80,2.20,0.40], 0.05, 0.05)
door1 = Td(STRUCT([COLOR(DOOR_COL)(Rd(door1)), COLOR(WINDOW_COL)(Rd(frame1))]))

#STRUCT
west = STRUCT([T([1,2])([29.20,-0.80])(wa_face), T([1,2])([26.08,6.24]), wb_face, wc_face])
west = DIFFERENCE([west, door1_hole])
west = STRUCT([west,door1, wa_windows])

''' EAST FACE '''

ea_face = T(1)(0.4)(wa_face)

e0a_face = INSL(PROD)([Q(0.4), Q(6.60), Q(2.8)])
e1a_face = INSL(PROD)([Q(0.4), Q(6.60), Q(1.2)])
e1b_face = INSL(PROD)([Q(0.4), QUOTE([-6.2,0.40]), Q(1.4)])
e1c_face = INSL(PROD)([Q(0.4), Q(6.60), Q(1.4)])
e2a_face = T(2)(-1.84)(INSL(PROD)([Q(0.4), Q(8.44), Q(1.2)]))
e2b_face = T(2)(-1.84)(INSL(PROD)([Q(0.4), QUOTE([1.84,-6.2,0.40]), Q(1.4)]))
e2c_face = T(2)(-1.84)(INSL(PROD)([Q(0.4), QUOTE([8.44]), Q(0.6)]))

#DOOR HOLES 
door2_hole = T(1)(16.40-3.44+0.4)(door1_hole)
door2 = T(1)(16.40-3.44+0.4)(door1)

# WINDOWS
e1_windows = T(1)(-29.20+0.4)(wa_windows)

glass, frame = WINDOW(2,[6.20/2,1.40, 0.40], 0.05,0.01)
glass = R([1,2])(PI/2)(R([2,3])(PI/2)(glass))
frame = R([1,2])(PI/2)(R([2,3])(PI/2)(frame))
e2_window = STRUCT([MATERIAL(GLASS)(glass), COLOR(WINDOW_COL)(frame)])
e2_windows = STRUCT([e2_window]+NN(1)([T(2)(6.20/2),e2_window]))

e3_windows = T(3)(4.0)(e2_windows)

#STRUCT
eb_face = STRUCT([T(3)(1.2),e0a_face,
	T(3)(2.8),e1a_face,T(3)(1.2),e1b_face,T(3)(1.4),e1c_face,
	T(3)(1.4),e2a_face, T(3)(1.2),e2b_face,T(3)(1.4),e2c_face])

ec_face = T(1)(16.40)(eb_face)
east = STRUCT([T(2)(-0.80)(ea_face), T([1,2])([6.24,6.24]),eb_face,ec_face])
east = DIFFERENCE([east, door2_hole])
east = STRUCT([east,door2, e1_windows, T([1,2,3])([6.24,6.24,5.2]), e2_windows, e3_windows, 
	T(1)(16.40), e2_windows, e3_windows])

''' 3D FACES '''

faces = STRUCT([north, curved, south, west,east])
weissenhof = STRUCT([floors, faces])
# VIEW(weissenhof)