import torch
import numpy as np
import torch.nn as nn
import torch.utils.data as data
import torchvision
import torchvision.transforms as transforms
from torch import nn,optim
from torch.autograd import Variable
from tqdm import tqdm
import torch.nn.functional as F
import matplotlib.pyplot as plt
import torch.utils.data as Data
from numpy import random
import time
import os
import csv

from dataread import get_data
from mylenet3d import LeNet3D1
from mytest3d import test_model

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# preprocessing
normalize = transforms.Normalize(mean=[.5], std=[.5])
transform = transforms.Compose([transforms.ToTensor(), normalize])
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

if __name__ == "__main__":
    model1=torch.load('D:/my_model/best_model1.pth')
    model1=model1.cuda()

    model2 =LeNet3D1()  
    model2=model2.cuda()
    model2.load_state_dict(torch.load('D:/my_model/params.pth'))  
    data_test,te_label,conte,data_tevoxel=get_data('./sjtu3d/test')
    filename="D:/test/Submission.csv"
    test_model(model2,model1,data_test,conte,filename)