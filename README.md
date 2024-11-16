### David Armendáriz | A01570813

Ya que los modelos se generaron en diversos archivos, la justificación y explicación de lo empleado se encuentra en el archivo 'Justification.ipynb', el cual contiene solo markdowns por simplicidad.

Los archivos de codigo de modelos son: 'Control_CNN.ipynb', 'YOLO.ipynb', 'YOLO_TUNED.ipynb'

Los archivos de codigo auxiliares son: 'Image_Handling.ipynb'

El archivo ejectuable a traves de una terminal es 'BM_Execution.py'. Este archivo utiliza el mejor modelo de los tres, (YOLO (10 EPOCHS, ADAM, MSE) sin data augmentation). Al ejecutarse este pide al
usuario el directorio de una imagen (ej, "C:\\Users\\david\\Desktop\\Cars207.png", ingresar sin comillas). Tras lo cual realiza la predicción y despliega una imagen con el cuadrante predecido de la 
placa y su nivel de confianza. Para ejectuarse correctamente, el modelo entrenado best.pt, debe estar en el mismo directorio que el BM_Execution.py.

Ya que los modelos pre entrenados y los datasets son muy pesados para github, su subieron a google drive, la liga se encuentra dentro del archivo LINK TO FILE.
Modelos entrenados:
- Control CNN: Control_Model_Detection.keras
- Control CNN DataAug: Control_Model_Detection_Augmented.keras
- **YOLO (10 EPOCHS, ADAM, MSE): best.pt, YOLOV11.pt** (son el mismo y este es el mejor de los modelos)
- YOLO DataAug (10 EPOCHS, ADAM, MSE): YOLO_AUG_E10_ADAM_MSE.pt
- YOLO DataAug (10 EPOCHS, ADAMW, MSE): YOLO_AUG_E10_ADAMW_MSE.pt
- YOLO DataAug (50 EPOCHS, ADAM, MSE): YOLO_AUG_E50_ADAM_MSE.pt

**<Estructura requerida de directorios:**
```
|
|
--> BM_Execution.ipynb
|
--> best.pt

------------------------------------------
|
|
--> augmented_control
|    |
|    --> [ ... ]
|
--> augemented_datasets
|    |
|    --> [ ... ]
|    |
|    --> data.yaml
|
--> control
|    |
|    --> [ ... ]
|
--> datasets
|    |
|    --> [ ...]
|    |
|    --> data.yaml
|
--> Control_CNN.ipynb
|
|
--> Image Handling.ipynb
|
|
--> YOLO.ipynb
|
|
--> YOLO_Tuned.ipynb

Los directorios dentro de los archivos .yaml se deben modificar para poder correr YOLO.ipynb y YOLO_Tuned.ipynb

------------------------------------------
|
|
--> Justifications.ipynb
|
|
--> YOLO_ARCHITECTURE.png
```
**Modifiqué el readme para clarificar unas cosas, pero todos los otros archivos fueron subidos dentro de la fecha límite**

