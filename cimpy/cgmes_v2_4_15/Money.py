from .Base import Base


class Money(Base):
	'''
	Amount of money.

	:unit:  Default: None
	:multiplier:  Default: None
	:value:  Default: 0.0
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, ],
						'unit': [cgmesProfile.EQ.value, ],
						'multiplier': [cgmesProfile.EQ.value, ],
						'value': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, unit = None, multiplier = None, value = 0.0,  ):
	
		self.unit = unit
		self.multiplier = multiplier
		self.value = value
		
	def __str__(self):
		str = 'class=Money\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
