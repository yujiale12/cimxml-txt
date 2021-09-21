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




#下输出数据到shuju.txt文档中
name = 'shuju'                                        #名称为数据
desktop_path = "C:\\Users\\Administrator\\Desktop\\"  # 新创建的txt文件的存放路径
full_path = desktop_path + name + '.txt'              # 也可以创建一个.doc的word文档
file_handle = open(full_path, mode='w')               # 直接写的话，file_handle = open('1.txt', mode='w')
file_handle.write('九节点系统示例 \n')

'''
# 输出线路数据到shuju.txt文档中 ACLineSegment
# 格式见raw文件格式说明无变压器支路数据（Non_Transformer Branch Data）P16-P17
# 可以通过结尾的方法把电流限制CurrentLimit加进来。
file_handle.write(' 0 \ BEGIN TRANSMISSION LINE DATA\n')
file_handle.write('%12s%12s%12s%12s%12s%12s%12s%12s%12s%12s%12s\n' % ('I', 'J', 'BV', 'bch', 'gch', 'r', 'x', 'b0ch', 'g0ch', 'r0', 'x0'))
for key, value in import_result['topology'].items():
    if value.__class__.__name__ in "ACLineSegment":
        str1 = value.name
        shuzi = re.sub("\D", "", str1)
        shumu = 0
        line1 = [0, 0]
        for item in shuzi:
            line1[shumu] = item
            shumu = shumu + 1
        file_handle.write('%12s%12s%12.0f%12.3f%12.3f%12.3f%12.3f%12.3f%12.3f%12.3f%12.3f\n' % (line1[0], line1[1], value.BaseVoltage.nominalVoltage, value.bch, value.gch, value.r, value.x, value.b0ch, value.g0ch, value.r0, value.x0))



# 输出负载数据到shuju.txt文档中 EnergyConsumer
file_handle.write(' 0 \ END OF TRANSMISSION LINE DATA, BEGIN LOAD DATA\n')
file_handle.write('%12s%12s%12s%12s%12s%12s%12s%12s%12s\n' % ('I', 'name', 'leixing', 'pfixed', 'pfixedPct', 'qfixed', 'qfixedPct', 'p', 'q'))
for key, value in import_result['topology'].items():
    if value.__class__.__name__ in "EnergyConsumer":
       #从Terminal模块中取出连接到哪个节点上
       load = [0, 0, 0, 0, 0, 0, 0, 0, 0]
       value1 = value             #存起来，便于循环后使用，因为value的值已经改变
       fuzaibiaozhi = value.mRID  #判断负载连接到哪个节点的一个判断条件
       for key, value in import_result['topology'].items():
           if value.__class__.__name__ in "Terminal":
               if value.ConductingEquipment.__class__.__name__ != "NoneType":  #注意注意此处NoneType的处理
                  if value.ConductingEquipment.mRID == fuzaibiaozhi:
                     load[0] = value.TopologicalNode.name
       #重新对EnergyConsumer模块进行操作
       value = value1
       load[1] = value.name
       load[2] = value.LoadResponse.name
       load[3] = value.pfixed
       load[4] = value.pfixedPct
       load[5] = value.qfixed
       load[6] = value.qfixedPct
       load[7] = value.p
       load[8] = value.q
       file_handle.write('%12s%12s%12s%12.3f%12.3f%12.3f%12.3f%12.3f%12.3f\n' % (load[0], load[1], load[2], load[3], load[4], load[5], load[6], load[7], load[8]))
'''