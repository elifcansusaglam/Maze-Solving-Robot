
"use strict";

let KeyboardInput = require('./KeyboardInput.js');
let ControllerInfo = require('./ControllerInfo.js');
let ExternalPower = require('./ExternalPower.js');
let BumperEvent = require('./BumperEvent.js');
let DigitalOutput = require('./DigitalOutput.js');
let ButtonEvent = require('./ButtonEvent.js');
let PowerSystemEvent = require('./PowerSystemEvent.js');
let ScanAngle = require('./ScanAngle.js');
let DockInfraRed = require('./DockInfraRed.js');
let SensorState = require('./SensorState.js');
let Led = require('./Led.js');
let WheelDropEvent = require('./WheelDropEvent.js');
let CliffEvent = require('./CliffEvent.js');
let RobotStateEvent = require('./RobotStateEvent.js');
let VersionInfo = require('./VersionInfo.js');
let DigitalInputEvent = require('./DigitalInputEvent.js');
let Sound = require('./Sound.js');
let MotorPower = require('./MotorPower.js');
let AutoDockingAction = require('./AutoDockingAction.js');
let AutoDockingActionFeedback = require('./AutoDockingActionFeedback.js');
let AutoDockingGoal = require('./AutoDockingGoal.js');
let AutoDockingActionResult = require('./AutoDockingActionResult.js');
let AutoDockingResult = require('./AutoDockingResult.js');
let AutoDockingActionGoal = require('./AutoDockingActionGoal.js');
let AutoDockingFeedback = require('./AutoDockingFeedback.js');

module.exports = {
  KeyboardInput: KeyboardInput,
  ControllerInfo: ControllerInfo,
  ExternalPower: ExternalPower,
  BumperEvent: BumperEvent,
  DigitalOutput: DigitalOutput,
  ButtonEvent: ButtonEvent,
  PowerSystemEvent: PowerSystemEvent,
  ScanAngle: ScanAngle,
  DockInfraRed: DockInfraRed,
  SensorState: SensorState,
  Led: Led,
  WheelDropEvent: WheelDropEvent,
  CliffEvent: CliffEvent,
  RobotStateEvent: RobotStateEvent,
  VersionInfo: VersionInfo,
  DigitalInputEvent: DigitalInputEvent,
  Sound: Sound,
  MotorPower: MotorPower,
  AutoDockingAction: AutoDockingAction,
  AutoDockingActionFeedback: AutoDockingActionFeedback,
  AutoDockingGoal: AutoDockingGoal,
  AutoDockingActionResult: AutoDockingActionResult,
  AutoDockingResult: AutoDockingResult,
  AutoDockingActionGoal: AutoDockingActionGoal,
  AutoDockingFeedback: AutoDockingFeedback,
};
