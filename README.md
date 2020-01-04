<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SJTU_M3DV项目README</title>
  <link rel="stylesheet" href="https://stackedit.io/style.css" />
</head>

<body class="stackedit">
  <div class="stackedit__html"><h1><a id="_0"></a>编译环境</h1>
<p>系统配置：Win10系统，GTX1050<br>
框架：pytorch<br>
编译工具：VSCODE</p>
<h1><a id="_5"></a>程序文件说明</h1>
<p>all.py:主程序<br>
dataread.py: 读取数据程序(需要说明的是:<strong>增加了一个test.csv文件用来保存test数据集的文件名，方便读取数据函数的统一性</strong> )<br>
mylenet3d.py:模型程序，用以生成训练和测试所用的模型<br>
mytrain13d.py:训练程序，用以训练模型，并返回loss，生成图像<br>
mytest3d.py:测试程序，用来测试数据<br>
mycutout3d.py:是数据增强的程序，实现了cutout算法<br>
fuxian.py:用来复现出最好结果的程序，加载模型的参数，并对数据集进行预测</p>
<h1><a id="_15"></a>数据文件夹说明</h1>
<p>my_model:用以存放两个模型，其中一个因为当时只保留了static_dist权重，所以显得比较小。直接放在d盘目录下面即可<br>
sjtu3d:数据集文件夹，有test和train以及读取数据需要的两个csv文件。(<strong>需要注意的是：为了方便数据集读取，增加了一个test.csv用来保存测试集文件名</strong>)<br>
test:用来保存提交所需要的Submission.csv文件，保存在d盘目录下即可。</p>
<h1><a id="KaggleSubmission_21"></a>复现Kaggle-Submission步骤</h1>
<p>1.先将sjtu3d文件夹保存在./目录下（即c盘用户目录下）。然后将给出的trian_val和test数据集保存下载到sjtu3d文件夹里面。<br>
2.模型存放位置在my_model里面，存放路径为D盘目录即可<br>
3.运行fuxian.py文件即可，寻找D盘目录下test文件夹里面的submission.csv文件即可。</p>
<h1><a id="_27"></a>数据集下载</h1>
<p>访问<a href="https://www.kaggle.com/c/sjtu-m3dv-medical-3d-voxel-classification/data">项目数据集</a>即可下载</p>
</div>
</body>

</html>
