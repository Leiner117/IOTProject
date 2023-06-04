from qgis.core import *
from qgis import *
import os
import subprocess



os.environ['QT_PLUGIN_PATH'] = 'C:/Program Files/QGIS 3.30.2/apps/Qt5/plugins'

# Inicializar la aplicación QGIS
QgsApplication.setPrefixPath("C:/Program Files/QGIS 3.30.2", True)
qgs = QgsApplication([], False)
qgs.initQgis()

# Establecer la ruta al proyecto de QGIS
project_path = "C:/Users/steve/Desktop/Intelectual_Stuff/U-2023/Arqui/Mapeo.qgz"

# Crear una instancia de la clase QgsProject
project = QgsProject.instance()

# Cargar el proyecto
project.read(project_path)

# Verificar si el proyecto se ha cargado correctamente
if project.read(project_path):
    print("El proyecto se ha cargado correctamente")
else:
    print("Error al cargar el proyecto")

# Obtener una lista de las capas del proyecto
layers = project.mapLayers()

# Verificar si hay capas cargadas
if len(layers) > 0:
    # Configurar la carpeta de salida para los archivos web
    output_folder = "C:/Users/steve/Desktop/x"

    # Crear la carpeta de salida si no existe
    os.makedirs(output_folder, exist_ok=True)

    # Generar los archivos web utilizando qgis2web
    subprocess.run(['C:/Program Files/QGIS 3.30.2/bin/python.exe', 'C:/Program Files/QGIS 3.30.2/apps/qgis/plugins/qgis2web/maindialog.py', '-p', project_path, '-o', output_folder])




    # Imprimir mensaje de finalización
    print("Se ha generado el mapa web en la carpeta de salida:", output_folder)
else:
    print("No se encontraron capas en el proyecto")

# Cerrar el proyecto
project.clear()

# Cerrar la aplicación QGIS
qgs.exitQgis()

print("Llegué aquí")