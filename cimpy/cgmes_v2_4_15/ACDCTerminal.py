from .IdentifiedObject import IdentifiedObject


class ACDCTerminal(IdentifiedObject):
	'''
	An electrical connection point (AC or DC) to a piece of conducting equipment. Terminals are connected at physical connection points called connectivity nodes.

	:BusNameMarker: The bus name marker used to name the bus (topological node). Default: None
	:sequenceNumber: The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the `starting point` for a two terminal branch. Default: 0
	:OperationalLimitSet:  Default: "list"
	:Measurements: Measurements associated with this terminal defining  where the measurement is placed in the network topology.  It may be used, for instance, to capture the sensor position, such as a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. Default: "list"
	:connected: The connected status is related to a bus-branch model and the topological node to terminal relation.  True implies the terminal is connected to the related topological node and false implies it is not.  In a bus-branch model, the connected status is used to tell if equipment is disconnected without having to change the connectivity described by the topological node to terminal relation. A valid case is that conducting equipment can be connected in one end and open in the other. In particular for an AC line segment, where the reactive line charging can be significant, this is a relevant case. Default: False
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.SSH.value, cgmesProfile.SV.value, cgmesProfile.DY.value, cgmesProfile.TP.value, ],
						'BusNameMarker': [cgmesProfile.EQ.value, ],
						'sequenceNumber': [cgmesProfile.EQ.value, ],
						'OperationalLimitSet': [cgmesProfile.EQ.value, ],
						'Measurements': [cgmesProfile.EQ.value, ],
						'connected': [cgmesProfile.SSH.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, BusNameMarker = None, sequenceNumber = 0, OperationalLimitSet = "list", Measurements = "list", connected = False,  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.BusNameMarker = BusNameMarker
		self.sequenceNumber = sequenceNumber
		self.OperationalLimitSet = OperationalLimitSet
		self.Measurements = Measurements
		self.connected = connected
		
	def __str__(self):
		str = 'class=ACDCTerminal\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
