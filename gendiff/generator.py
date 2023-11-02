import json


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

    result = json.dumps(diff, indent=2)
    return result.replace('"', '').replace(',', '')
