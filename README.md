### David Armendáriz | A01570813

Ya que los modelos se generaron en diversos archivos, la justificación y explicación de lo empleado se encuentra en el archivo 'Justification.ipynb', el cual contiene solo markdowns por simplicidad.

Los archivos de codigo de modelos son: 'Control_CNN.ipynb', 'YOLO.ipynb', 'YOLO_TUNED.ipynb'

Los archivos de codigo auxiliares son: 'Image_Handling.ipynb'

El archivo ejectuable a traves de una terminal es 'BM_Execution.py'. Este archivo utiliza el mejor modelo de los tres, (YOLO (10 EPOCHS, ADAM, MSE) sin data augmentation). Al ejecutarse este pide al
usuario el directorio de una imagen (ej, "C:\\Users\\david\\Desktop\\Cars207.png", ingresar sin comillas). Tras lo cual realiza la predicción y despliega una imagen con el cuadrante predecido de la 
placa y su nivel de confianza.

Ya que los modelos pre entrenados y los datasets son muy pesados para github, su subieron a google drive, la liga se encuentra dentro del archivo LINK TO FILE.
Modelos entrenados:
- Control CNN: Control_Model_Detection.keras
- Control CNN DataAug: Control_Model_Detection_Augmented.keras
- **YOLO (10 EPOCHS, ADAM, MSE): best.pt, YOLOV11.pt**
