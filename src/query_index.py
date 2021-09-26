import os
import json
from utilities.utility_constants import generated_files_dir, ROOT_DIR


def search_term(term, index_result, text_list):
    if term in index_result:
        print(f'{term} occurs in following lines:\n--------------------------')
        for i in index_result[term]:
            print(text_list[i])
    else:
        print("Not Found!!!")


def start_execution():
    index_file_path = os.path.join(generated_files_dir, 'index_result.json')
    with open(index_file_path, "r") as fr:
        index_dict = json.load(fr)
        term = input("Enter term to search: ").strip()
        with open(os.path.join(ROOT_DIR, "data_files", "data1.txt"), "r") as fr1:
            text_list = fr1.read().strip().splitlines()
            # print(text_list)
            search_term(term.lower(), index_dict, text_list)


start_execution()

"""
whole email: From , To, Subject, CC, BCC, content, Date,
From: User can give anything to look email in From list
To: User can give anything to look email in From list
Cc: User can give anything to look email in From list
Bcc: User can give anything to look email in From list
Content: Look for tem only in content
Date: 

"""