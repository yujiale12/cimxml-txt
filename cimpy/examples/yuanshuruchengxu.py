import logging
import re
import cimpy
from pathlib import Path


logging.basicConfig(filename='importCIGREMV.log', level=logging.INFO, filemode='w')

example = Path(__file__).resolve().parent

# called as cimpy.examples.import_example() or file run from quickstart directory?
if 'cimexamples.py' in str(__file__):
    sample_folder = example / 'examples' / 'sampledata' / 'CIGRE_MV'
else:
    sample_folder = example / 'sampledata' / 'CIGRE_MV'
print(sample_folder)
sample_files = sample_folder.glob('*.xml')
print(sample_files)
xml_files = []
for file in sample_folder.glob('*.xml'):
    xml_files.append(str(file.absolute()))

import_result = cimpy.cim_import(xml_files, "cgmes_v2_4_15")
print("\n\n")
'''上面是导入xml文件的内容'''




results = [ "ACLineSegment"]
for key, value in import_result['topology'].items():
    if value.__class__.__name__ in results:
        #print(value.__str__())
        #print(value.name)


        str1 = value.name
        shuzi = re.findall( "\d+", str1)
        print(shuzi)




#print(value.LoadResponse.name)


       # if value.ConductingEquipment.__class__.__name__ != "NoneType":
        #    print(value.ConductingEquipment.__class__.__name__)

'''
str="abc123abd223"
I = re.sub("\D", "", str)
for item in I:
    print(item)
'''