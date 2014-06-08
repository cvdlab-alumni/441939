/* ---------- Animations ---------- */

// Enemy flying

var T3 = 1;
var scene3 = 2000;
var delay3 = 750;

var T3b = T3;
var scene3b = scene3/4;

var objThrownXYTween = new TWEEN.Tween(obj.position)
  .delay(delay3+5)
  .to({x: -PLANE_W*3/8+30+7, y: PLANE_H*5/8-OBJ_L/2-(8-OBJ_L)/2}, scene3b*T3b)
  .easing(TWEEN.Easing.Linear.None)

var objRotationTween = new TWEEN.Tween(obj.rotation)
  .delay(delay3+5)
  .to({x: 4*PI, y: 0, z: -4*PI}, scene3b*T3b)
  .easing(TWEEN.Easing.Linear.None)

var objThrownZDownTween = new TWEEN.Tween(obj.position)
  .to({z: 30+OBJ_L/2+1.2*2+0.8/2}, scene3b/2*T3b)
  .easing(TWEEN.Easing.Quadratic.In)

var objThrownZUpTween = new TWEEN.Tween(obj.position)
  .delay(delay3+5)
  .to({z: 75}, scene3b/2*T3b)
  .easing(TWEEN.Easing.Quadratic.Out)
  .chain(objThrownZDownTween)

var camTween = new TWEEN.Tween(camera.position)
  .delay(delay3+5)
  .to({x: PLANE_H/2, y: -100}, scene3b*T3b)
  .easing(TWEEN.Easing.Linear.None)

// HIT!!!!!!!!!!!!!

var T3a = T3;
var scene3a = scene3;

var lampHitAlfaTween = new TWEEN.Tween(arm1.rotation)
  .delay(delay3)
  .to({y: -4*PI+PI/2}, scene3a*T3a)
  .easing(TWEEN.Easing.Exponential.Out)

var lampHitBetaTween = new TWEEN.Tween(arm1.joint.rotation)
  .delay(delay3)
  .to({x: 0}, scene3a/10*T3a)
  .easing(TWEEN.Easing.Exponential.Out)

var lampHitDeltaTween = new TWEEN.Tween(arm2.joint.rotation)
  .delay(delay3)
  .to({y: 0}, scene3a/10*T3a)
  .easing(TWEEN.Easing.Exponential.Out)

// Enemy detected (cube) prepare to hit it

var T2 = 1;
var scene2 = 500;

var lampPrepareHitAlfaTween = new TWEEN.Tween(arm1.rotation)
  .to({y: PI/2*3+PI/6}, scene2*T2)
  .easing(TWEEN.Easing.Exponential.Out)

var lampPrepareHitBetaTween = new TWEEN.Tween(arm1.joint.rotation)
  .to({x: PI/3.5}, scene2*T2)
  .easing(TWEEN.Easing.Exponential.Out)

var lampPrepareHitGammaTween = new TWEEN.Tween(arm2.joint.rotation)
  .to({x: PI/2.8}, scene2*T2)
  .easing(TWEEN.Easing.Exponential.Out)

var lampPrepareHitDeltaTween = new TWEEN.Tween(arm2.joint.rotation)
  .to({y: 3*PI/4}, scene2*T2)
  .easing(TWEEN.Easing.Exponential.Out)

var lampPrepareHitEpsilonTween = new TWEEN.Tween(head.joint.rotation)
  .to({x: PI/6}, scene2*T2)
  .easing(TWEEN.Easing.Exponential.Out)
  .chain(lampHitAlfaTween, 
    lampHitBetaTween,
    lampHitDeltaTween,
    objThrownXYTween,
    objRotationTween,
    objThrownZUpTween,
    camTween);

// Lamp is confused

var T1 = 1;
var scene1 = 1000

var lampConfusedTween = new TWEEN.Tween(head.joint.rotation)
  .to({x: PI/4}, scene1*T1)
  .easing(TWEEN.Easing.Circular.Out)
  .repeat(3)
  .yoyo(true)
  .chain(lampPrepareHitAlfaTween,
    lampPrepareHitBetaTween,
    lampPrepareHitGammaTween,
    lampPrepareHitDeltaTween,
    lampPrepareHitEpsilonTween)

// Jumping

var T0 = 1;
var scene0 = 500;
var delay = 1000;
var offset = 200;

var lampWalkTween = new TWEEN.Tween(lamp.position)
  .delay(delay)
  .to({ x: [-PLANE_W/32, -PLANE_W/16], y: [-PLANE_H/8,-PLANE_H/4], z: [+50, 0]}, scene0*T0)
  .easing(TWEEN.Easing.Quadratic.Out)
  .interpolation( TWEEN.Interpolation.Bezier)
  .chain(lampConfusedTween)

var lampTwistAlfaTween = new TWEEN.Tween(arm1.rotation)
  .delay(delay)
  .to({y: PI/2*3}, scene0*T0)
  .easing(TWEEN.Easing.Linear.None)
  // .chain(lampConfusedTween)

var lampTwistBetaTween = new TWEEN.Tween(arm1.joint.rotation)
  .delay(delay-offset)
  .to({x: [PI/3, 0]}, scene0*T0+offset)
  .easing(TWEEN.Easing.Linear.None)
  // .chain(lampConfusedTween)

var lampTwistGammaTween = new TWEEN.Tween(arm2.joint.rotation)
  .delay(delay-offset)
  .to({x: [PI/6,PI/2]}, scene0*T0+offset)
  .easing(TWEEN.Easing.Linear.None)
  // .chain(lampConfusedTween)

var lampTwistEpsilonTween = new TWEEN.Tween(head.joint.rotation)
  .delay(delay)
  .to({x: PI/3}, scene0*T0)
  .easing(TWEEN.Easing.Linear.None)
  .chain(lampConfusedTween)

// Lights turning on

mainLight.intensity = 0;
secondaryLight.intensity = 0;
backLight.intensity = 0;

var TL = 1;
var sceneL = 2500;
var delayL = 1500;

var updateGUITween = new TWEEN.Tween()
  .delay(500)
  .onComplete(function() {
    controls.mainLight = true;
    controls.secondaryLight = true;
    controls.backLight = true;
    updateControllers();
  })
  .chain(lampWalkTween,
    lampTwistAlfaTween,
    lampTwistBetaTween,
    lampTwistGammaTween,
    lampTwistEpsilonTween)

var secondaryLightTween = new TWEEN.Tween(secondaryLight)
  .delay(delayL)
  .to({intensity: SECONDARY_INTENSITY}, sceneL*TL)
  .easing(TWEEN.Easing.Linear.None)

var mainLightTween = new TWEEN.Tween(mainLight)
  .delay(delayL)
  .to({intensity: DIRECTIONAL_INTENSITY}, sceneL*TL)
  .easing(TWEEN.Easing.Linear.None)
  .chain(updateGUITween)

var backLightTween = new TWEEN.Tween(backLight)
  .delay(delayL)
  .to({intensity: BACK_LIGHT_INTENSITY}, sceneL*TL)
  .easing(TWEEN.Easing.Linear.None)

function updateControllers() {
  for (var i=0; i<lightsGUI.__controllers.length; i++) {
    lightsGUI.__controllers[i].updateDisplay();
  }
}

function startAnimation() {
  $("#startButton").fadeOut(500, function() { $(this).remove(); });
  secondaryLightTween.start();
  mainLightTween.start();
  backLightTween.start();
  // var elem = document.getElementById('startButton');
  // elem.parentNode.removeChild(elem);
}