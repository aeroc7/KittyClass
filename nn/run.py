import torch
import torchvision.models as models
import torch.nn.functional as F
import torchvision.transforms as transforms
import torchvision.transforms.functional as tvf


class RunModel():
    def __init__(self, model_file, transforms):
        self.net = models.resnet18()
        self.net.load_state_dict(torch.load(
            model_file, map_location=self.device()))
        self.net.to(device=self.device())
        self.transforms = transforms

    def device(self):
        return torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    def transform_img(self, img):
        img = tvf.pil_to_tensor(img).type(dtype=torch.FloatTensor)

        ctrnsfms = transforms.Compose([
            transforms.Resize((178, 104)),
            transforms.CenterCrop((445, 260))
        ])

        img = ctrnsfms(img)

        # First dimension represents batch_size (of 1 in this case)
        img = img.reshape((1, 3, 445, 260))

        if not self.transforms:
            img = self.transforms(img)

        return img

    def run_model(self, img):
        self.net.eval()

        img = self.transform_img(img)

        img = img.to(device=self.device())
        output = self.net(img)

        pred = output.max(1).indices
        probs = F.softmax(output, dim=1)
        conf, _ = torch.max(probs, 1)

        return (pred[0], conf[0])


def pred_num_to_str(pred):
    if pred == 1:
        return 'cat'
    elif pred == 0:
        return 'dog'
    else:
        raise Exception("Invalid input number")


def nn_run_image(img):
    rm = RunModel('model.pt', transforms=transforms.ToTensor())
    pred, conf = rm.run_model(img)

    pred = pred_num_to_str(pred)

    return bytes(f'{pred},{conf*100:.2f}', encoding='utf-8')
