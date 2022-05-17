# TotoBot-V2
El repositorio de TotoBot V2
## Como probar el código con tu propio bot de pruebas
1. Instala las librerias necesarias (Cuando vaya agregando comandos voy a actualizar esta lista) utilizando el comando "pip install nombre-de-la-libreria", estas son:
  - beautifulsoup4
  - discord
  - requests
  - discord.py
  - regex
  - mysql-connector-python
  - python-dotenv
2. Crea un archivo .env en la carpeta del bot
3. Pon las siguientes variables:
  - TOKEN="TOKEN DE TU BOT DE PRUEBAS"
  - SERVER_1="[ES]Hispania - Paracode"
  - CHANNEL_ID_SERVER_1="ID DEL CANAL PARA ANUNCIAR POR EL SERVER 1"
  - SERVER_2="[ES]Hispania - CEV Eris"
  - CHANNEL_ID_SERVER_2="ID DEL CANAL PARA ANUNCIAR POR EL SERVER 2"
  - HISPANIA_HOST_DATABASE="IP base de datos del servidor de SS13"
  - HISPANIA_PORT_DATABASE="Puerto de la base de datos"
  - HISPANIA_USER_DATABASE="Usuario con el que ingresas a la base de datos"
  - HISPANIA_PASSWORD_DATABASE="Contraseña de la base de datos"
  - HISPANIA_NAME_DATABASE="Nombre de la base de datos"
  - DISCORD_HOST_DATABASE="IP base de datos del bot"
  - DISCORD_PORT_DATABASE="Puerto de la base de datos"
  - DISCORD_USER_DATABASE="Usuario con el que ingresas a la base de datos"
  - DISCORD_PASSWORD_DATABASE="Contraseña de la base de datos"
  - DISCORD_NAME_DATABASE="Nombre de la base de datos"

4. Ejecuta el archivo main.py, si tienes las librerias necesarias el código debería ejecutarse bien
