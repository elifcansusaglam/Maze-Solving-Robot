import gym
import rospy
import roslaunch
import time
import numpy as np
from gym import utils, spaces
from gym_gazebo.envs import gazebo_env
from geometry_msgs.msg import Twist, Point
from std_srvs.srv import Empty
from nav_msgs.msg import Odometry
from std_msgs.msg import Empty as odomEmpty
from sensor_msgs.msg import LaserScan
from gym.utils import seeding

#Initial position of the robot
INIT_X = 0.0
INIT_Y = 0.0
#Size of the map(M)
STAGE_X_MIN = -4.0
STAGE_X_MAX =  4.0
STAGE_Y_MIN = -4.0
STAGE_Y_MAX =  4.0

FS_MARKER_SIZE = 0.2

EXIT = 6



class GazeboMazeTurtlebotLidarEnv(gazebo_env.GazeboEnv):
   
    def __init__(self):
        # Launch the simulation with the given launchfile name
        gazebo_env.GazeboEnv.__init__(self, "GazeboMazeTurtlebotLidar_v0.launch")
        self.vel_pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=5)
        self.unpause = rospy.ServiceProxy('/gazebo/unpause_physics', Empty)
        self.pause = rospy.ServiceProxy('/gazebo/pause_physics', Empty)
        self.reset_proxy = rospy.ServiceProxy('/gazebo/reset_simulation', Empty)
        self.reset_world = rospy.ServiceProxy('/gazebo/reset_world', Empty)
        self.action_space = spaces.Discrete(3)
        self.reward_range = (-np.inf, np.inf)
        self.reset_pub = rospy.Publisher("mobile_base/commands/reset_odometry", odomEmpty, queue_size=10)
        self._seed()
        self.right = 0
        self.left = 0
        self.front = 0
        self.x = INIT_X
        self.y = INIT_Y
        self.fs_marker = np.zeros((int((STAGE_X_MAX - STAGE_X_MIN) / FS_MARKER_SIZE)+1, int((STAGE_Y_MAX - STAGE_Y_MIN) / FS_MARKER_SIZE)+1))
        self.last_position_x = self.x
        self.last_position_u = self.y
        self.last_fs_mark_position = self.calc_fs_mark_position(self.x,self.y)
    
        
        rospy.Subscriber('odom', Odometry, self.callback)
        rospy.Subscriber('/mybot/laser/scan', LaserScan, self.data_func)
        
        
        
    def callback(self,data):
        self.x = data.pose.pose.position.x
        self.y = data.pose.pose.position.y

    def reset_world(self):
        rospy.wait_for_service('/gazebo/reset_world')
        self.reset_world = rospy.ServiceProxy('/gazebo/reset_world', Empty)
        
    def discretize_observation(self,data,new_ranges):
        discretized_ranges = []
        min_range = 0.2
        done = False
        mod = len(data.ranges)/new_ranges
        for i, item in enumerate(data.ranges):
            if (i%mod==0):
                if data.ranges[i] == float ('Inf'):
                    discretized_ranges.append(6)
                elif np.isnan(data.ranges[i]):
                    discretized_ranges.append(0)
                else:
                    discretized_ranges.append(int(data.ranges[i]))
            if (min_range > data.ranges[i] > 0):
                done = True
        return discretized_ranges,done

    def _seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def data_func(self,data):
        self.right = min(min(data.ranges[0:287]), 30)
        self.front = min(min(data.ranges[288:431]), 30)
        self.left = min(min(data.ranges[432:719]), 30)

    def calc_fs_mark_position(self, x,y):
        mx = int((x - STAGE_X_MIN)/ FS_MARKER_SIZE)
        my = int((y - STAGE_Y_MIN)/ FS_MARKER_SIZE)
        
        if mx < 0 : mx = 0
        elif mx >= len(self.fs_marker) : mx = len(self.fs_marker) - 1

        if my < 0 : my = 0
        elif my >= len(self.fs_marker[0]) : my = len(self.fs_marker[0]) - 1
        
        return mx, my
        
    def step(self, action):

        rospy.wait_for_service('/gazebo/unpause_physics')
        try:
            self.unpause()
        except (rospy.ServiceException) as e:
            print ("/gazebo/unpause_physics service call failed")

        if action == 0: #FORWARD
            vel_cmd = Twist()
            vel_cmd.linear.x = 0.3
            vel_cmd.angular.z = 0.0
            self.vel_pub.publish(vel_cmd)
        elif action == 1: #LEFT
            vel_cmd = Twist()
            vel_cmd.linear.x = 0.05
            vel_cmd.angular.z = 0.3
            self.vel_pub.publish(vel_cmd)
        elif action == 2: #RIGHT
            vel_cmd = Twist()
            vel_cmd.linear.x = 0.05
            vel_cmd.angular.z = -0.3
            self.vel_pub.publish(vel_cmd)
      

        data = None
        while data is None:
            try:
                data = rospy.wait_for_message('/scan', LaserScan, timeout=5)
            except:
                pass

        rospy.wait_for_service('/gazebo/pause_physics')
        try:
            #resp_pause = pause.call()
            self.pause()
        except (rospy.ServiceException) as e:
            print ("/gazebo/pause_physics service call failed")

        state,done = self.discretize_observation(data,5)
        footstep_marker = self.calc_fs_mark_position(self.x, self.y)

        if not done:
            if self.last_position_x >= EXIT  :
                reward = 1000
                print("Congrats u reach the exit")
                done = True
            elif action == 0 and (self.right <= 0.29 or self.front <= 0.29 or self.left <= 0.29) :
                reward = -2
            elif action == 0 and (self.right >= 0.3 or self.front >= 0.3 or self.left >= 0.3) :
                reward = -1
            elif (action == 1 or action == 2) and (self.right <= 0.29 or self.front <= 0.29 or self.left <= 0.29)  :
                reward = -2
            else:
                reward = -1 
        else:
            reward = -100
        
        if not self.last_fs_mark_position == footstep_marker:
            if self.fs_marker[footstep_marker[0]][footstep_marker[1]] > 1:
                reward = -50
                print("Robot went through the same way 2 times.Episode resetting...")
                done = True
            elif self.fs_marker[footstep_marker[0]][footstep_marker[1]] > 0:
                reward = reward * 0.01
                print("Robot went through the same way.Reward reduced.")
            self.fs_marker[footstep_marker[0]][footstep_marker[1]] += 1
            self.last_fs_mark_position = footstep_marker
            
        self.last_position_x = self.x
        self.last_position_y = self.y 
        
        return state, reward, done, {}
    
    def reset(self):
        
        # Resets the state of the environment and returns an initial observation.
        rospy.wait_for_service('/gazebo/reset_simulation')
        try:
            #reset_proxy.call()
            self.reset_proxy()
        except (rospy.ServiceException) as e:
            print ("/gazebo/reset_simulation service call failed")
            
        rospy.wait_for_service('/gazebo/reset_world')
        try:
            self.reset_world()
        except (rospy.ServiceException) as e:
            print("/gazebo/reset_world service call failed")

        # Unpause simulation to make observation
        rospy.wait_for_service('/gazebo/unpause_physics')
        try:
            #resp_pause = pause.call()
            self.unpause()
        except (rospy.ServiceException) as e:
            print ("/gazebo/unpause_physics service call failed")

        #read laser data
        data = None
        while data is None:
            try:
                data = rospy.wait_for_message('/scan', LaserScan, timeout=5)
            except:
                pass

        rospy.wait_for_service('/gazebo/pause_physics')
        try:
            #resp_pause = pause.call()
            self.pause()
        except (rospy.ServiceException) as e:
            print ("/gazebo/pause_physics service call failed")
    
        state = self.discretize_observation(data,5)
        self.x = INIT_X
        self.y = INIT_Y
        self.fs_marker = np.zeros((int((STAGE_X_MAX - STAGE_X_MIN) / FS_MARKER_SIZE)+1, int((STAGE_Y_MAX - STAGE_Y_MIN) / FS_MARKER_SIZE)+1))
        self.last_position_x = self.x
        self.last_position_y = self.y
        self.last_fs_mark_position = self.calc_fs_mark_position(self.x, self.y)

        self.reset_pub.publish(odomEmpty())

        time.sleep(1)
         
        return state
