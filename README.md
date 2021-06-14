# Algoritmos Deep Learning para el estudio de Covid19 en imágenes de TAC de tórax. 

Acá se presenta una etapa básica de un pipeline mayor donde se identifican los cortes tomográficos que exhiben lesiones de Covid19. El objetivo final del pipeline, actualmente en desarrollo, es la cuantificación de la extensión de los distintos tipos de lesiones características de la neumonía por SARS-CoV-2 (Ground-glass opacification, pleural effusion, consolidation, etc.) mediante el uso de técnicas de segmentación.

# Dataset

El modelo fue entrenado con cortes tomográficos axiales extraídos de la base de datos [1], la información de los pacientes fue debidamente eliminada de acuerdo a los protocolos de imágenes médicas. En las imágenes se muestran dos cortes de pacientes diferentes. La columna izquierda corresponde a una paciente normal mientras las imágenes a la derecha exhiben el patrón típico de la neumonía por Covid19: opacidades tipo vidrio esmerilado de predominio periférico. La primera fila muestra la imagen original y la segunda la imagen segmentada y la tercera muestra la máscara multiplicativa usada en la segmentación para conservar solo los pixeles correspondientes al pulmón. 


<p align="center">
  <img src="Crudas_png/IM0635_cruda.png" width="400" title="cruda1"> <img src="Crudas_png/IM0044_cruda.png" width="400" title="seg1">
  <img src="IMG_prueba/Segmentadas_png/IM0635_seg.png" width="400" title="seg1"><img src="IMG_prueba/Segmentadas_png/IM0044_seg.png" width="400" title="seg1">
  <img src="Crudas_png/IM0635_mascara.png" width="400" title="seg1"><img src="Crudas_png/IM0044_mascara.png" width="400" title="seg1">
  

</p>

# Modelo

El modelo consiste en una DenseNet121 con una capa de salida con una activación sigmoidea y entrega una probabilidad de que la imagen sea positiva para Covid19. Se utilizó la API de Keras. La arquitectura se inspiró en [2] donde se demostró la eficacia de estas configuraciones para la clasificación multiclase, i.e. varias patologías, de radiografías de tórax. Previo a la clasificación, se requiere una segmentación, se pueden encontrar varios repositorios con herramientas de segmentación eficientes, por ejemplo: https://github.com/JoHof/lungmask. 

# Entrenamiento

El entrenamiento se realizó sobre un conjunto de más de 1200 cortes pertenecientes a 108 pacientes separados en conjuntos de entrenamiento, validación y testeo. Se respetó el balance entre casos normales y positivos (entre 48-53% en cada conjunto). Se utilizó un optimizador Adam con un learning rate adaptativo (valor inicial de 0.0001) y binary cross entropy como función de perdida. El algoritmo se entreno en una GPU GeForce GTX 1650 Ti con early stopping al alcanzar una meseta en la pérdida medida para el conjunto de validación.

# Resultados

Se obtuvo una accuracy final de 0.923 (loss=0.227) una matriz de confusión con VP=60, VN=60, FP=9 y FN=1 y un misclassification rate de 0.083. En la figura se muestra la curva ROC.

<p align="center">
  <img src="ROC.png" width="400" title="seg1">
</p>

Para las TACs mostradas arriba (extraidas del conjunto de testeo) las probabilidades predichas son P=0.9993 para el caso positivo y P=0.0260 para el caso negativo.

# Referencias

[1] Afshar, P., Heidarian, S., Enshaei, N. et al. COVID-CT-MD, COVID-19 computed tomography scan dataset applicable in machine learning and deep learning. Sci Data 8, 121 (2021). https://doi.org/10.1038/s41597-021-00900-3

[2] Pranav Rajpurkar ,Jeremy Irvin ,Robyn L. Ball,Kaylie Zhu et al. Deep learning for chest radiograph diagnosis: A retrospective comparison of the CheXNeXt algorithm to practicing radiologists PLOS Medicine, November 2018.
https://dx.plos.org/10.1371/journal.pmed.1002686





