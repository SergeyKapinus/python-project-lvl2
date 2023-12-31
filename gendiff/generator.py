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


def dict_diff(file1, file2):
    diff = {}
    keys = set(file1.keys()) | set(file2.keys())

    for key in sorted(keys):
        if key in file1 and key in file2:
            if file1[key] == file2[key]:
                diff[f'  {key}'] = file1[key]
            else:
                diff[f'- {key}'] = file1[key]
                diff[f'+ {key}'] = file2[key]
        elif key in file1:
            diff[f'- {key}'] = file1[key]
        else:
            diff[f'+ {key}'] = file2[key]

    for key in file2:
        if key not in file1:
            diff[f'+ {key}'] = file2[key]

    return create_diff_string(diff)


def create_diff_string(diff):
    result = json.dumps(diff, indent=2)
    return result.replace('"', '').replace(',', '')


def is_yaml(file):
    return file.endswith('.yaml') or file.endswith('.yml')
