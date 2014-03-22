from exercise2 import *

p_col = RED
div_col = BLUE
front_col = GREEN

# Floor 0

floor0a = PROD([f0a_plan,Q(-4.0)])
pillars0a = COLOR(p_col)(PROD([pillars0a,Q(4-0.40)]))
div0a_wall = COLOR(div_col)(PROD([div0a_wall, Q(4-0.40)]))
floor0a = STRUCT([floor0a,pillars0a,div0a_wall])

floor0b = PROD([f0b_plan,Q(-1.20)])
pillars0b = COLOR(p_col)(PROD([pillars0b,Q(4-1.2-0.40)]))
back_pillars0b = COLOR(p_col)(PROD([back_pillars0b, Q(4-1.2-0.40)]))
div0b_wall = COLOR(div_col)(PROD([div0b_wall, Q(4-1.2-0.40)]))
floor0b = T([1,2])([6.24,3.44])(STRUCT([floor0b,pillars0b,back_pillars0b,div0b_wall]))

floor0 = STRUCT([floor0a,T(3)(1.2),floor0b])

# Floor 1

floor1 = PROD([f1_plan,Q(-0.4)])
pillars1 = COLOR(p_col)(PROD([pillars1,Q(4-0.40)]))
back_pillars1 = COLOR(p_col)(PROD([back_pillars1, Q(4-0.40)]))
div1_wall = COLOR(div_col)(PROD([div1_wall, Q(4-0.40)]))
floor1 = STRUCT([floor1,pillars1,back_pillars1,div1_wall])

# ROOF

roof = PROD([f1_plan,Q(-0.4)])
pillars2 = COLOR(p_col)(PROD([pillars2,Q(3.20-0.40)]))
back_pillars2 = COLOR(p_col)(PROD([back_pillars2, Q(3.20-0.40)]))
roof = STRUCT([roof,pillars2,back_pillars2])

# ROOF COVER

cover = PROD([cover,Q(-0.4)])

# NORTH FACE

n1a_face = INSL(PROD)([Q(29.2), Q(0.4), Q(1.20)])
n1b_face = INSL(PROD)([QUOTE([0.40,-28.4,0.40]), Q(0.4), QUOTE([-1.20,1.40])])
n1c_face = INSL(PROD)([Q(29.2), Q(0.4), QUOTE([-2.60,1.40])])
n2a_face = INSL(PROD)([Q(29.2), Q(0.4), QUOTE([-4.0,1.20])])

na_face = STRUCT([T([2,3])([-0.80,4.0]), n1a_face, n1b_face,n1c_face,n2a_face])

nb_face = T([2,3])([4.4,8.0])(INSL(PROD)([QUOTE([-6.24,3.44,-12.96,3.44]),Q(0.4),Q(3.2)]))

north = STRUCT([na_face,nb_face,nc_face])

# SOUTH FACE

s0a_face = INSL(PROD)([Q(29.2), Q(-0.4), Q(2.40)])
s0b_face = INSL(PROD)([QUOTE([6.24,-3.44,-12.96,-3.44,3.12]), Q(-0.4), QUOTE([-2.40,1.20])])
s0c_face = INSL(PROD)([QUOTE([6.24,-3.44,12.96,-3.44,3.12]), Q(-0.4), QUOTE([-3.60,0.40])])
s0_face = [s0a_face, s0b_face, s0c_face]
s1a_face = INSL(PROD)([QUOTE([6.24,-3.44,12.96,-3.44,3.12]), Q(-0.4), Q(1.90)])
s1b_face = INSL(PROD)([QUOTE([6.24,-3.44,-12.96,-3.44,3.12]), Q(-0.4), QUOTE([-1.9,0.7])])
s1c_face = INSL(PROD)([QUOTE([6.24,-3.44,12.96,-3.44,3.12]), Q(-0.4), QUOTE([-2.60,1.40])])
s1_face = [s1a_face, s1b_face, s1c_face]
s2_face = INSL(PROD)([QUOTE([6.24,-3.44,12.96,-3.44,3.12]), Q(-0.4), Q(2.80)])
s3_face = T(2)(12.84)(INSL(PROD)([QUOTE([-6.24,3.44,-12.96,3.44,-3.12]), Q(-0.4), QUOTE([-1.20,10.0])]))

south = STRUCT([s3_face,T(2)(6.24)]+s0_face+[T(3)(4)]+s1_face+[T(3)(4),s2_face])

# WEST FACE

w1a_face = INSL(PROD)([Q(-0.4), Q(7.04), Q(1.2)])
w1b_face = INSL(PROD)([Q(-0.4), QUOTE([2.60,-2.80,1.64]), Q(1.4)])
w1c_face = INSL(PROD)([Q(-0.4), Q(7.04), Q(2.60)])
w2_face = INSL(PROD)([Q(-0.4), Q(2.60), Q(2.0)])
wa_face = STRUCT([T(3)(4.0),w1a_face,T(3)(1.2),w1b_face, T(3)(1.4),w1c_face,T(3)(2.60),w2_face])

w01a_face = INSL(PROD)([Q(-0.4), Q(6.60), Q(6.8)])
w2_face = T(2)(-1.84)(INSL(PROD)([Q(-0.4), Q(8.44), Q(3.2)]))
wb_face = STRUCT([T(3)(1.2),w01a_face,T(3)(6.8),w2_face])

wc_face = T(1)(-16.40)(wb_face)

west = STRUCT([T([1,2])([29.20,-0.80])(wa_face), T([1,2])([26.08,6.24]), wb_face, wc_face])

# EAST FACE

ea_face = wa_face

e0a_face = INSL(PROD)([Q(0.4), Q(6.60), Q(2.8)])
e1a_face = INSL(PROD)([Q(0.4), Q(6.60), Q(1.2)])
e1b_face = INSL(PROD)([Q(0.4), QUOTE([-6.2,0.40]), Q(1.4)])
e1c_face = INSL(PROD)([Q(0.4), Q(6.60), Q(1.4)])
e2a_face = T(2)(-1.84)(INSL(PROD)([Q(0.4), Q(8.44), Q(1.2)]))
e2b_face = T(2)(-1.84)(INSL(PROD)([Q(0.4), QUOTE([1.84,-6.2,0.40]), Q(1.4)]))
e2c_face = T(2)(-1.84)(INSL(PROD)([Q(0.4), QUOTE([8.44]), Q(0.6)]))
eb_face = STRUCT([T(3)(1.2),e0a_face,
	T(3)(2.8),e1a_face,T(3)(1.2),e1b_face,T(3)(1.4),e1c_face,
	T(3)(1.4),e2a_face,T(3)(1.2),e2b_face,T(3)(1.4),e2c_face])

ec_face = T(1)(16.40)(eb_face)

east = STRUCT([T(2)(-0.80)(ea_face), T([1,2])([6.24,6.24]),eb_face,ec_face])

# 3D Model

faces = STRUCT([north,south,west,east])
floors = STRUCT([floor0,T(3)(4.0),floor1,T(3)(4.0),roof,T(3)(3.20),cover])
solid_model_3D = STRUCT([floors,faces])

VIEW(solid_model_3D)

