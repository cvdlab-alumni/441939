/* ---------- CONSTANTS ---------- */

var PLANE_W = 200;
var PLANE_H = 200;
var BASE_R = 8;
var BASE_H = 2.5;
var ARM_R = 1;
var ARM_H = 21;
var SHADE_R = 5;
var BULB_R = 1.5;
var OBJ_L = 10;
var ASPECT_RATIO = window.innerWidth / window.innerHeight;
var CAM_NEAR = 0.1;
var CAM_FAR = (PLANE_H+PLANE_W)*5;
var CAM_ANGLE = 50;
var PI = Math.PI;

/* ---------- Colors and lights ---------- */

var AMBIENT_COLOR = 0x0c0c0c;
var DIRECTIONAL_COLOR = 0xffffff;
var DIRECTIONAL_INTENSITY = 0.55;
var SECONDARY_INTENSITY = 0.50;
var POINT_LIGHT_INTENSITY = 10.0;
var BULB_LIGHT_NEAR = SHADE_R;
var BULB_LIGHT_DISTANCE = 150;
var BULB_LIGHT_INTENSITY = 4.5;
var BULB_LIGHT_A = PI/3;
var BULB_LIGHT_COLOR = 0xFFC58F;
var RENDERER_COLOR = 0x87CEEB;
var PLANE_COLOR = 0xe0e0e0;
var SHADOWMAP = 2048;
var BASE_COLOR = 0xDDDDDD;
var JOINT_COLOR = 0xEDEDED;
var STICK_COLOR = 0xD3D3D3;
var SHADE_COLOR = 0xEDEDED;
var BULB_COLOR = 0xFFFFFF;
var OBJ_COLOR = 0x3399FF;
var TEXT_COLOR = 0x003366;