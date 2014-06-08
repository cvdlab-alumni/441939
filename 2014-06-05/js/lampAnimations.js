/* ---------- Animations ---------- */

// Final check

var TF = 1000;
var delayF = 2000;

var lampFinalBetaTween = new TWEEN.Tween(arm1.joint.rotation)
  .delay(delayF)
  .to({x: PI/12}, TF)
  .easing(TWEEN.Easing.Linear.None)

var lampFinalGammaTween = new TWEEN.Tween(arm2.joint.rotation)
  .delay(delayF)
  .to({x: PI/3}, TF)
  .easing(TWEEN.Easing.Linear.None)

var lampFinalDeltaTween = new TWEEN.Tween(arm2.stick.rotation)
  .delay(delayF)
  .to({y: 0}, TF)
  .easing(TWEEN.Easing.Linear.None)

var lampFinalEpsilonTween = new TWEEN.Tween(head.joint.rotation)
  .delay(delayF)
  .to({x: PI/5}, TF)
  .easing(TWEEN.Easing.Linear.None)

// bouncing

var TB = 100;

var objBouncingDownTween3 = new TWEEN.Tween(obj.position)
  .to({z: OBJ_L/2}, TB*2)
  .easing(TWEEN.Easing.Bounce.Out)
  .chain(lampFinalBetaTween, 
    lampFinalGammaTween, 
    lampFinalDeltaTween, 
    lampFinalEpsilonTween)

var objBouncingUpTween3 = new TWEEN.Tween(obj.position)
  .to({z: 15}, TB)
  .easing(TWEEN.Easing.Quadratic.Out)
  .chain(objBouncingDownTween3)

var iScaleTween2 = new TWEEN.Tween(iText.scale)
  .delay(TB*1.55)
  .to({y: 0.0}, 0.45*TB)
  .easing(TWEEN.Easing.Linear.None)
  .chain(objBouncingUpTween3)

var objBouncingDownTween2 = new TWEEN.Tween(obj.position)
  .to({z: OBJ_L/2}, TB*2)
  .easing(TWEEN.Easing.Quadratic.In)

var objBouncingUpTween2 = new TWEEN.Tween(obj.position)
  .to({z: (30+1.2*2+0.8/2)/2+OBJ_L/2+30}, TB)
  .easing(TWEEN.Easing.Quadratic.Out)
  .chain(objBouncingDownTween2, iScaleTween2)

var iScaleTween1 = new TWEEN.Tween(iText.scale)
  .delay(TB*1.55)
  .to({y: 0.5}, 0.45*TB)
  .easing(TWEEN.Easing.Linear.None)
  .chain(objBouncingUpTween2)

var objBouncingDownTween1 = new TWEEN.Tween(obj.position)
  .to({z: (30+1.2*2+0.8/2)/2+OBJ_L/2}, TB*2)
  .easing(TWEEN.Easing.Quadratic.In)

var objBouncingUpTween1 = new TWEEN.Tween(obj.position)
  .to({z: 30+OBJ_L/2+1.2*2+0.8/2+40}, TB)
  .easing(TWEEN.Easing.Quadratic.Out)
  .chain(objBouncingDownTween1, iScaleTween1)

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
  .chain(objBouncingUpTween1)

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
  .to({y: -2*PI+PI/2}, scene3a/2*T3a)
  .easing(TWEEN.Easing.Exponential.Out)

var lampHitBetaTween = new TWEEN.Tween(arm1.joint.rotation)
  .delay(delay3)
  .to({x: 0}, scene3a/4*T3a)
  .easing(TWEEN.Easing.Exponential.Out)

var lampHitDeltaTween = new TWEEN.Tween(arm2.stick.rotation)
  .delay(delay3)
  .to({y: 0}, scene3a/4*T3a)
  .easing(TWEEN.Easing.Exponential.Out)

// Warm up

var T2b = 1
var scene2b = 1500;
var delay2b = 200;

var lampWarmUpAlfaTween = new TWEEN.Tween(arm1.rotation)
  .delay(delay2b)
  .to({y: PI/2*3+PI/12}, scene2b*T2b)
  .easing(TWEEN.Easing.Exponential.Out)
  .repeat(3)
  .yoyo(true)
  .chain(lampHitAlfaTween, 
    lampHitBetaTween,
    lampHitDeltaTween,
    objThrownXYTween,
    objRotationTween,
    objThrownZUpTween, 
    camTween
  );

var lampWarmUpBetaTween = new TWEEN.Tween(arm1.joint.rotation)
  .delay(delay2b)
  .to({x: PI/3.5}, scene2b*T2b)
  .easing(TWEEN.Easing.Exponential.Out)
  .repeat(3)
  .yoyo(true)

// Enemy detected (cube) prepare to hit it

var T2a = 1;
var scene2a = 2000;
var delay2a = 1000;

