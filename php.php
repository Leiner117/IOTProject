<?php


$conexion = pg_connect("host=localhost dbname=ruteo_aceras_2023 user=postgres password=root");

$query = "select st_asgeojson(aceras.geom) from aceras inner join  pgr_dijkstra('SELECT id,source, target, distancia as cost FROM aceras',1, 2, directed => false) as ruta on (aceras.id=ruta.edge)";
$consulta = pg_query($conexion,$query);


while($obj=pg_fetch_object($consulta)){
echo($obj->st_asgeojson);
}


?>