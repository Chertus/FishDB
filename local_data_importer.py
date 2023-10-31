import torch
import csv

def load_local_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def process_data(data):
    # Convert data to PyTorch tensors for further processing
    tensor_data = torch.tensor(data)
    return tensor_data

if __name__ == "__main__":
    file_path = "path_to_your_local_data_file.csv"
    data = load_local_data(file_path)
    processed_data = process_data(data)
    print(processed_data)
