#!/usr/bin/env python
import rospy as rp
import math 
from std_msgs.msg import Float32
from agv_as18.msg import Motor, Reference

class PID:
	"""
	Discrete PID control
	"""

	def __init__(self, P=1.0, I=0.1, D=0.0, Derivator=0.0, Integrator=0.0, Integrator_max=500, Integrator_min=-500, set_point=0.0):
		self.Kp=P
		self.Ki=I
		self.Kd=D
		self.Derivator=Derivator
		self.Integrator=Integrator
		self.Integrator_max=Integrator_max
		self.Integrator_min=Integrator_min
		self.set_point=set_point
		self.error=0.0

	def update(self, process_value):
		"""
		Calculate PID output value for given reference input and feedback
		"""

		self.error = self.set_point - process_value
		self.P_value = self.Kp * self.error
		self.D_value = self.Kd * ( self.error - self.Derivator)
		self.Derivator = self.error
		self.Integrator = self.Integrator + self.error

		if self.Integrator > self.Integrator_max:
			self.Integrator = self.Integrator_max
		elif self.Integrator < self.Integrator_min:
			self.Integrator = self.Integrator_min
		self.I_value = self.Integrator * self.Ki

		PID = self.P_value + self.I_value + self.D_value
		return PID

	def setPoint(self, set_point):
		"""
		Initilize the setpoint of PID
		"""
		self.set_point = set_point
		self.Integrator=0
		self.Derivator=0

	def setIntegrator(self, Integrator):
		self.Integrator = Integrator

	def setDerivator(self, Derivator):
		self.Derivator = Derivator

	def setKp(self, P):
		self.Kp = P

	def setKi(self, I):
		self.Ki = I

	def setKd(self,D):
		self.Kd = D

	def getPoint(self):
		return self.set_point

	def getError(self):
		return self.error

	def getIntegrator(self):
		return self.Integrator

	def getDerivator(self):
		return self.Derivator

## Get messages ##
enc_r = 0.0
enc_l = 0.0
omega_a=0.0
omega_b=0.0

def encoder_left(enc_left):
	global enc_l
	enc_l = enc_left

def encoder_right(enc_right):
	global enc_r
	enc_r = enc_right

def cmd_vel_cb(data):
	global omega_a
	global omega_b
	omega_a = data.v
	omega_b = data.omega

if __name__=="__main__":	
	rp.init_node("pid")
	rp.Subscriber("encoder_signal_left", encoder_l, encoder_left)	
	rp.Subscriber("encoder_signal_right", encoder_r, encoder_right)
	rp.Subscriber("cmd_vel", Reference, cmd_vel_cb)
	pub = rp.Publisher("motor_signal", Motor, queue_size=1)
	
	try:
		while not rp.is_shutdown():			
		    controller_right = PID()
			if controller_right.getPoint() != omega_a:
				controller_right.setPoint(omega_a)
			pid_r = controller_right.update(enc_r)
				
		    controller_left = PID()
			if controller_left.getPoint() != omega_b:
				controller_left.setPoint(omega_b)
			pid_l = controller_left.update(-enc_l)
				
			# Saturated the signal
			if pid_r > 54:
				pid_r = 54
			if pid_r < -54:
				pid_r = -54

			# Saturated the signal
			if pid_l > 54:
				pid_l = 54
			if pid_l < -54:
				pid_l = -54

			pub.publish(pid_r, pid_l)
			 
	except rp.ROSInterruptException:
		destroy()
