import math
from MatrixPro import HariMatrix

class DHRow():
	def __init__(self, a, alpha, d, theta):
		self.a = a
		self.alpha = alpha
		self.d = d
		self.theta = theta

	@classmethod
	def getRadians(cls, angleInDegrees):
		angleInRadians = angleInDegrees*math.pi/180
		return angleInRadians


	def getHomoMatrix(self):
		a = self.a
		alpha = self.alpha
		d = self.d
		theta = self.theta
		
		def sin(angleInDegrees):
			return math.sin(DHRow.getRadians(angleInDegrees))

		def cos(angleInDegrees):
			return math.cos(DHRow.getRadians(angleInDegrees))
		HomoMatrix = [
			[cos(theta), -sin(theta)*cos(alpha), sin(theta)*sin(alpha), a*cos(theta)],
			[sin(theta), cos(theta)*cos(alpha), -cos(theta)*sin(alpha), a*sin(theta)],
			[0, sin(alpha), cos(alpha), d],
			[0, 0, 0, 1]
		]
		HomoMatrix = HariMatrix(HomoMatrix)
		print(HomoMatrix.getBeautyStringPro())


