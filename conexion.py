from qgis.core import *

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
    print("bien")
    # El proyecto se ha cargado correctamente
else:
    print("Error al cargar el proyecto")

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

# Cerrar el proyecto
project.clear()