# Deep Learning for COVID19 detection in CT images 


This is a classificator to detect signs of SARS-CoV-2 pneumonia in CT scans. This is the first step of a major pipeline, currently under development, intended to analyze the existence, distribution, and extension of the Covid19 characteristic lesions such as ground-glass opacification, pleural effusion, and consolidation.


# Dataset

The model was trained with labeled Covid19 and normal images from the data base in [1] after converting them to NIfTI format. The figure shows an example of a normal subject (left) and an infected subject exhibiting the typical ground-glass pattern.

<p align="center">
  <img src="Crudas_png/IM0635_cruda.png" width="400" title="cruda1"> <img src="Crudas_png/IM0044_cruda.png" width="400" title="seg1">
</p>


A total number of 108 subjects (54 positives for Covid19 and 54 normal) was employed. Each image is a slice of a CT volume containing approximately 200 slices. Images positives for Covid19 are labeled by experts as expalined in [1]. Normal images are sampled uniformly form a volume of a normal patient. The slice distribution on normal and Covid19 images is shown in the figure where <img src="https://render.githubusercontent.com/render/math?math=z\in\[0, 1]"> is the normalized position of the slice, i.e. <img src="https://render.githubusercontent.com/render/math?math=z=0"> is the first slice and <img src="https://render.githubusercontent.com/render/math?math=z=1"> the last one.


 

<p align="center">
  <img src="covid_dist.png" width="400" title="cruda1"> <img src="normal_dist.png" width="400" title="seg1">
</p>



The table summarizes the distridution of samples in each dataset. 

Set| Number of samples | % of Covid19 positives
--- | --- | ---
Training | 5318| 50
Validation | 1486| 48
Test | 755| 53


# Model

The model was developped using Keras/Tensorflow.
Architecture: DenseNet121 with a sigmoid activation layer that represents the probability of being positive for Covid19. This configuration is inspired in [2] where it was shown to be efficient for X-ray classification.

# Training

The model was trained with a GeForce GTX 1650 Ti GPU. A validation set was used to monitor the progress of the training, for instance the leraning rate was adapted when the accuracy on the validation set platoed. 

 
Setting | Value
--- | --- 
Loss function | binary crossentropy
Epochs | 20
Learning rate | 0.00005 (adaptive)
Optimizer | Adam
 

# Results

The table shows the outcomes of the assesment on the testing set, figure shows the ROC curve.

Metric | Value
--- | --- 
True positives | 401
True negatives | 296
False positives | 53
False negatives | 2
Accuracy | 0.92
Loss | 0.19
Misclassification rate |  0.07
AUC | 0.9


<p align="center">
  <img src="ROC.png" width="400" title="seg1">
</p>

<!-- Para las TACs mostradas arriba (extraídas del conjunto de testeo) las probabilidades predichas son P=0.9993 para el caso positivo y P=0.0260 para el caso negativo. 

 <a name="myfootnote1">1</a>: La cantidad es insuficiente para asegurar los resultados pero se prevé aumentar los datos de entrenamiento.
 
 
  -->
# Further analysis using Gradcam

<p align="center">
  
  <img src="Crudas_png/IM0635_cruda.png" width="400" title="cruda1"> <img src="Crudas_png/IM0044_cruda.png" width="400" title="seg1">
  
  <img src="Crudas_png/IM0635_mascara.png" width="400" title="seg1"><img src="Crudas_png/IM0044_mascara.png" width="400" title="seg1">
  
  <img src="IMG_prueba/Segmentadas_png/IM0635_seg.png" width="400" title="seg1"><img src="IMG_prueba/Segmentadas_png/IM0044_seg.png" width="400" title="seg1">
  

</p> 

Previo a la clasificación, se requiere una segmentación, se pueden encontrar varios repositorios con herramientas de segmentación eficientes, por ejemplo: https://github.com/JoHof/lungmask. 

# References
[1] Afshar, P., Heidarian, S., Enshaei, N. et al. COVID-CT-MD, COVID-19 computed tomography scan dataset applicable in machine learning and deep learning. Sci Data 8, 121 (2021). https://doi.org/10.1038/s41597-021-00900-3

[2] Pranav Rajpurkar ,Jeremy Irvin ,Robyn L. Ball,Kaylie Zhu et al. Deep learning for chest radiograph diagnosis: A retrospective comparison of the CheXNeXt algorithm to practicing radiologists PLOS Medicine, November 2018.
https://dx.plos.org/10.1371/journal.pmed.1002686


