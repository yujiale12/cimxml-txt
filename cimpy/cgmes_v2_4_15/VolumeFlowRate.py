from .Base import Base


class VolumeFlowRate(Base):
	'''
	Volume per time.

	:denominatorMultiplier:  Default: None
	:denominatorUnit:  Default: None
	:multiplier:  Default: None
	:unit:  Default: None
	:value:  Default: 0.0
		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						'denominatorMultiplier': [cgmesProfile.DY.value, ],
						'denominatorUnit': [cgmesProfile.DY.value, ],
						'multiplier': [cgmesProfile.DY.value, ],
						'unit': [cgmesProfile.DY.value, ],
						'value': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self, denominatorMultiplier = None, denominatorUnit = None, multiplier = None, unit = None, value = 0.0,  ):
	
		self.denominatorMultiplier = denominatorMultiplier
		self.denominatorUnit = denominatorUnit
		self.multiplier = multiplier
		self.unit = unit
		self.value = value
		
	def __str__(self):
		str = 'class=VolumeFlowRate\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
