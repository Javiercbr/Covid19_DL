from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import matplotlib.pyplot as plt




def acondicionar_imagen(image_dir,  target_w = 256, target_h = 256):

    # normalize images
    image_generator = ImageDataGenerator(
        samplewise_center=True,
        samplewise_std_normalization= True)
    
    # flow from directory with specified batch size
    # and target image size
    generator = image_generator.flow_from_directory(image_dir, target_size=(256, 256)) 
    
 

    return generator



modeloCovid = load_model('modeloCovid.h5')
IMAGE_DIR = ".\IMG_prueba"
preprocessed_input =  acondicionar_imagen(IMAGE_DIR)
preds = modeloCovid.predict(preprocessed_input)



print("Las probabilidades de que sea positivo para Covid19 son: ")
print(preds[:,0])

x = preprocessed_input.__getitem__(0)
x=np.asarray(x[0])


for i in range(len(preds)):

    x0 = x[i]
    x0 = x0[:,:,0]
    f = plt.figure(i) 	
    plt.imshow(x0, cmap="gray", origin="upper")
    plt.title("Probabilidad de positivo: "+ str(preds[i,0]))
    f.show()

input() 