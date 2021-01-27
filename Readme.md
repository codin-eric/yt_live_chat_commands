# Youtube Live Chat
Proyecto para tomar comandos desde el chat del vivo de youtube y reproducir distintos comandos.

# Funcionamiento.
Al pasarle tu `CHANNEL_ID` yt_live_chat_commands busca una transmisión en vivo y levanta el 
`chat_id`. Una vez que tiene tu `chat_id` empieza a traer todos los mensajes 

## Instalación
clonar el repo
```
git clone https://github.com/codin-eric/yt_live_chat_commands.git
cd yt_live_chat_commands
```

### Variables de entorno
debes definir las siguientes variables

```
API_KEY=API_KEY_DE_GOOLE
CHANNELID=TU_CHANNEL_ID
```

O puedes crear un archivo `settings.ini` con la siguiente estructura

```
[settings]
API_KEY=API_KEY_DE_GOOLE
CHANNELID=TU_CHANNEL_ID
```

## Correr `yt_live_chat_commands` 
### Poetry

```
poetry install
poetry yt_live_chat_commands/main.py
```

## Objetivos

- [x] Conseguir el chatid
- [x] Parsear el texto
- [x] Activar algún script
- [x] Parametrizar sonidos
- [x] Cambiar la logica del flag en `live_chat.scan_chat`
- [x] Hacer que al iniciar no ejecute comandos
- [x] Cambiar prints por logs
- [x] Implementar metodo !luz
- [x] Conseguir información de los viewers
- [x] Parsear la información de los viewers 
- [x] guardar la información de cada mensaje en un archivo
- [x] .cache file -> id_chat y paginación
- [x] No guardar datos cuando el df está vacio
- [x] Guardar datos de viewers en archivos separados en carpeta `data`
- [x] Agregar timestamp al .cache para deprecarlo 
- [ ] Agregar una validación de Pathlib para crear el folder `data` 
- [ ] Crear una web que muestre un ranking por mayor interacción
    - [ ] Crear flask server
    - [ ] Crear endpoint que lee los archivos
    - [ ] Procesar los archivos y conseguir el top
    - [ ] Crear un index que haga AJAX al endpoint
    - [ ] Integrar index con OBS
    - [ ] Hacer un lindo CSS

# Blocked
- [ ] Enviar un mensaje de !help con los comandos habilitados
    - Necesito encontrar la forma de poder crear una cred OAth

# Backlog
- [ ] Hacer una salida segura sin Ctrl + C | check pynput https://pypi.org/project/pynput/
- [ ] Desacoplar los comandos de sonido contra otros
- [ ] Mejorar la logica de validación de comandos
- [ ] Implementar la ejecución de distintas funciones
- [ ] Limitar los llamados por usuario

# Lindo de tener
- Sonidos interesantes
    - [ ] Casi Hacker
    - [ ] Awantia
    - [ ] "Y la pizza donde esta la pizza?"
    - [ ] "Quince pesos"
    - [ ] "Esto no es coca papu"
- [ ] Implementar un deploy con docker
- [ ] Testear el proyecto en OSX y Windows
