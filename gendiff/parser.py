from generator import is_yaml, dict_diff
import json
import yaml


def generate_diff(path_file1, path_file2):
    with open(path_file1, 'r') as f1, open(path_file2, 'r') as f2:

        if is_yaml(path_file1) and is_yaml(path_file2):
            file1 = yaml.safe_load(f1)
            file2 = yaml.safe_load(f2)
        else:
            file1 = json.load(f1)
            file2 = json.load(f2)

    return dict_diff(file1, file2)
