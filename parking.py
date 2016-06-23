import RPi.GPIO as GPIO
import time

class ParkingLot(object):

	def __init__(self):
		self.IN1 = 11
		self.IN2 = 12
		self.IN3 = 13
		self.IN4 = 15
		self.status = 0

	def setStep(self, w1, w2, w3, w4):
		GPIO.output(self.IN1, w1)
		GPIO.output(self.IN2, w2)
		GPIO.output(self.IN3, w3)
		GPIO.output(self.IN4, w4)

	def stop(self):
		self.setStep(0, 0, 0, 0)

	def forward(self, delay, steps):
		for i in range(0, steps):
			self.setStep(1, 0, 0, 0)
			time.sleep(delay)
			self.setStep(0, 1, 0, 0)
			time.sleep(delay)
			self.setStep(0, 0, 1, 0)
			time.sleep(delay)
			self.setStep(0, 0, 0, 1)
			time.sleep(delay)

	def backward(self, delay, steps):
		for i in range(0, steps):
			self.setStep(0, 0, 0, 1)
			time.sleep(delay)
			self.setStep(0, 0, 1, 0)
			time.sleep(delay)
			self.setStep(0, 1, 0, 0)
			time.sleep(delay)
			self.setStep(1, 0, 0, 0)
			time.sleep(delay)

	def openGate(self):
		if self.status == 0:
			return "Gate already opened!"
		else:
			self.backward(0.005, 128)
			self.stop()
			time.sleep(0.5)	
			self.status = 0			
			return "Gate opened!"

	def closeGate(self):
		if self.status == 1:
			return "Gate already closed!"
		else:
			self.forward(0.005, 128)
			self.stop()
			time.sleep(0.5)
			self.status = 1
			return "Gate closed!"			


	def setup(self):
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
		GPIO.setup(self.IN1, GPIO.OUT)      # Set pin's mode is output
		GPIO.setup(self.IN2, GPIO.OUT)
		GPIO.setup(self.IN3, GPIO.OUT)
		GPIO.setup(self.IN4, GPIO.OUT)

	def destroy(self):
		GPIO.cleanup()







	
	

