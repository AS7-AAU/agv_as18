#!/usr/bin/env python

import rospy as rp
import message_filters
import math 

from agv_as18.msg import Right_encoder as encoder_r
from agv_as18.msg import Left_encoder as encoder_l
from agv_as18.msg import Motor as motor
"""from agv_as18.msg import Left_sp as sp_left
from agv_as18.msg import Right_sp as sp_right """






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



	def update(self, encoder_signal):

		"""

		Calculate PID output value for given reference input and feedback

		"""

		process_value = encoder_signal  #describing PV in 0-100%
		

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
def encoder_left(enc_left):

	global enc_l
	enc_l = enc_left


def encoder_right( enc_right):

	global enc_r
	enc_r = enc_right
	

if __name__=="__main__":
	
	rp.init_node("pid")
	rp.Subscriber("encoder_signal_left", encoder_l, encoder_left)	
	rp.Subscriber("encoder_signal_right", encoder_r, encoder_right)
	pub = rp.Publisher("motor_signal", motor, queue_size=1)
	
	
	try:
		while not rp.is_shutdown():
			
			
		        controller_right = PID()
			controller_right.setPoint(30)
			pid_r = controller_right.update(encoder_signal=enc_r)
				
		        controller_left = PID()
			controller_left.setPoint(30)
			pid_l = controller_left.update(encoder_signal=-enc_l)
				
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
		
			
			msg = motor()
			msg.b = pid_l/5.4
			msg.a = pid_r/5.4
			pub.publish(msg)
			 
	except rp.ROSInterruptException:
		destroy()
