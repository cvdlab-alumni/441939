from larcc import *

''' CONSTANTS '''

# Wall width
in_wall = 0.1
out1_wall = 0.25
out2_wall = 0.35

# Floor heights
h = 3.4
fl_h = 0.3

# Door measures
door1_h = 2.40
door2_h = 2.10
door1_w = 1.20
door2_w = 0.80
door1_f = 0.10
door2_f = door1_f
door1_th = 0.15
door2_th = 0.02

# Window measures
window_h1 = 0.95
window_h2 = 0.95 + 1.80
window_h = window_h2-window_h1
window_w = 1.0
window_f = 0.05
window_th = 0.05

''' FUNCTIONS '''

def draw(model):
	return STRUCT(MKPOLS(model))

def addCellNumbers(model, color=CYAN, scale=1.0):
	V,CV = model
	hpc = SKEL_1(STRUCT(MKPOLS(model)))
	return cellNumbering (model,hpc)(range(len(CV)),color,scale)

def removeCells(toRemove, diagram):
	V,CV = diagram
	return V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]

def door_hole(w,h,p,h_floor,axis='x'):
	shape = [1,1,2]
	size = [[w],[p],[h,h_floor-h]] if axis=='x' else [[p],[w],[h,h_floor-h]]
	return assemblyDiagramInit(shape)(size)

def window_hole(w,h1,h2,p,h_floor,axis='x'):
	shape = [1,1,3]
	z_size = [h1,h2-h1,h_floor-h2]
	size = [[w],[p],z_size] if axis=='x' else [[p],[w],z_size]
	return assemblyDiagramInit(shape)(size)

def door(w,h,p,frame,th,axis='x',dtype='main'):
	x_shape = 6 if dtype=='main' else 3
	y_shape = 3
	shape = [x_shape,y_shape,2] if axis=='x' else [y_shape,x_shape,2]
	shutter = (w-frame*3.0)/2 if dtype=='main' else (w-frame*2)
	x_size = [frame,shutter,frame/2.0,frame/2.0,shutter,frame] if dtype=='main' else [frame,shutter,frame]
	y_size = [(p-th)/2.0,th,(p-th)/2.0]
	z_size = [h-frame,frame]
	size = [x_size,y_size,z_size] if axis=='x' else [y_size,x_size,z_size]
	door = assemblyDiagramInit(shape)(size)
	return door

def window(w,h,p,frame,th,axis='x'):
	shape = [6,3,3] if axis=='x' else [3,6,3]
	glass = (w-frame*4)/2.0
	x_size = [frame,glass,frame,frame,glass,frame]
	y_size = [(p-th)/2.0,th,(p-th)/2.0]
	z_size = [frame,h-frame*2,frame]
	size = [x_size,y_size,z_size] if axis=='x' else [y_size,x_size,z_size]
	window = assemblyDiagramInit(shape)(size)
	return window

''' WALLS '''

# MASTER DIAGRAM

master = assemblyDiagramInit([3,5,2])([
	[out2_wall,3.5*2+in_wall,out1_wall],
	[out1_wall,3,in_wall,4,out1_wall],
	[fl_h,h]])

# SOUTH PART

south = assemblyDiagramInit([3,1,1])([[3.5,in_wall,3.5],[3],[h]])
master = diagram2cell(south,master,13)

# NORTH PART

north = assemblyDiagramInit([5,3,1])([[1.5,in_wall,4,in_wall,1.5],[1,in_wall,3],[h]])
master = diagram2cell(north,master,16)

''' DOORS AND WINDOWS HOLES'''

# Creating all type of doors and windows holes

entrance = door_hole(door1_w,door1_h,out2_wall,h,'y')
door_x = door_hole(door2_w,door2_h,in_wall,h,'x')
door_y = door_hole(door2_w,door2_h,in_wall,h,'y')
window_x = window_hole(window_w,window_h1,window_h2,out1_wall,h,'x')
window_y = window_hole(window_w-0.20,window_h1,window_h2,out1_wall,h,'y')

