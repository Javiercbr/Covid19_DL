from tensorflow.keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
import SimpleITK as sitk
# from lungmask import mask
import cv2




def load_image_nii(img, image_dir, H=256, W=256):
    
 
    
    img_path = image_dir + '\\' + img
     
   
    
    image       = sitk.ReadImage(img_path)

    image_arr   = sitk.GetArrayFromImage(image )
    image_arr   = cv2.resize(image_arr[0,:,:] , dsize=(H,W ),interpolation=cv2.INTER_NEAREST)
    image_arr   = np.stack( (image_arr,image_arr,image_arr), 2)
    image_arr   = np.expand_dims(image_arr, axis=0)
     
    return  image_arr 


 


modeloCovid = load_model('modeloCovid.h5')
IMAGE_DIR = ".\IMG_prueba"


X = load_image_nii('IM2048_cruda.nii', IMAGE_DIR)

pred = modeloCovid.predict(X)


print("Porbability: ", pred)



X = X[0]
X = (X-X.min())/(X.max()-X.min())
plt.imshow(X)
plt.title('Probability: P= {}'.format(pred[0])) 
plt.show()
 

X = load_image_nii('IM6508_cruda.nii', IMAGE_DIR)

pred = modeloCovid.predict(X)


print("Porbability: ", pred)



X = X[0]
X = (X-X.min())/(X.max()-X.min())
plt.imshow(X)
plt.title('Probability: P= {}'.format(pred[0])) 
plt.show()
 

 
input() 