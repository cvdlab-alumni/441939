/* ---------- Controls ---------- */

var controls = new function () {
  this.alpha = 7*PI/4;
  this.beta = PI/12;
  this.gamma = PI/3;
  this.delta = 0;
  this.epsilon = PI/5;
  this.switch = true;
  this.x = 0;
  this.y = 0;

  this.ambientColor = AMBIENT_COLOR;
  this.mainLight = false;
  this.secondaryLight = false;
  this.backLight = false;

  this.debugShadows = false;
  this.debugHelpers = false;
}

var gui = new dat.GUI();

// Folders
var lampGUI = gui.addFolder('Lamp');
var lightsGUI = gui.addFolder('Lights');
var debugGUI = gui.addFolder('Debug');

lampGUI.add(controls, 'alpha', 0, 2*PI).onChange(function (a) {
  arm1.rotation.y = a;
});

lampGUI.add(controls, 'beta', 0, PI/2).onChange(function (a) {
  arm1.joint.rotation.x = a;
});

lampGUI.add(controls, 'gamma', 0, PI/2).onChange(function (a) {
  arm2.joint.rotation.x = a;
});

lampGUI.add(controls, 'delta', 0, 2*PI).onChange(function (a) {
  arm2.stick.rotation.y = a;
});

lampGUI.add(controls, 'epsilon', 0, PI/2).onChange(function (a) {
  head.joint.rotation.x = a;
});

lampGUI.add(controls, 'switch').onChange(function (b) {
  bulbLight.shadowDarkness = b * 0.5;
  bulbLight.intensity = b * BULB_LIGHT_INTENSITY;
  pointLight.intensity = b * POINT_LIGHT_INTENSITY;
  backBulbLight1.intensity = b * POINT_LIGHT_INTENSITY;
  backBulbLight2.intensity = b * POINT_LIGHT_INTENSITY;
  backBulbLight3.intensity = b * POINT_LIGHT_INTENSITY;
  backBulbLight4.intensity = b * POINT_LIGHT_INTENSITY;
 });

var Lx = 4*PLANE_W/2 - BASE_R;

lampGUI.add(controls, 'x', -Lx, Lx).onChange(function (xx) {
  lamp.position.x = xx;
});

var Ly = 2*PLANE_H/2 - BASE_R;

lampGUI.add(controls, 'y', -Ly, Ly).onChange(function (yy) {
  lamp.position.y = yy;
});

lightsGUI.addColor(controls, 'ambientColor').onChange(function (c) {
  ambientLight.color = new THREE.Color(c);
});

lightsGUI.add(controls, 'mainLight').onChange(function (i) {
  mainLight.intensity = i * DIRECTIONAL_INTENSITY;
});

lightsGUI.add(controls, 'secondaryLight').onChange(function (i) {
  secondaryLight.intensity = i * SECONDARY_INTENSITY;
});

lightsGUI.add(controls, 'backLight').onChange(function (i) {
  backLight.shadowDarkness = i * 0.5;
  backLight.intensity = i * BACK_LIGHT_INTENSITY;
});

debugGUI.add(controls, 'debugShadows').onChange(function (e) {
  bulbLight.shadowCameraVisible = e;
  backLight.shadowCameraVisible = e;
});

debugGUI.add(controls, 'debugHelpers').onChange(function (e) {
  axisHelper.visible = e;
  bulbLightHelper.visible = e;
  pointLightHelper.visible = e;

  if (e) {
    scene.add(bulbLightHelper);
    scene.add(backBulbLightHelper1);
    scene.add(backBulbLightHelper2);
    scene.add(backBulbLightHelper3);
    scene.add(backBulbLightHelper4);
  } else {
    scene.remove(bulbLightHelper);
    scene.remove(backBulbLightHelper1);
    scene.remove(backBulbLightHelper2);
    scene.remove(backBulbLightHelper3);
    scene.remove(backBulbLightHelper4);
  }
});