from .Base import Base


class WindLookupTableFunctionKind(Base):
	'''
	Function of the lookup table.

		'''

	cgmesProfile = Base.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.DY.value, ],
						 }

	serializationProfile = {}

	

	def __init__(self,  ):
	
		pass
	
	def __str__(self):
		str = 'class=WindLookupTableFunctionKind\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
