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
