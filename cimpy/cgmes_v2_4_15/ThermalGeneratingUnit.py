from .GeneratingUnit import GeneratingUnit


class ThermalGeneratingUnit(GeneratingUnit):
	'''
	A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine.

	:FossilFuels: A thermal generating unit may have one or more fossil fuels. Default: "list"
		'''

	cgmesProfile = GeneratingUnit.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.SSH.value, ],
						'FossilFuels': [cgmesProfile.EQ.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class GeneratingUnit: \n' + GeneratingUnit.__doc__ 

	def __init__(self, FossilFuels = "list",  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.FossilFuels = FossilFuels
		
	def __str__(self):
		str = 'class=ThermalGeneratingUnit\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
