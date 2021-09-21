'''
方法1：创建一个txt文件，文件名为mytxtfile,并向文件写入msg
'''
'''
def text_create(name, msg):
    desktop_path = "C:\\Users\\Administrator\\Desktop\\"  # 新创建的txt文件的存放路径
    full_path = desktop_path + name + '.txt'  # 也可以创建一个.doc的word文档
    file = open(full_path, 'w')
    file.write(msg)  # msg也就是下面的Hello world!
    # file.close()

text_create('mytxtfile', 'Hello world!')
# 调用函数创建一个名为mytxtfile的.txt文件，并向其写入Hello world!
'''



'''
方法二，另一种写入方法，主要应该就是用这一种
'''
zifu1 = 'a'
zifu2 = 'b'
zifu3 = 'c'

name = 'shuju'
desktop_path = "C:\\Users\\Administrator\\Desktop\\"  # 新创建的txt文件的存放路径
full_path = desktop_path + name + '.txt'  # 也可以创建一个.doc的word文档
file_handle = open(full_path, mode='w')   #直接写的话，file_handle = open('1.txt', mode='w')

file_handle.write('hello world 你好 \n')   #不加换行符下一行不换行，与print不同
file_handle.write('%6s%6s%6s' % (zifu1, zifu2, zifu3)) #主要应用此种方法
#file_handle.writelines(['hello', 'world', '你好'])
file_handle.close()

