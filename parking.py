import RPi.GPIO as GPIO
import time

class ParkingLot(object):

	IN1 = 11
	IN2 = 12
	IN3 = 13
	IN4 = 15

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
		print "OpenGate"
		self.backward(0.005, 128)

		self.stop()
		time.sleep(3)

	def closeGate(self):
		print "closeGate"
		self.forward(0.005, 128)

		self.stop()
		time.sleep(3)

	def setup(self):
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
		GPIO.setup(self.IN1, GPIO.OUT)      # Set pin's mode is output
		GPIO.setup(self.IN2, GPIO.OUT)
		GPIO.setup(self.IN3, GPIO.OUT)
		GPIO.setup(self.IN4, GPIO.OUT)

	def destroy(self):
		GPIO.cleanup()







	
	

