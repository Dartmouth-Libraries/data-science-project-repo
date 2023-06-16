"""
Retrieves the dataset from the web and
places it in the project's data folder
"""
from fashion_classifier.config import data_dir

from torchvision import datasets
from torchvision.transforms import ToTensor


training_data = datasets.FashionMNIST(
    root=data_dir,
    train=True,
    download=True,
    transform=ToTensor()
)

test_data = datasets.FashionMNIST(
    root=data_dir,
    train=False,
    download=True,
    transform=ToTensor()
)