var lampPrepareHitAlfaTween = new TWEEN.Tween(arm1.rotation)
  .delay(delay2a)
  .to({y: PI/2*3+PI/4+PI/6}, scene2a*T2a)
  .easing(TWEEN.Easing.Exponential.Out)

var lampPrepareHitBetaTween = new TWEEN.Tween(arm1.joint.rotation)
  .delay(delay2a)
  .to({x: PI/6}, scene2a*T2a)
  .easing(TWEEN.Easing.Exponential.Out)

var lampPrepareHitGammaTween = new TWEEN.Tween(arm2.joint.rotation)
  .delay(delay2a)
  .to({x: PI/2.8}, scene2a*T2a)
  .easing(TWEEN.Easing.Exponential.Out)

var lampPrepareHitDeltaTween = new TWEEN.Tween(arm2.stick.rotation)
  .delay(delay2a)
  .to({y: 3*PI/4}, scene2a*T2a)
  .easing(TWEEN.Easing.Exponential.Out)

var lampPrepareHitEpsilonTween = new TWEEN.Tween(head.joint.rotation)
  .delay(delay2a)
  .to({x: PI/6}, scene2a*T2a)
  .easing(TWEEN.Easing.Exponential.Out)
  .chain(lampWarmUpAlfaTween, lampWarmUpBetaTween);

// Lamp is confused

var T1 = 1;
var scene1 = 1500

var lampConfusedTween = new TWEEN.Tween(head.joint.rotation)
  .to({x: PI/6}, scene1*T1)
  .easing(TWEEN.Easing.Elastic.Out)
  .repeat(2)
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
var offset = 1000;

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
  .delay(delay)
  .to({x: [-PI/6,-PI/6]}, scene0*T0)
  .easing(TWEEN.Easing.Linear.None)
  // .chain(lampConfusedTween)

var lampTwistGammaTween = new TWEEN.Tween(arm2.joint.rotation)
  .delay(delay)
  .to({x: [PI/6,4*PI/6]}, scene0*T0)
  .easing(TWEEN.Easing.Linear.None)
  // .chain(lampConfusedTween)

var lampTwistEpsilonTween = new TWEEN.Tween(head.joint.rotation)
  .delay(delay)
  .to({x: PI/4}, scene0*T0)
  .easing(TWEEN.Easing.Linear.None)
  .chain(lampConfusedTween)

var lampPrepareBetaJumpTween = new TWEEN.Tween(arm1.joint.rotation)
  .delay(delay)
  .to({x: -PI/3}, T0*offset)
  .easing(TWEEN.Easing.Exponential.Out)

var lampPrepareGammaJumpTween = new TWEEN.Tween(arm2.joint.rotation)
  .delay(delay)
  .to({x: 3*PI/4}, T0*offset)
  .easing(TWEEN.Easing.Exponential.Out)
  .chain(lampWalkTween,
    lampTwistAlfaTween,
    lampTwistBetaTween,
    lampTwistGammaTween,
    lampTwistEpsilonTween)

var lampCheckingTween = new TWEEN.Tween(head.joint.rotation)
  .delay(250)
  .to({x: PI/4}, scene1*T1)
  .easing(TWEEN.Easing.Elastic.Out)
  .repeat(2)
  .yoyo(true)
  .chain(lampPrepareBetaJumpTween, lampPrepareGammaJumpTween)

var lookingScene = 2000;

var objColorTween = new TWEEN.Tween(obj.material.color)
  .delay(lookingScene*T0*1.8+delay)
  .to({r: [0.25,0.65], g: [0.85,0.2], b: [0.1,0.2]}, 300)
  .easing(TWEEN.Easing.Quadratic.In)

var lampLoorkAroundTween3 = new TWEEN.Tween(arm1.rotation)
  .to({y: 7*PI/4}, lookingScene*T0)
  .easing(TWEEN.Easing.Elastic.Out)
  .chain(lampCheckingTween)

var lampLoorkAroundTween2 = new TWEEN.Tween(arm1.rotation)
  .delay(delay)
  .to({y: 2*PI}, lookingScene*T0*2)
  .easing(TWEEN.Easing.Linear.None)
  .chain(lampLoorkAroundTween3)

var lampLoorkAroundTween1 = new TWEEN.Tween(arm1.rotation)
  .to({y: PI/2*3}, lookingScene*T0)
  .easing(TWEEN.Easing.Linear.None)
  .chain(lampLoorkAroundTween2, objColorTween)

// Lights turning on

mainLight.intensity = 0;
secondaryLight.intensity = 0;
backLight.intensity = 0;

var TL = 1;
var sceneL = 2000;
var delayL = 1500;

var updateGUITween = new TWEEN.Tween()
  .delay(500)
  .onComplete(function() {
    controls.mainLight = true;
    controls.secondaryLight = true;
    controls.backLight = true;
    updateControllers();
  })
  .chain(lampLoorkAroundTween1)

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