import os
from pathlib import Path
from typing import List, Dict

file_name_and_path_dict: List[Dict[str, str]] = [
    {'file_name': "a123456", 'file_path': 'aaaaa'}
]


def read_CBETA_filename_name_and_path_list(path_of_CBETA: str) -> [Dict[str, str]]:
    path = Path(path_of_CBETA)
    dirs = [e for e in path.iterdir() if e.is_dir()]
    file_name_and_path_dict: List[Dict[str, str]] =[]
    for dir in dirs:
        files_list_in_one_folder: List[str] = os.listdir(dir)
        for file in files_list_in_one_folder:
            name_and_path_dict:Dict[str,str]={'file_name':file,'file_path':str(dir)+'\\'+file}
            file_name_and_path_dict.append(name_and_path_dict)
    return file_name_and_path_dict


def read_txt_file_name_into_list(path_of_name_file_txt: str) -> List[str]:
    with open(path_of_name_file_txt, 'r', encoding='utf-8') as f:
        content: List[str] = list(f)
        file_name_list_in_txt: List[str] = []
        for file_name in content[2:]:
            file_name_list_in_txt.append(file_name.strip())
        return file_name_list_in_txt


def rename_epub_file(path:str,file_name_txt:str,file_type:str='epub')->None:
    file_name_list_in_txt=read_txt_file_name_into_list(file_name_txt)
    file_name_and_path_dict=read_CBETA_filename_name_and_path_list(path)
    for file_name in file_name_list_in_txt:
        want_to_use_file_name:str=file_name
        file_name_using_num_in_list:str=file_name.split(',')[0].strip()

        for file_and_path in file_name_and_path_dict:
            file_name_num:str=file_and_path['file_name'].split('.')[0].strip()
            # print(file_name_num)
            if file_name_num==file_name_using_num_in_list:
                old_filename_and_path:str=file_and_path['file_path']
                new_filename_and_path_element:list=old_filename_and_path.split('\\')[:-1]
                new_file_path:str=('\\').join(new_filename_and_path_element)
                new_filename_and_path:str=new_file_path+'\\'+want_to_use_file_name+'.'+file_type
                try:
                    os.rename(old_filename_and_path, new_filename_and_path)
                    print('完成文件重命名，命名后文件为：',new_filename_and_path)
                except Exception as e:
                    print(e)
                    with open('error.txt','a',encoding='utf-8') as f:
                        f.write(str(e))
                        f.write('\\n')


if __name__ == '__main__':
    path_of_CBETA = 'D:\CODE\PYTHON\cbeta_epub_2022q4'
    file_name_txt = 'D:\CODE\PYTHON\cbeta_epub_2022q4\\filelist_2022q4.txt'
    rename_epub_file(path_of_CBETA,file_name_txt)

