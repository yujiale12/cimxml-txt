from .PowerSystemResource import PowerSystemResource


class ControlArea(PowerSystemResource):
	'''
	A control areais a grouping of generating units and/or loads and a cutset of tie lines (as terminals) which may be used for a variety of purposes including automatic generation control, powerflow solution area interchange control specification, and input to load forecasting.   Note that any number of overlapping control area specifications can be superimposed on the physical model.

	:type: The primary type of control area definition used to determine if this is used for automatic generation control, for planning interchange control, or other purposes.   A control area specified with primary type of automatic generation control could still be forecast and used as an interchange area in power flow analysis. Default: None
	:TieFlow: The tie flows associated with the control area. Default: "list"
	:ControlAreaGeneratingUnit: The generating unit specificaitons for the control area. Default: "list"
	:EnergyArea: The energy area that is forecast from this control area specification. Default: None
	:netInterchange: The specified positive net interchange into the control area, i.e. positive sign means flow in to the area. Default: 0.0
	:pTolerance: Active power net interchange tolerance Default: 0.0
		'''

	cgmesProfile = PowerSystemResource.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.SSH.value, ],
						'type': [cgmesProfile.EQ.value, ],
						'TieFlow': [cgmesProfile.EQ.value, ],
						'ControlAreaGeneratingUnit': [cgmesProfile.EQ.value, ],
						'EnergyArea': [cgmesProfile.EQ.value, ],
						'netInterchange': [cgmesProfile.SSH.value, ],
						'pTolerance': [cgmesProfile.SSH.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class PowerSystemResource: \n' + PowerSystemResource.__doc__ 

	def __init__(self, type = None, TieFlow = "list", ControlAreaGeneratingUnit = "list", EnergyArea = None, netInterchange = 0.0, pTolerance = 0.0,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.type = type
		self.TieFlow = TieFlow
		self.ControlAreaGeneratingUnit = ControlAreaGeneratingUnit
		self.EnergyArea = EnergyArea
		self.netInterchange = netInterchange
		self.pTolerance = pTolerance
		
	def __str__(self):
		str = 'class=ControlArea\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
