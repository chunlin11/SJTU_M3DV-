import torch
import numpy as np
import torch.nn as nn
import torchvision
import matplotlib.pyplot as plt
import torch.utils.data as Data
from tqdm import tqdm
import os
import csv
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def test_model(model1,model2,data_test,conte,filename):
    file=open(filename,'w',newline='')
    csv_write=csv.writer(file)
    csv_write.writerow(["Id","Predicted"])
    i=0
    model1.eval()
    model2.eval()
    for data in tqdm(data_test):
        voxel=np.array(data)
        voxel=torch.tensor(voxel).float()
        voxel=voxel.view(-1,1,40,40,40)
        voxel=voxel.to(device)
        out=model1(voxel)
        out2=model2(voxel)
        a=out.tolist()
        a1=out2.tolist()
        row=[conte[i+1][0],0.2119*a[0][1]/(a[0][0]+a[0][1])+0.7881*a1[0][1]/(a1[0][0]+a1[0][1])]
        csv_write.writerow(row)
        i+=1
    file.close()