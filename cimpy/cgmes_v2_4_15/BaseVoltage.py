from .IdentifiedObject import IdentifiedObject


class BaseVoltage(IdentifiedObject):
	'''
	Defines a system base voltage which is referenced.

	:nominalVoltage: The power system resource`s base voltage. Default: 0.0
	:ConductingEquipment: Base voltage of this conducting equipment.  Use only when there is no voltage level container used and only one base voltage applies.  For example, not used for transformers. Default: "list"
	:VoltageLevel: The voltage levels having this base voltage. Default: "list"
	:TransformerEnds: Transformer ends at the base voltage.  This is essential for PU calculation. Default: "list"
	:TopologicalNode: The topological nodes at the base voltage. Default: "list"
		'''

	cgmesProfile = IdentifiedObject.cgmesProfile

	possibleProfileList = {'class': [cgmesProfile.EQ.value, cgmesProfile.TP.value, cgmesProfile.TP_BD.value, cgmesProfile.EQ_BD.value, ],
						'nominalVoltage': [cgmesProfile.EQ.value, cgmesProfile.EQ_BD.value, ],
						'ConductingEquipment': [cgmesProfile.EQ.value, ],
						'VoltageLevel': [cgmesProfile.EQ.value, ],
						'TransformerEnds': [cgmesProfile.EQ.value, ],
						'TopologicalNode': [cgmesProfile.TP.value, cgmesProfile.TP_BD.value, ],
						 }

	serializationProfile = {}

	__doc__ += '\n Documentation of parent class IdentifiedObject: \n' + IdentifiedObject.__doc__ 

	def __init__(self, nominalVoltage = 0.0, ConductingEquipment = "list", VoltageLevel = "list", TransformerEnds = "list", TopologicalNode = "list",  *args, **kw_args):
		super().__init__(*args, **kw_args)
	
		self.nominalVoltage = nominalVoltage
		self.ConductingEquipment = ConductingEquipment
		self.VoltageLevel = VoltageLevel
		self.TransformerEnds = TransformerEnds
		self.TopologicalNode = TopologicalNode
		
	def __str__(self):
		str = 'class=BaseVoltage\n'
		attributes = self.__dict__
		for key in attributes.keys():
			str = str + key + '={}\n'.format(attributes[key])
		return str
