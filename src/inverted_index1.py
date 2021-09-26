import os
import json
from utilities.utility_constants import ROOT_DIR
from utilities.utility_constants import generated_files_dir
from utilities.utility_methods import calculate_time


class SearchEngine:
    def __init__(self, root_path):
        self.root_path = root_path
        self.lookup_index = {}
        self.index_file_path = os.path.join(generated_files_dir, "email_index.json")
        self.initialize_data()

    def initialize_data(self):
        if os.path.exists(self.index_file_path):
            with open(self.index_file_path, "r") as fr:
                self.lookup_index = json.load(fr)

    def search_files(self, term):
        result = []
        for path, sub_dir, files in os.walk(self.root_path):
            if files:
                for file in files:
                    file_path = os.path.join(path, file)
                    with open(file_path, "r") as fr:
                        text = fr.read().strip().lower()
                        if term in text:
                            result.append(file_path)
        return result

    def search_term(self, term):
        if term in self.lookup_index:
            return self.lookup_index[term]
        else:
            search_result = self.search_files(term)
            if search_result:
                self.lookup_index[term] = search_result
                with open(self.index_file_path, "w") as fw:
                    json.dump(self.lookup_index, fw)
            return search_result


@calculate_time
def kickstart():
    # (if you want search any other folder in skiling j just need to change "inbox" to "name of subdirectory")
    root_path = os.path.join(ROOT_DIR, "skilling-j", "inbox") 
    se = SearchEngine(root_path)
    term = input("Enter text to search: ").strip()
    result = se.search_term(term.lower())
    result_file = os.path.join(generated_files_dir, "search_result_text.txt")
    print(f"Found {len(result)} search results..")
    print("Find you result in file:\n{}".format(result_file))
    with open(result_file, "w") as fw:
        fw.write("You searched for: " + term + "\n")
        fw.write("\n".join(result))


kickstart()

