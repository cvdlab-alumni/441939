from exercise3 import *

l = 0.30;
h = 0.20;
unit = MKPOL([[[0,0],[0,0.2+h],[l,h],[l,0.2+h]],[[1,2,3,4]],None])
unit = MAP([S1,S3,S2])(PROD([unit,Q(0.80)]))
ramp = T([1,2,3])([7.44,-0.80,-4.0])(STRUCT(NN(19)([unit,T([1,3])([l,h])])))


building = STRUCT([solid_model_3D,ramp])

VIEW(building)