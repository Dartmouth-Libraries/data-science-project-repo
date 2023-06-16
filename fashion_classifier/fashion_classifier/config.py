"""
Special paths and variables that are used throughout the project
are placed here
"""
from pathlib import Path

import torch
from torchvision.transforms import ToTensor, Lambda

project_root = Path(Path(__file__).parent / '../..')
data_dir = project_root / 'data'
model_dir = project_root / 'models'

transform = ToTensor()
target_transform = Lambda(
    lambda y: torch.zeros(10, dtype=torch.float).scatter_(0, torch.tensor(y),
                                                          value=1))
