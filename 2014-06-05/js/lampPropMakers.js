/* ---------- Makers ---------- */

function makeHead(r,R,B) {
  var head = new THREE.Object3D;

  var joint = makeJoint(r);
  head.add(joint);

  var shade = makeShade(R);
  var bulb = makeBulb(B);
  bulb.position.z = R - B - B/4;
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

  var stick = makeStick(r*0.8,h);
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
  var baseOBJ = new THREE.Object3D();

  var points = [];
  for ( var i = 0; i < 10; i ++ ) {
    points.push( new THREE.Vector3( r - Math.sin( i * 0.15 ) * r, 0, (i/10)*h ) );
  }
  points.push(new THREE.Vector3(0,0,h));
  points.push(new THREE.Vector3(0,0,0));
  points.push(new THREE.Vector3(r,0,0));
  var baseGeometry = new THREE.LatheGeometry( points, 32 );
  var base = new THREE.Mesh(baseGeometry, baseMaterial);
  base.position.z = h/4;

  var supportGeometry = new THREE.CylinderGeometry(r, r, h/4, 32);
  var support = new THREE.Mesh(supportGeometry, baseMaterial);
  support.position.z = h/8;
  support.rotation.x = -PI/2;

  support.castShadow = true;
  base.castShadow = true;
  baseOBJ.add(base);
  baseOBJ.add(support);

  return baseOBJ;
}

function makeBulb(B) {
  var bulbGeometry = new THREE.SphereGeometry(B,32,32);
  var bulb = new THREE.Mesh(bulbGeometry);
  bulb.castShadow = true;

  var bulbIn = bulb.clone();
  bulbIn.scale.set(0.95,0.95,0.95);

  // BOOLEAN OPERATION
  var c1 = new ThreeBSP(bulb);
  var c2 = new ThreeBSP(bulbIn);
  var sub = c1.subtract(c2);
  bulb = sub.toMesh(bulbMaterial);

  var bulbBaseGeometry = new THREE.CylinderGeometry(B/2,B/3,B/2,32);
  var bulbBase = new THREE.Mesh(bulbBaseGeometry, bulbBaseMaterial);
  bulbBase.castShadow = true;
  bulbBase.position.z = B+B/4;
  bulbBase.rotation.x = -PI/2;
  bulb.add(bulbBase);

  var bulbWireGeometry = new THREE.OctahedronGeometry(B/2);
  var bulbWire = new THREE.Mesh(bulbWireGeometry, bulbWireMaterial);
  bulb.add(bulbWire);

  var bulbCylinderGeometry = new THREE.CylinderGeometry(B/8,B/8,B,32);
  var bulbWireCylinder = new THREE.Mesh(bulbCylinderGeometry, bulbWireMaterial);
  bulbWireCylinder.position.z = B/2;
  bulbWireCylinder.rotation.x = -PI/2;
  bulb.add(bulbWireCylinder);

  return bulb;
}

function makeShade(R) {
  var shadeGeometry = new THREE.SphereGeometry(R,32,32,0,PI);
  shadeMaterial.side = THREE.DoubleSide;
  var shade = new THREE.Mesh(shadeGeometry, shadeMaterial);
  shade.castShadow = true;
  shade.rotation.x = PI/2;
  return shade;
}

function makeStick(r,h) {
  var stickOBJ = new THREE.Object3D();

  var stickGeometry = new THREE.CylinderGeometry(r,r,1.1*h,32);
  var stick = new THREE.Mesh(stickGeometry, stickMaterial);
  stick.scale.x = 0.8; 
  stick.castShadow = true;
  stickOBJ.add(stick);

  return stickOBJ;
}

function makeJoint(r) {
  var jointOBJ = new THREE.Object3D();

  var jointGeometry = new THREE.CylinderGeometry(r*1.1,r*1.1,1.1*2*r,32);
  var joint = new THREE.Mesh(jointGeometry, jointMaterial);

  var screwGeometry = new THREE.CylinderGeometry(r/1.4,r/1.4,1.4*2*r,32);
  var screw = new THREE.Mesh(screwGeometry);

  var screwHoleGeometry = new THREE.BoxGeometry(2*r/1.9,2*r/1.9/8,4*r/1.9);
  var screwHole1 = new THREE.Mesh(screwHoleGeometry);
  screwHole1.rotation.x = PI/2;
  var screwHole2 = screwHole1.clone();
  screwHole1.position.y = 1.4*r;
  screwHole2.position.y = -1.4*r;

  // BOOLEAN OPERATION
  var sc = new ThreeBSP(screw);
  var h1 = new ThreeBSP(screwHole1);
  var h2 = new ThreeBSP(screwHole2);
  var sub = sc.subtract(h1);
  sub = sub.subtract(h2);
  screw = sub.toMesh(stickMaterial);

  screw.castShadow = true;
  joint.castShadow = true;

  joint.rotation.z = PI/2;
  screw.rotation.z = PI/2;

  jointOBJ.add(joint);
  jointOBJ.add(screw);

  return jointOBJ;
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
  bulbLight.shadowCameraFov = 180 * BULB_LIGHT_A / PI;

  bulbLight.target = target;
  bulbLight.position.set(0,0,BULB_R/2);
  obj.add(bulbLight);

  return bulbLight;
}

function makeBackBulbLight(obj, target, a, b) {
  // bulb light
  var backBulbLight = new THREE.SpotLight( BULB_LIGHT_COLOR );
  backBulbLight.intensity = POINT_LIGHT_INTENSITY;
  backBulbLight.angle = PI/6;
  backBulbLight.distance = BULB_R;
  backBulbLight.castShadow = false;

  backBulbLight.target = target;
  backBulbLight.position.set(a*BULB_R/2,b*BULB_R/2,-BULB_R/2);
  obj.add(backBulbLight);

  return backBulbLight;
}

function makePointLight(obj) {
  var pointLight = new THREE.PointLight( 
    BULB_LIGHT_COLOR, 
    POINT_LIGHT_INTENSITY, 
    SHADE_R*1.05
  );

  pointLight.position.set(0,0,0);
  obj.add(pointLight);

  return pointLight;
}

function makePlane() {
  var planeGeometry = new THREE.PlaneGeometry(PLANE_W*4,PLANE_H*2,PLANE_W/2,PLANE_H/2);
  var plane = new THREE.Mesh(planeGeometry,planeMaterial);
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