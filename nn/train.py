import torch
import hparams
import torch.nn as nn
import torch.optim as optim
import torchvision.models as models

from data import PetData
from torch.utils.data.dataset import random_split
from torch.utils.data.dataloader import DataLoader
from torchvision import transforms


class TrainPetClass():
    def __init__(self):
        #self.model = PetDataArch().to(device=self.device())
        self.model = models.efficientnet_b0(pretrained=True)
        self.model.classifier = nn.Sequential(
            nn.Dropout(p=0.2, inplace=True),
            nn.Linear(1280, 1000),
            nn.Linear(1000, 10),
        )

        self.model.to(device=self.device())

        self.loss_func = nn.CrossEntropyLoss()
        self.optimizer = optim.Adam(
            self.model.parameters(), lr=hparams.LEARNING_RATE)
        self.load_data()
        self.train_model()
        self.check_model_acc(self.train_data)
        self.check_model_acc(self.test_data)
        self.save_model()

    def device(self):
        return torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    def load_data(self):
        pet_data = PetData(transforms=transforms.ToTensor())
        train_set, test_set = random_split(
            pet_data, hparams.TRAIN_TEST_VAL_RATIO, generator=torch.Generator().manual_seed(73))

        self.train_data = DataLoader(train_set, batch_size=hparams.BATCH_SIZE, shuffle=hparams.DATASET_SHUFFLE,
                                     num_workers=hparams.DATASET_WORKERS, pin_memory=hparams.DATASET_PIN_MEMORY)
        self.test_data = DataLoader(test_set, batch_size=hparams.BATCH_SIZE, shuffle=hparams.DATASET_SHUFFLE,
                                    num_workers=hparams.DATASET_WORKERS, pin_memory=hparams.DATASET_PIN_MEMORY)

    def train_model(self):
        self.model.train()
        losses = []

        for epoch in range(hparams.NUM_EPOCHS):
            for img, label in self.train_data:
                img = img.to(device=self.device())
                label = label.to(device=self.device())

                output = self.model(img)

                # Get loss between network prediction and actual label
                loss = self.loss_func(output, label)

                losses.append(loss.item())

                loss.backward()
                self.optimizer.step()

                # Zero out parameters
                for p in self.model.parameters():
                    p.grad = None

            print(
                f'Loss at epoch {epoch + 1} (/{hparams.NUM_EPOCHS}) is {sum(losses) / len(losses)}')

    def check_model_acc(self, dataset):
        self.model.eval()

        num_correct = 0
        num_samples = 0

        with torch.no_grad():
            for img, label in dataset:
                img = img.to(device=self.device())
                label = label.to(device=self.device())

                output = self.model(img)

                _, predc = output.max(1)
                num_correct += (predc == label).sum()
                num_samples += predc.size(0)

            print(
                f'Got {num_correct} / {num_samples} with an accuracy of {float(num_correct) / float(num_samples)*100:.2f}')

    def save_model(self):
        torch.save(self.model.state_dict(), 'model.pt')


if __name__ == "__main__":
    train = TrainPetClass()
