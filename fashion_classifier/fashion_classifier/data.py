"""
This file contains data-related code that is used throughout the project.
"""
from .config import data_dir

from torch.utils.data import Dataset
from torchvision import datasets


def download_data():
    """ Downloads the dataset """

    datasets.FashionMNIST(
        root=data_dir,
        train=True,
        download=True
    )

    datasets.FashionMNIST(
        root=data_dir,
        train=False,
        download=True
    )


def data(train: bool, transform=None, target_transform=None) -> Dataset:
    return datasets.FashionMNIST(
        root=data_dir,
        train=train,
        download=False,
        transform=transform,
        target_transform=target_transform
    )


def training_data(transform=None, target_transform=None) -> Dataset:
    """ Returns the training data """
    return data(train=True, transform=transform,
                target_transform=target_transform)


def test_data(transform=None, target_transform=None) -> Dataset:
    """ Returns the test data """
    return data(train=False, transform=transform,
                target_transform=target_transform)
