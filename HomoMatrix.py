import math
from MatrixPro import HariMatrix
from napolita import Napolita

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


	def getHomoMatrix(self, accuracy):
		a = Napolita(str(self.a))
		alpha = self.alpha
		d = Napolita(str(self.d))
		theta = self.theta

		def sin(angleInDegrees):
			return round(math.sin(DHRow.getRadians(angleInDegrees)), 7)

		def cos(angleInDegrees):
			return round(math.cos(DHRow.getRadians(angleInDegrees)), 7)
		print(str(cos(alpha)))

		ct = Napolita(str(cos(theta)))
		st = Napolita(str(sin(theta)))
		ca = Napolita(str(cos(alpha)))
		sa = Napolita(str(sin(alpha)))

		HomoMatrix = [
			[ct, (st*ca)*-1, st*sa, ct*a],
			[st, ct*ca, (ca*st)*-1, st*a],
			[0, sa, ca, d],
			[0, 0, 0, 1]
		]
		HomoMatrix = HariMatrix(HomoMatrix)
		return HomoMatrix.getBeautyStringProFraction(accuracy)


