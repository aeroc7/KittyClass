import hparams
import torchvision.transforms.functional as tvf
import torchvision.transforms as transforms
import pathlib
import torch

from torch.utils.data import Dataset
from PIL import Image


class PetData(Dataset):
    def __init__(self, transforms=None):
        self.path = hparams.DATASET_PATH
        self.transforms = transforms
        self.data = []

        for dir in ['Cat/', 'Dog/']:
            for f in pathlib.Path(self.path + dir).iterdir():
                if f.is_file() and (f.stat().st_size > 0):
                    if f.name.find('.jpg') != -1:
                        if dir == 'Cat/':
                            self.data.append((dir + f.name, 1))
                        elif dir == 'Dog/':
                            self.data.append((dir + f.name, 0))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        finpath = self.path + self.data[index][0]

        img = Image.open(finpath).convert('RGB')
        img = tvf.pil_to_tensor(img).type(dtype=torch.FloatTensor)

        ctrnsfms = transforms.Compose([
            transforms.Resize(hparams.DATASET_IMAGE_SIZE)
        ])

        img = ctrnsfms(img)

        img = img.reshape(
            (3, hparams.DATASET_IMAGE_SIZE[0], hparams.DATASET_IMAGE_SIZE[1]))

        if not self.transforms:
            img = self.transforms(img)

        return img, self.data[index][1]