# Doors inception

main_door = assemblyDiagramInit([1,3,1])([
	[out2_wall],[4-0.40,door1_w,0.40],[h]])
main_door = diagram2cell(entrance,main_door,1)

south_doors = assemblyDiagramInit([7,1,1])([
	[0.3,door2_w,3.5-0.3-door2_w,in_wall,0.3,door2_w,3.5-0.3-door2_w],
	[in_wall],[h]])
south_doors = diagram2cell(door_y,south_doors,1)
south_doors = diagram2cell(door_y,south_doors,4)

room_door = assemblyDiagramInit([1,3,1])([
	[in_wall],[3.0-0.4-door2_w,door2_w,0.4],[h]])
room_door = diagram2cell(door_y,room_door,1)

bath_door = assemblyDiagramInit([1,3,1])([
	[in_wall],[0.1,door2_w,0.1],[h]])
bath_door = diagram2cell(door_y,bath_door,1)

# Windows inception

south_windows = assemblyDiagramInit([7,1,1])([
	[2.3,window_w,0.20,in_wall,1.25,window_w,1.25],
	[out1_wall],[h]])
south_windows = diagram2cell(window_x,south_windows,1)
south_windows = diagram2cell(window_x,south_windows,4)

north_windows = assemblyDiagramInit([8,1,1])([
	[0.25,window_w,0.25,in_wall,2.0,window_w,1.0,in_wall+1.50],
	[out1_wall],[h]])
north_windows = diagram2cell(window_x,north_windows,1)
north_windows = diagram2cell(window_x,north_windows,4)

bath_windows = assemblyDiagramInit([1,4,1])([
	[out1_wall],[0.1,window_w-0.20,0.1,3.0+in_wall],[h]
	])
bath_windows = diagram2cell(window_y,bath_windows,1)

# Inception into master

master = diagram2cell(main_door,master,7)
master = diagram2cell(south_doors,master,13)
master = diagram2cell(room_door,master,34)
master = diagram2cell(bath_door,master,37)

master = diagram2cell(south_windows,master,10)
master = diagram2cell(north_windows,master,14)
master = diagram2cell(bath_windows,master,21)

''' DOOR AND WINDOW '''

# Door and windows diagrams

entrance = door(door1_w,door1_h,out2_wall,door1_f,door1_th,'y')
door_x = door(door2_w,door2_h,in_wall,door2_f,door2_th,'x','normal')
door_y = door(door2_w,door2_h,in_wall,door2_f,door2_th,'y','normal')
window_x = window(window_w,window_h,out1_wall,window_f,window_th,'x')
window_y = window(window_w,window_h,out1_wall,window_f,window_th,'y')

# Door and window inceptions

master = diagram2cell(entrance,master,41)
master = diagram2cell(door_y,master,53)
master = diagram2cell(door_x,master,47)
master = diagram2cell(door_x,master,48)
master = diagram2cell(door_y,master,54)

master = diagram2cell(window_x,master,73)
master = diagram2cell(window_x,master,75)
master = diagram2cell(window_x,master,61)
master = diagram2cell(window_x,master,63)
master = diagram2cell(window_y,master,78)

''' REMOVING CELLS '''

# VIEW(addCellNumbers(master, RED, 0.1))
toRemove = [23,25,36,37,38,31,29,26,27,28,33,
	105,107,109,111,81,83,85,87,
	117,129,139,143,157,161,171,183,
	203,212,221,230,200,227,197,206,215,224,
	257,266,275,284,254,281,251,260,269,278,
	452,449,446,443,434,425,416,413,410,407,
	311,320,329,338,308,335,305,314,323,332,
	365,374,383,392,362,389,359,368,377,386
	]
master = removeCells(toRemove,master)

''' VIEWS '''

# VIEW(draw(master))
# VIEW(addCellNumbers(master))