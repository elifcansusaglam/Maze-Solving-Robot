# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from kobuki_msgs/SensorState.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class SensorState(genpy.Message):
  _md5sum = "430a4bfd78449c8740bfef32b26613a6"
  _type = "kobuki_msgs/SensorState"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """# Kobuki Sensor Data Messages
#
# For more direct simple interactions (buttons, leds, gyro, motor velocity
# etc) use the other topics. This provides detailed information about the
# entire state package that is transmitted at 50Hz from the robot.
#


###### CONSTANTS ######
# Bumper states (states are combined, when multiple bumpers are pressed)
uint8 BUMPER_RIGHT  = 1
uint8 BUMPER_CENTRE = 2
uint8 BUMPER_LEFT   = 4

# Wheel drop sensor states (states are combined, when both wheel drop sensors are triggered)
uint8 WHEEL_DROP_RIGHT = 1
uint8 WHEEL_DROP_LEFT  = 2

# Cliff sensor states (states are combined, when multiple cliff sensors are triggered)
uint8 CLIFF_RIGHT  = 1
uint8 CLIFF_CENTRE = 2
uint8 CLIFF_LEFT   = 4

# Button states (only one button can be triggered at a time)
uint8 BUTTON0 = 1
uint8 BUTTON1 = 2
uint8 BUTTON2 = 4

# Charger state is a combination of charging device (adapter, docking station)
# and state (charging, charged, discharging):
uint8 DISCHARGING      = 0
uint8 DOCKING_CHARGED  = 2
uint8 DOCKING_CHARGING = 6
uint8 ADAPTER_CHARGED  = 18
uint8 ADAPTER_CHARGING = 22

# Over current states
uint8 OVER_CURRENT_LEFT_WHEEL  = 1
uint8 OVER_CURRENT_RIGHT_WHEEL = 2
uint8 OVER_CURRENT_BOTH_WHEELS = 3

# Digital input states (states are combined, when multiple inputs are set at the same time)
# When connecting Yujin's test board, it acts as pull-up what inverts the behaviour:
# No input: 79, all inputs set (e.g. buttons pressed): 64
uint8 DIGITAL_INPUT0 = 1
uint8 DIGITAL_INPUT1 = 2
uint8 DIGITAL_INPUT2 = 4
uint8 DIGITAL_INPUT3 = 8
uint8 DB25_TEST_BOARD_CONNECTED = 64

###### MESSAGE ######

Header header

###################
# Core Packet
###################
uint16 time_stamp      # milliseconds starting when turning on Kobuki (max. 65536, then starts from 0 again)
uint8  bumper          # see bumper states
uint8  wheel_drop      # see wheel drop sensor states
uint8  cliff           # see cliff sensor states
uint16 left_encoder    # accumulated ticks left wheel starting with turning on Kobuki (max. 65535)
uint16 right_encoder   # accumulated ticks right wheel starting with turning on Kobuki (max. 65535)
int8   left_pwm        # % of applied maximum voltage left wheel: -100 (max. voltage backward) to +100 (max. voltage forward)
int8   right_pwm       # % of applied maximum voltage right wheel: -100 (max. voltage backward) to +100 (max. voltage forward)
uint8  buttons         # see button states
uint8  charger         # see charger states
uint8  battery         # battery voltage in 0.1V (ex. 16.1V -> 161)

###################
# Cliff Packet
###################
uint16[] bottom        # ADC output of the right, centre, left cliff PSD sensor (0 - 4095, distance measure is non-linear)

###################
# Current Packet
###################
uint8[] current        # motor current for the left and right motor in 10mA (ex. 12 -> 120mA)
uint8   over_current   # see over current states

###################
# Input Packet
###################
uint16   digital_input # see digital input states; will show garbage when nothing is connected
uint16[] analog_input  # ADC values for the 4 analog inputs; 0 - 4095: 0.0 - 3.3V; will show garbage when nothing is connected

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id
"""
  # Pseudo-constants
  BUMPER_RIGHT = 1
  BUMPER_CENTRE = 2
  BUMPER_LEFT = 4
  WHEEL_DROP_RIGHT = 1
  WHEEL_DROP_LEFT = 2
  CLIFF_RIGHT = 1
  CLIFF_CENTRE = 2
  CLIFF_LEFT = 4
  BUTTON0 = 1
  BUTTON1 = 2
  BUTTON2 = 4
  DISCHARGING = 0
  DOCKING_CHARGED = 2
  DOCKING_CHARGING = 6
  ADAPTER_CHARGED = 18
  ADAPTER_CHARGING = 22
  OVER_CURRENT_LEFT_WHEEL = 1
  OVER_CURRENT_RIGHT_WHEEL = 2
  OVER_CURRENT_BOTH_WHEELS = 3
  DIGITAL_INPUT0 = 1
  DIGITAL_INPUT1 = 2
  DIGITAL_INPUT2 = 4
  DIGITAL_INPUT3 = 8
  DB25_TEST_BOARD_CONNECTED = 64

  __slots__ = ['header','time_stamp','bumper','wheel_drop','cliff','left_encoder','right_encoder','left_pwm','right_pwm','buttons','charger','battery','bottom','current','over_current','digital_input','analog_input']
  _slot_types = ['std_msgs/Header','uint16','uint8','uint8','uint8','uint16','uint16','int8','int8','uint8','uint8','uint8','uint16[]','uint8[]','uint8','uint16','uint16[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,time_stamp,bumper,wheel_drop,cliff,left_encoder,right_encoder,left_pwm,right_pwm,buttons,charger,battery,bottom,current,over_current,digital_input,analog_input

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SensorState, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.time_stamp is None:
        self.time_stamp = 0
      if self.bumper is None:
        self.bumper = 0
      if self.wheel_drop is None:
        self.wheel_drop = 0
      if self.cliff is None:
        self.cliff = 0
      if self.left_encoder is None:
        self.left_encoder = 0
      if self.right_encoder is None:
        self.right_encoder = 0
      if self.left_pwm is None:
        self.left_pwm = 0
      if self.right_pwm is None:
        self.right_pwm = 0
      if self.buttons is None:
        self.buttons = 0
      if self.charger is None:
        self.charger = 0
      if self.battery is None:
        self.battery = 0
      if self.bottom is None:
        self.bottom = []
      if self.current is None:
        self.current = b''
      if self.over_current is None:
        self.over_current = 0
      if self.digital_input is None:
        self.digital_input = 0
      if self.analog_input is None:
        self.analog_input = []
    else:
      self.header = std_msgs.msg.Header()
      self.time_stamp = 0
      self.bumper = 0
      self.wheel_drop = 0
      self.cliff = 0
      self.left_encoder = 0
      self.right_encoder = 0
      self.left_pwm = 0
      self.right_pwm = 0
      self.buttons = 0
      self.charger = 0
      self.battery = 0
      self.bottom = []
      self.current = b''
      self.over_current = 0
      self.digital_input = 0
      self.analog_input = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_H3B2H2b3B().pack(_x.time_stamp, _x.bumper, _x.wheel_drop, _x.cliff, _x.left_encoder, _x.right_encoder, _x.left_pwm, _x.right_pwm, _x.buttons, _x.charger, _x.battery))
      length = len(self.bottom)
      buff.write(_struct_I.pack(length))
      pattern = '<%sH'%length
      buff.write(struct.Struct(pattern).pack(*self.bottom))
      _x = self.current
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BH().pack(_x.over_current, _x.digital_input))
      length = len(self.analog_input)
      buff.write(_struct_I.pack(length))
      pattern = '<%sH'%length
      buff.write(struct.Struct(pattern).pack(*self.analog_input))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 14
      (_x.time_stamp, _x.bumper, _x.wheel_drop, _x.cliff, _x.left_encoder, _x.right_encoder, _x.left_pwm, _x.right_pwm, _x.buttons, _x.charger, _x.battery,) = _get_struct_H3B2H2b3B().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sH'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.bottom = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.current = str[start:end]
      _x = self
      start = end
      end += 3
      (_x.over_current, _x.digital_input,) = _get_struct_BH().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sH'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.analog_input = s.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_H3B2H2b3B().pack(_x.time_stamp, _x.bumper, _x.wheel_drop, _x.cliff, _x.left_encoder, _x.right_encoder, _x.left_pwm, _x.right_pwm, _x.buttons, _x.charger, _x.battery))
      length = len(self.bottom)
      buff.write(_struct_I.pack(length))
      pattern = '<%sH'%length
      buff.write(self.bottom.tostring())
      _x = self.current
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BH().pack(_x.over_current, _x.digital_input))
      length = len(self.analog_input)
      buff.write(_struct_I.pack(length))
      pattern = '<%sH'%length
      buff.write(self.analog_input.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 14
      (_x.time_stamp, _x.bumper, _x.wheel_drop, _x.cliff, _x.left_encoder, _x.right_encoder, _x.left_pwm, _x.right_pwm, _x.buttons, _x.charger, _x.battery,) = _get_struct_H3B2H2b3B().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sH'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.bottom = numpy.frombuffer(str[start:end], dtype=numpy.uint16, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.current = str[start:end]
      _x = self
      start = end
      end += 3
      (_x.over_current, _x.digital_input,) = _get_struct_BH().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sH'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.analog_input = numpy.frombuffer(str[start:end], dtype=numpy.uint16, count=length)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_BH = None
def _get_struct_BH():
    global _struct_BH
    if _struct_BH is None:
        _struct_BH = struct.Struct("<BH")
    return _struct_BH
_struct_H3B2H2b3B = None
def _get_struct_H3B2H2b3B():
    global _struct_H3B2H2b3B
    if _struct_H3B2H2b3B is None:
        _struct_H3B2H2b3B = struct.Struct("<H3B2H2b3B")
    return _struct_H3B2H2b3B
