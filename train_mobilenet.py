import os
import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# Define the data directory
data_dir = r'C:\Users\AFREEN\Desktop\TrafficManagement\datasets\classification'

# Print the data directory and check its contents
print("Data directory:", data_dir)
if not os.path.exists(data_dir):
    print("The data directory does not exist!")
else:
    print("Contents of the data directory:")
    print(os.listdir(data_dir))

# Define image transformations
data_transforms = {
    'train': transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ]),
    'val': transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ]),
}

# Load the datasets
try:
    image_datasets = {x: datasets.ImageFolder(os.path.join(data_dir, x), data_transforms[x])
                      for x in ['train', 'val']}
    dataloaders = {x: DataLoader(image_datasets[x], batch_size=32, shuffle=True)
                   for x in ['train', 'val']}

    print("Datasets loaded successfully!")
    for phase in ['train', 'val']:
        print(f"{phase} dataset size: {len(image_datasets[phase])}")

except FileNotFoundError as e:
    print("FileNotFoundError: Ensure that the directory structure is correct and images are in place.")
    print(e)

except Exception as e:
    print("An error occurred:")
    print(e)
