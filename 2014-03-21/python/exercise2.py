from exercise1 import *

# North face

n1a_face = INSL(PROD)([Q(29.2), Q(0), Q(1.20)])
n1b_face = INSL(PROD)([QUOTE([0.40,-28.4,0.40]), Q(0), QUOTE([-1.20,1.40])])
n1c_face = INSL(PROD)([Q(29.2), Q(0), QUOTE([-2.60,1.40])])
n2a_face = INSL(PROD)([Q(29.2), Q(0), QUOTE([-4.0,1.20])])
na_face = STRUCT([T([2,3])([-0.80,4.0]), n1a_face, n1b_face,n1c_face,n2a_face])

nb_face = T([2,3])([4.4,8.0])(INSL(PROD)([QUOTE([-6.24,3.44,-12.96,3.44]),Q(0),Q(3.2)]))

domain = PROD([MK([1.2]),INTERVALS(PI/2)(20)])
quarter = MAP(circle)(domain)
curve1 = T(1)(1.2)(R([1,2])(PI)(quarter))
curve2 = T(1)(18.64)(R([1,2])(-PI/2)(quarter))
side1 = PROD([Q(0), Q(2.80)])
side2 = T(1)(18.64+1.2)(side1)
front_side = T([1,2])([1.2,-1.2])(Q(18.64-1.2))

nc_face = T([1,2])([6.24,3.44])(PROD([STRUCT([curve1,curve2,side1,side2,front_side]),Q(4)]))

north = STRUCT([na_face,nb_face,nc_face])

# South face

s0a_face = INSL(PROD)([Q(29.2), Q(0), Q(2.40)])
s0b_face = INSL(PROD)([QUOTE([6.24,-3.44,-12.96,-3.44,3.12]), Q(0), QUOTE([-2.40,1.20])])
s0c_face = INSL(PROD)([QUOTE([6.24,-3.44,12.96,-3.44,3.12]), Q(0), QUOTE([-3.60,0.40])])
s0_face = [s0a_face, s0b_face, s0c_face]
s1a_face = INSL(PROD)([QUOTE([6.24,-3.44,12.96,-3.44,3.12]), Q(0), Q(1.90)])
s1b_face = INSL(PROD)([QUOTE([6.24,-3.44,-12.96,-3.44,3.12]), Q(0), QUOTE([-1.9,0.7])])
s1c_face = INSL(PROD)([QUOTE([6.24,-3.44,12.96,-3.44,3.12]), Q(0), QUOTE([-2.60,1.40])])
s1_face = [s1a_face, s1b_face, s1c_face]
s2_face = INSL(PROD)([QUOTE([6.24,-3.44,12.96,-3.44,3.12]), Q(0), Q(2.80)])
s3_face = T(2)(12.84)(INSL(PROD)([QUOTE([-6.24,3.44,-12.96,3.44,-3.12]), Q(0), QUOTE([-1.20,10.0])]))

south = STRUCT([s3_face,T(2)(6.24)]+s0_face+[T(3)(4)]+s1_face+[T(3)(4),s2_face])

# West face

w1a_face = INSL(PROD)([Q(0), Q(7.04), Q(1.2)])
w1b_face = INSL(PROD)([Q(0), QUOTE([2.60,-2.80,1.64]), Q(1.4)])
w1c_face = INSL(PROD)([Q(0), Q(7.04), Q(2.60)])
w2_face = INSL(PROD)([Q(0), Q(2.60), Q(2.0)])
wa_face = STRUCT([T(3)(4.0),w1a_face,T(3)(1.2),w1b_face, T(3)(1.4),w1c_face,T(3)(2.60),w2_face])

w01a_face = INSL(PROD)([Q(0), Q(6.60), Q(6.8)])
w2_face = T(2)(-1.84)(INSL(PROD)([Q(0), Q(8.44), Q(3.2)]))
wb_face = STRUCT([T(3)(1.2),w01a_face,T(3)(6.8),w2_face])

wc_face = T(1)(-16.40)(wb_face)

west = STRUCT([T([1,2])([29.20,-0.80])(wa_face), T([1,2])([26.08,6.24]), wb_face, wc_face])

# East face

ea_face = wa_face

e0a_face = INSL(PROD)([Q(0), Q(6.60), Q(2.8)])
e1a_face = INSL(PROD)([Q(0), Q(6.60), Q(1.2)])
e1b_face = INSL(PROD)([Q(0), QUOTE([-6.2,0.40]), Q(1.4)])
e1c_face = INSL(PROD)([Q(0), Q(6.60), Q(1.4)])
e2a_face = T(2)(-1.84)(INSL(PROD)([Q(0), Q(8.44), Q(1.2)]))
e2b_face = T(2)(-1.84)(INSL(PROD)([Q(0), QUOTE([1.84,-6.2,0.40]), Q(1.4)]))
e2c_face = T(2)(-1.84)(INSL(PROD)([Q(0), QUOTE([8.44]), Q(0.6)]))
eb_face = STRUCT([T(3)(1.2),e0a_face,
	T(3)(2.8),e1a_face,T(3)(1.2),e1b_face,T(3)(1.4),e1c_face,
	T(3)(1.4),e2a_face,T(3)(1.2),e2b_face,T(3)(1.4),e2c_face])

ec_face = T(1)(16.40)(eb_face)

east = STRUCT([T(2)(-0.80)(ea_face), T([1,2])([6.24,6.24]),eb_face,ec_face])
VIEW(east)

# Mockup 3D

mock_up_3D = STRUCT([building,north,south,west,east])

# VIEW(SKEL_1(north))
VIEW(mock_up_3D)
VIEW(SKEL_1(mock_up_3D))
# VIEW(SKEL_1(west))