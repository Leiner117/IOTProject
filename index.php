<!DOCTYPE html>
<link rel="stylesheet" type="text/css" href="style.css" media="screen" />
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
<center>

<form action="php.php" method="post">



  <h2>
    <label for="og">Ubicación de origen</label>
    </h2>
    <select name="og" id="og">
      <option value="u1">u1</option>
      <option value="u2">u2</option>
      <option value="u3">u3</option>
    </select>
    
    <h2>
        <label for="og">Ubicación destino:</label>
        </h2>
        <select name="og" id="og">
          <option value="u1">u1</option>
          <option value="u2">u2</option>
          <option value="u3">u3</option>
        </select>
    
        <br><br>
        <button type="submit" name="Enviar">Calcular Ruta</button>

</center>

</form>




</body>
</html>