import os
import json
import csv
import pickle


def get_dir_size(folder):
    total_size = 0
    for root, dirs, files in os.walk(folder):
        for name in files:
            path = os.path.join(root, name)
            total_size += os.path.getsize(path)
        for name in dirs:
            path = os.path.join(root, name)
            total_size += get_dir_size(path)
    return total_size


def traverse_directory(folder):
    result_list = []
    for root, dirs, files in os.walk(folder):
        for name in files:
            path = os.path.join(root, name)
            size = os.path.getsize(path)
            result_list.append({'Path': path, 'Type': 'File', 'Size': size})
        for name in dirs:
            path = os.path.join(root, name)
            size = get_dir_size(path)
            result_list.append({'Path': path, 'Type': 'Directory', 'Size': size})
    return result_list


def save_results_to_json(output, filename):
    with open(filename, 'w') as f:
        json.dump(output, f, indent=4)


def save_results_to_csv(output, filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Path', 'Type', 'Size'])
        writer.writeheader()
        for result in output:
            writer.writerow(result)


def save_results_to_pickle(output, filename):
    with open(filename, 'wb') as f:
        pickle.dump(output, f)


directory = 'test_dir'
results = traverse_directory(directory)

save_results_to_json(results, 'results_JSON.json')
save_results_to_csv(results, 'results_CSV.csv')
save_results_to_pickle(results, 'results_PICKLE.pkl')
