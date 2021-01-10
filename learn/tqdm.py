import tqdm
import time
import pathlib

# 本程序制作一个能够推出所有文件列表的文件内容，并且记录到文件中去。
def write_all_file_name(file_dir_path,output_path):
    """
    本函数实现针对给定的路径，将当前路径所有的文件内容遍历，然后打印到一个汇总文档中去

    :param file_dir_path: 给定的文件路径,str类型
    :param output_path: 输出打印文档路径,str类型
    :return:
    """
    # f = open(output_path,'a')
    try :
        path_over_all=pathlib.Path(file_dir_path)
        pass
    except:
        print(file_dir_path +'maybe some wrong')
    for x in path_over_all.iterdir():
        # print(x)
        if x.is_dir():
            if '.' in str(x):
                print(str(x))
                continue
            # f.close()
            print('dir :'+str(x))
            return write_all_file_name(str(x),output_path)
        else :
            # f.write(str(x)+'\n')
            print('file:'+str(x))
            pass

    # f.close()

dir=r'C:\Users\MILO\PycharmProjects'
outfile= r'C:\Users\MILO\PycharmProjects\Xicun_King\fil.txt'


import sys
sys.stdout=open(outfile,'a')
write_all_file_name(dir, outfile)
sys.stdout.close()