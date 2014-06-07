/* ---------- Makers ---------- */

function makeHead(r,R,B) {
  var head = new THREE.Object3D;

  var joint = makeJoint(r);
  head.add(joint);

  var shade = makeShade(R);
  var bulb = makeBulb(B);
  bulb.position.z = R - B;
  shade.add(bulb);
  shade.position.y = R + r;
  joint.add(shade);
  
  head.joint = joint;
  head.shade = shade;
  head.bulb = bulb;

  return head;
}

function makeArm(r,h) {
  var arm = new THREE.Object3D();

  var joint = makeJoint(r);
  arm.add(joint);

  var stick = makeStick(r,h);
  stick.position.y = h/2 + r;
  joint.add(stick);

  var hook = new THREE.Object3D();
  hook.position.y = h/2 + r;
  stick.add(hook);

  arm.joint = joint;
  arm.stick = stick;
  arm.hook = hook;

  return arm;
}

function makeBase(r,h) {
  var baseGeometry = new THREE.CylinderGeometry(r, r, h);
  var base = new THREE.Mesh(baseGeometry, baseMaterial);
  base.castShadow = true;
  return base;
}

function makeBulb(B) {
  var bulbGeometry = new THREE.SphereGeometry(B);
  var bulb = new THREE.Mesh(bulbGeometry, bulbMaterial);
  bulb.castShadow = true;
  return bulb;
}

function makeShade(R) {
  var shadeGeometry = new THREE.SphereGeometry(R,50,50,0,PI);
  shadeMaterial.side = THREE.DoubleSide;
  var shade = new THREE.Mesh(shadeGeometry, shadeMaterial);
  shade.castShadow = true;
  shade.rotation.x = PI/2;
  return shade;
}

function makeStick(r,h) {
  var stickGeometry = new THREE.CylinderGeometry(r,r,h);
  var stick = new THREE.Mesh(stickGeometry, stickMaterial);
  stick.castShadow = true;
  return stick;
}

function makeJoint(r) {
  var jointGeometry = new THREE.SphereGeometry(r);
  var joint = new THREE.Mesh(jointGeometry, jointMaterial);
  joint.castShadow = true;
  return joint;
}

function makeObj(L) {
  var objGeometry = new THREE.BoxGeometry(L,L,L);
  var obj = new THREE.Mesh(objGeometry, objMaterial);
  obj.castShadow = true;
  return obj;
}

function makeMainLight(target) {
  var directionalLight = new THREE.DirectionalLight( DIRECTIONAL_COLOR );
  directionalLight.intensity = DIRECTIONAL_INTENSITY;

  // directionalLight.castShadow = true;
  // directionalLight.shadowMapWidth = SHADOWMAP;
  // directionalLight.shadowMapHeight = SHADOWMAP;
  // directionalLight.shadowBias = 0.0001;
  // directionalLight.shadowDarkness = 0.5;
  // directionalLight.shadowCameraNear = SHADE_R;
  // directionalLight.shadowCameraFar = PLANE_H+PLANE_W;
  // directionalLight.shadowCameraTop = (PLANE_H+PLANE_W)/2;
  // directionalLight.shadowCameraBottom = -(PLANE_H+PLANE_W)/2;
  // directionalLight.shadowCameraLeft = -(PLANE_H+PLANE_W)/2;
  // directionalLight.shadowCameraRight = (PLANE_H+PLANE_W)/2;

  directionalLight.target = target;

  return directionalLight;
}

function makeBulbLight(obj, target) {
  // bulb light
  var bulbLight = new THREE.SpotLight( BULB_LIGHT_COLOR );
  bulbLight.intensity = BULB_LIGHT_INTENSITY;
  bulbLight.distance = BULB_LIGHT_DISTANCE;
  bulbLight.angle = BULB_LIGHT_A;

  bulbLight.castShadow = true;
  bulbLight.shadowMapWidth = SHADOWMAP;
  bulbLight.shadowMapHeight = SHADOWMAP;
  bulbLight.shadowCameraNear = SHADE_R;
  bulbLight.shadowCameraFar = PLANE_H+PLANE_W;
  bulbLight.shadowBias = 0.0001;
  bulbLight.shadowDarkness = 0.5;
  bulbLight.shadowCameraFov = 2*180 * BULB_LIGHT_A / PI;

  bulbLight.target = target;
  bulbLight.position.set(0,0,BULB_R/2);
  obj.add(bulbLight);

  return bulbLight;
}

function makePointLight(obj) {
  var light = new THREE.PointLight( 
    BULB_LIGHT_COLOR, 
    POINT_LIGHT_INTENSITY, 
    BULB_R*1.5
  );

  light.position.set(0,0,0);
  obj.add(light);

  return light;
}

function makePlane() {
  var planeGeometry = new THREE.PlaneGeometry(PLANE_W*4,PLANE_H*2,PLANE_W,PLANE_H);
  var plane = new THREE.Mesh(planeGeometry,planeMaterial);
  // rotate and translate the plane
  plane.receiveShadow = true;
  return plane;
}

function makeText(text) {

  var options = {
    size: 30,
    height: 8,
    weight: 'normal',
    font: 'helvetiker',
    style: 'normal',
    bevelThickness: 0.8,
    bevelSize: 1.2,
    bevelSegments: 3,
    bevelEnabled: true,
    curveSegments: 12,
    steps: 1
  };

  var textGeometry = new THREE.TextGeometry(text, options);
  var text = new THREE.Mesh(textGeometry, textMaterial);
  text.castShadow = true;
  return text;
}