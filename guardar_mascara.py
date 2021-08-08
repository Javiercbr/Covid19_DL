from lungmask import mask
import SimpleITK as sitk
import numpy as np
import pandas as pd
import os, os.path
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

 



DIR = 'C:/Users/javie/Documents/Covid19/Proyecto_clasificacion_CT_3/DBnii/'

 
writer = sitk.ImageFileWriter()

 
img = sitk.ReadImage(DIR + 'IM0044_cruda' +'.nii')
        
segmentation = mask.apply(img,batch_size=1) 
mascara    = segmentation>0
writer.SetFileName('IM0044_mascara'+'.png')
writer.Execute(mascara)

img = sitk.ReadImage(DIR + 'IM0635_cruda' +'.nii')
        
segmentation = mask.apply(img,batch_size=1) 
mascara    = segmentation>0
writer.SetFileName('IM0635_mascara'+'.png')
writer.Execute(mascara)
