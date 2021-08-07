# Deep Learning for COVID19 detection in CT images 


This is a classificator to detect signs of SARS-CoV-2 pneumonia in CT scans. This is the first step of a major pipeline, currently under development, intended to analyze the existence, distribution, and extension of the Covid19 characteristic lesions such as ground-glass opacification, pleural effusion, and consolidation.


# Dataset

The model was trained with labeled Covid19 and normal images from the data base in [1] after converting them to NIfTI format. The figure shows an example of a normal subject (left) and an infected subject exhibiting the typical ground-glass pattern.

<p align="center">
  <img src="Crudas_png/IM0635_cruda.png" width="400" title="cruda1"> <img src="Crudas_png/IM0044_cruda.png" width="400" title="seg1">
</p>
The table summarizes 

Attempt | #1 | #2 | #3 | #4 | #5 | #6 | #7 | #8 | #9 | #10 | #11
--- | --- | --- | --- |--- |--- |--- |--- |--- |--- |--- |---
Seconds | 301 | 283 | 290 | 286 | 289 | 285 | 287 | 287 | 272 | 276 | 269



# Modelo

El modelo se confeccionó con la API de Keras. La arquitectura consiste en una DenseNet121 con una capa de salida con una activación sigmoidea y entrega la probabilidad de que la imagen sea positiva para Covid19. La arquitectura se inspiró en [2] donde se demostró la eficacia de estas configuraciones para la clasificación multiclase, i.e. varias patologías, de radiografías de tórax. Previo a la clasificación, se requiere una segmentación, se pueden encontrar varios repositorios con herramientas de segmentación eficientes, por ejemplo: https://github.com/JoHof/lungmask. 

# Entrenamiento

El entrenamiento se realizó sobre un conjunto de alrededor de 700 <sup>[1](#myfootnote1)</sup> cortes pertenecientes a 108 pacientes separados en conjuntos de entrenamiento, validación y testeo. Se mantuvo el balance entre casos normales y positivos (entre 48-53% en cada conjunto). Se utilizó un optimizador Adam con un learning rate adaptativo (valor inicial de 0.0001) y binary cross entropy como función de perdida. El algoritmo se entrenó en una GPU GeForce GTX 1650 Ti con early stopping al alcanzar una meseta en la pérdida medida para el conjunto de validación.

# Resultados

Se obtuvo una accuracy final de 0.923 (loss=0.227) una matriz de confusión con VP=60, VN=60, FP=9 y FN=1 y un misclassification rate de 0.083. En la figura se muestra la curva ROC.

<p align="center">
  <img src="ROC.png" width="400" title="seg1">
</p>

Para las TACs mostradas arriba (extraídas del conjunto de testeo) las probabilidades predichas son P=0.9993 para el caso positivo y P=0.0260 para el caso negativo. 

 <a name="myfootnote1">1</a>: La cantidad es insuficiente para asegurar los resultados pero se prevé aumentar los datos de entrenamiento.
 
 
 
# Further analysis 

<p align="center">
  
  <img src="Crudas_png/IM0635_cruda.png" width="400" title="cruda1"> <img src="Crudas_png/IM0044_cruda.png" width="400" title="seg1">
  
  <img src="Crudas_png/IM0635_mascara.png" width="400" title="seg1"><img src="Crudas_png/IM0044_mascara.png" width="400" title="seg1">
  
  <img src="IMG_prueba/Segmentadas_png/IM0635_seg.png" width="400" title="seg1"><img src="IMG_prueba/Segmentadas_png/IM0044_seg.png" width="400" title="seg1">
  

</p> 

# Referencias

[1] Afshar, P., Heidarian, S., Enshaei, N. et al. COVID-CT-MD, COVID-19 computed tomography scan dataset applicable in machine learning and deep learning. Sci Data 8, 121 (2021). https://doi.org/10.1038/s41597-021-00900-3

[2] Pranav Rajpurkar ,Jeremy Irvin ,Robyn L. Ball,Kaylie Zhu et al. Deep learning for chest radiograph diagnosis: A retrospective comparison of the CheXNeXt algorithm to practicing radiologists PLOS Medicine, November 2018.
https://dx.plos.org/10.1371/journal.pmed.1002686


