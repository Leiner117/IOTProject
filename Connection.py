from qgis.core import QgsApplication, QgsProject
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
if project.read(project_path):
    # El proyecto se ha cargado correctamente

    # Obtener información del proyecto
    project_title = project.title()
    project_crs = project.crs().authid()

    # Obtener una lista de las capas del proyecto
    layers = project.mapLayers()

    # Imprimir información del proyecto
    print("Título del proyecto:", project_title)
    print("Sistema de coordenadas de referencia (CRS):", project_crs)
    print("Capas del proyecto:")
    for layer_id, layer in layers.items():
        print("  - Nombre:", layer.name())
        print("    Tipo:", layer.providerType())
        print("    CRS:", layer.crs().authid())

    # Configurar la carpeta de salida para los archivos web
    output_folder = "ruta/de/la/carpeta/de/salida"

    # Crear la carpeta de salida si no existe
    os.makedirs(output_folder, exist_ok=True)

    # Generar los archivos web utilizando qgis2web
    subprocess.run(['C:/Program Files/QGIS 3.30.2/bin/qgis.bat', '--project', project_path, '--code', 'qgis.utils.plugins["qgis2web"].run("'+output_folder+'")'])


    # Imprimir mensaje de finalización
    print("Se ha generado el mapa web en la carpeta de salida:", output_folder)
else:
    print("Error al cargar el proyecto")

# Cerrar la aplicación QGIS
qgs.exitQgis()
