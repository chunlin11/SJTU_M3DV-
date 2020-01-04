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
from mylenet3d import LeNet3D,LeNet3D1
from newnet import LeNet13D
from myresnet3d import resnet3d
from mytest3d import test_model
from mytrain13d import trainmodel
from mytrain23d import trainmodel1

# preprocessing
normalize = transforms.Normalize(mean=[.5], std=[.5])
transform = transforms.Compose([transforms.ToTensor(), normalize])
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
'''
def thre_data(data_test,data_tevoxel):
    return data_test*data_tevoxel
'''
if __name__ == "__main__":

    model1= LeNet3D1()
    model1=model1.to(device)

    model2=LeNet3D()
    model2=model2.to(device)

    data_train,data_label,c,data_trvoxel=get_data('./sjtu3d/train_val')
    data_test,te_label,conte,data_tevoxel=get_data('./sjtu3d/test')

    #TODO:model1
    filename="D:/test/Submission1.csv"
    print("---------Letnet3d--without--dropout------------")
    model1,x_axi,all_loss=trainmodel(model1,data_train,data_label,c,11)
    print("---------Letnet3d--with-----dropout------------")
    model2,x_axi1,all_loss1=trainmodel(model2,data_train,data_label,c,12)
    test_model(model1,model2,data_test,conte,filename)

    all_loss=all_loss
    X=np.linspace(0,x_axi,x_axi,endpoint=True)
    plt.plot(X,all_loss)
    plt.show()
