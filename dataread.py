import torch
import numpy as np
import torch.nn as nn
import torch.utils.data as data
import torchvision
import torchvision.transforms as transforms
from torch import nn,optim
from torch.autograd import Variable
from tqdm import tqdm
import torch.nn.functional as func
import matplotlib.pyplot as plt
import torch.utils.data as Data
import time
import os
import csv

def get_data(path):
    if path=="./sjtu3d/train_val":
        csv_file=csv.reader(open("./sjtu3d/train_val.csv",'r'))
    else:
        csv_file=csv.reader(open("./sjtu3d/test.csv",'r'))
    content=[]
    for line in csv_file:
        content.append(line)
    data_len=len(content)
    data_voxel=[]
    data_seg=[]
    label=[]
    
    for i in range(1,data_len):
        data_path=path+'/'+content[i][0]+".npz"
        tmp=np.load(data_path)
        y=[];h=[]
        seg=tmp['seg'];voxel=tmp['voxel']*(tmp['seg']*0.8+0.2)
        seg=seg.astype(int);voxel=voxel/255
        seg=seg.tolist()
        for j in seg[30:70]:
            x=[]
            for k in j[30:70]:
                x.append(k[30:70])
            y.append(x)
        #data.append(tmp)
        for j in voxel[30:70]:
            vox=[]
            for k in j[30:70]:
                vox.append(k[30:70])
            h.append(vox)
        data_seg.append(y);data_voxel.append(h)
        la=float(int(content[i][1])-int('0'))
        label.append(la)
    return data_seg,label,content,data_voxel
