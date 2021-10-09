#!/usr/bin/env python3

import rtde_receive
import numpy as np
import roslib
import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Bool
import time

Config={
  'robot_ip':'111.11.1.1',
  'joint_ids':['shoulder_pan_joint','shoulder_lift_joint','elbow_joint','wrist_1_joint','wrist_2_joint','wrist_3_joint']
}

def rtde_update():
  if rtde_r.isConnected():
    q=rtde_r.getActualQ()
    if len(q)>=len(joints.name):
      joints.header.stamp=rospy.Time.now()
      joints.position = q
      pub_js.publish(joints)
      pub_conn.publish(mTrue)
  else:
    rtde_r.reconnect()
    print('rtde reconnect')
    time.sleep(1.0)

###############################################################
if __name__ == "__main__":
  rospy.init_node('rjoint_ur',anonymous=True)
  joints=JointState()
  joints.name=Config['joint_ids']
  try:
    Config.update(rospy.get_param('/config/rsocket'))
  except Exception as e:
    print("get_param exception:",e.args)
  pub_js=rospy.Publisher('/joint_states',JointState,queue_size=1)
  pub_conn=rospy.Publisher('/rsocket/enable',Bool,queue_size=1)
  rtde_r=rtde_receive.RTDEReceiveInterface(Config['robot_ip'])
  print("rtde connect",Config['robot_ip'])
  mTrue=Bool();mTrue.data=True
  mFalse=Bool();mFalse.data=False
  while not rospy.is_shutdown():
    rtde_update()
    time.sleep(0.1)

