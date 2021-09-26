import os
import json
from utilities.utility_constants import ROOT_DIR

result = {}


def create_index(root_path):
    for path, sub_dir, files in os.walk(root_path):
        if files:
            for file in files:
                file_path = os.path.join(path, file)
                with open(file_path, "r") as fr:
                    text = fr.read().strip()



def start_execution():
    result_dict = {}
    text_list = []
    with open(os.path.join(ROOT_DIR, "data_files", "data1.txt"), "r") as fr:
        text_list = fr.read().strip().splitlines()
    # text_list = ["Python is a very easy language.", "Python is not python snake"]
    for i in range(len(text_list)):
        item = text_list[i].lower()
        words = item.strip().split()
        for word in words:
            if word in result_dict:
                index_list = result_dict[word]
                if i not in index_list:
                    index_list.append(i)
            else:
                result_dict[word] = [i]

    # print(json.dumps(result_dict))
    dir_name = os.path.join(ROOT_DIR, 'generated_files')
    os.makedirs(dir_name, exist_ok=True)
    with open(os.path.join(dir_name, 'index_result.json'), 'w') as fw:
        json.dump(result_dict, fw)
    # root_path = r"D:\python related\projects\enron-search\skilling-j\skilling-j\inbox"
    # create_index(root_path)


start_execution()
