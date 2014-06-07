/* ---------- Prepare materials ---------- */

var planeMaterial = new THREE.MeshPhongMaterial({
	color: PLANE_COLOR, 
	shininess: 50,
	map: THREE.ImageUtils.loadTexture('textures/plane.jpg')});
planeMaterial.side = THREE.DoubleSide;

var baseMaterial = new THREE.MeshPhongMaterial( { 
	color: BASE_COLOR, 
	metal: true, 
	shininess: 100 });

var jointMaterial = new THREE.MeshPhongMaterial( { 
	color: JOINT_COLOR, 
	metal: true, 
	shininess: 500, 
	specular: JOINT_COLOR });

var stickMaterial = new THREE.MeshPhongMaterial( { 
	color: STICK_COLOR, 
	metal: true, 
	shininess: 250, 
	specular: STICK_COLOR });

var shadeMaterial = new THREE.MeshPhongMaterial( { 
	color: SHADE_COLOR,
	metal: true, 
	shininess: 100 });

var bulbMaterial = new THREE.MeshPhongMaterial( { 
	color: BULB_COLOR,
	transparent: true, 
	opacity: 0.2, 
	shininess: 250 });

var objMaterial = new THREE.MeshLambertMaterial( { 
	color: OBJ_COLOR });

var textMaterial = new THREE.MeshPhongMaterial( { 
	color: TEXT_COLOR });

function colorMultiply(C1, C2) {
	var C1R = (C1 >> 16) & 0xFF;
	var C1G = (C1 >> 8) & 0xFF;
	var C1B = C1 & 0xFF;
	var C2R = (C2 >> 16) & 0xFF;
	var C2G = (C2 >> 8) & 0xFF;
	var C2B = C2 & 0xFF;

	var comb = 
		((C1R*C2R/256) << 16) | 
		((C1G*C2G/256) << 8) | 
		((C1B*C2B/256));
	return comb;
}

console.log(colorMultiply(0xDDDDDD, 0xFFFFFF));