/* ---------- Prepare scene ---------- */

// create scene
var scene = new THREE.Scene();
// scene.fog = new THREE.FogExp2( 0xc0c0c0, PLANE_H*2, PLANE_H*10 );

// position and point the camera to the center of the scene
var camera = new THREE.PerspectiveCamera(CAM_ANGLE, ASPECT_RATIO, CAM_NEAR, CAM_FAR);
camera.up = new THREE.Vector3(0,0,1);
camera.position.set(0,-PLANE_H/1.2, 2*ARM_H);
camera.lookAt(scene.position);

// set renderer
var renderer = new THREE.WebGLRenderer();
renderer.setClearColor(new THREE.Color(RENDERER_COLOR, 1.0));
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.antialias = true;
renderer.shadowMapEnabled = true;
// renderer.shadowMapType = THREE.PCFSoftShadowMap;

// stats
var stats = initStats();

// trackball
var trackball = new THREE.TrackballControls(camera);

// axis
var axisHelper = new THREE.AxisHelper(3);
axisHelper.visible = false;
scene.add(axisHelper);

// create plane
var plane = makePlane();
scene.add(plane);

// create background
var background = plane.clone();
background.rotation.x = PI/2;
background.position.set(0,PLANE_H,PLANE_H);
scene.add(background);

/* ---------- Create objects ---------- */

var obj = makeObj(OBJ_L);
obj.position.set(-PLANE_W/4, -PLANE_H/4, OBJ_L/2);
scene.add(obj);

var text = makeText('P   x a r');
text.rotation.x = PI/2;
text.position.set(-PLANE_W*3/8,PLANE_H*5/8, 1.2);
scene.add(text);

var iText = makeText('   i');
iText.rotation.x = PI/2;
iText.position.set(-PLANE_W*3/8,PLANE_H*5/8, 1.2);
scene.add(iText);

/* ---------- Create lamp structure ---------- */

// base
var base = makeBase(BASE_R,BASE_H);
// center2Origin(BASE_H/2,base);

// arm
var arm1 = makeArm(ARM_R,ARM_H);
var arm2 = makeArm(ARM_R,ARM_H);
arm1.hook.add(arm2);

// head
var head = makeHead(ARM_R,SHADE_R,BULB_R);
arm2.hook.add(head);

// position and rotation
center2Origin(ARM_R,arm1);
arm1.position.z += BASE_H;

// lamp
var arm = arm1;
var lamp = new THREE.Object3D();
lamp.add(base);
lamp.add(arm);
scene.add(lamp);

// Initial position
arm1.rotation.y = 7*PI/4;
arm1.joint.rotation.x = PI/12;
arm2.joint.rotation.x = PI/3;
arm2.stick.rotation.y = 0;
head.joint.rotation.x = PI/5;

/* ---------- Prepare lights ---------- */

// add ambientLight
var ambientLight = new THREE.AmbientLight( AMBIENT_COLOR );
scene.add(ambientLight);

// add directional light
var mainLight = makeMainLight(plane);
mainLight.position.set(PLANE_W,-PLANE_H,4*ARM_H);
scene.add(mainLight);

// add secondary light
var secondaryLight = mainLight.clone();
secondaryLight.position.set(0,0,(PLANE_W+PLANE_H)/2);
secondaryLight.intensity = SECONDARY_INTENSITY;
scene.add(secondaryLight);

// backlight
var backLight = mainLight.clone();
backLight.position.set(0,50,PLANE_H);
backLight.intensity = BACK_LIGHT_INTENSITY;
backLight.target = background;
backLight.castShadow = true;
scene.add(backLight);

// add bulb light
var target = new THREE.Object3D();
target.position.set(0, 0, 0);
head.shade.add(target);
var bulbLight = makeBulbLight(head.bulb, target);
var bulbLightHelper = new THREE.SpotLightHelper(bulbLight);

var backBulbLight1 = makeBackBulbLight(head.bulb, bulbLight, 1, -1);
var backBulbLight2 = makeBackBulbLight(head.bulb, bulbLight, 1, 1);
var backBulbLight3 = makeBackBulbLight(head.bulb, bulbLight, -1, 1);
var backBulbLight4 = makeBackBulbLight(head.bulb, bulbLight, -1, -1);

var backBulbLightHelper1 = new THREE.SpotLightHelper(backBulbLight1);
var backBulbLightHelper2 = new THREE.SpotLightHelper(backBulbLight2);
var backBulbLightHelper3 = new THREE.SpotLightHelper(backBulbLight3);
var backBulbLightHelper4 = new THREE.SpotLightHelper(backBulbLight4);

var pointLight = makePointLight(head.shade);
var pointLightHelper = new THREE.PointLightHelper(pointLight);
pointLightHelper.visible = false;
scene.add(pointLightHelper);

/* ---------- Support methods ---------- */

// for rendering stats
function initStats() {
  var stats = new Stats();
  stats.setMode(0); // 0: fps, 1: ms
  $('#stats').append(stats.domElement);
  return stats;
}

function center2Origin(h,mesh) {
  mesh.rotation.x = PI/2;
  mesh.position.z = h;
}