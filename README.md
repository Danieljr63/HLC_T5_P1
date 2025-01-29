# Práctica 1: Creación y Detección de un Keylogger en Python

En esta práctica, aprenderemos cómo programar un keylogger básico en Python y a desarrollar un programa que lo detecte y elimine.

# ✅ - Entrega y evaluación

Deberás entregar el código generado, así como subirlo a GitHub y adjuntar el enlace del repositorio (llamado SI_T5_P1). Es obligatorio incluir un archivo README.md, donde se explique cómo funciona el keylogger, áreas de mejora, como usarlo, etc.

Este es mi código:

![image](https://github.com/user-attachments/assets/841a9097-835f-4e98-9567-304dcaca8dac)

Primero desde una terminal ejecutaremos el comando "pip install keyboard" para instalar esta libreria que se ocupa de detectar los eventos pulsados por teclado tanto para windows como linux. Y lo importaremos en el script.

He creado una función llamada "pulsacionTeclas" que lo que hara es ejecutarse cada vez que se pulse una tecla que contiene dentro el argumentos "teclas" que contiene las teclas que se presionan en el teclado.

La siguiente linea abre un archivo llamado "teclas.txt" en modo append que se usa para poder añadir teclas al archivo cada vez que se presionan y con with se cierra el archivo automaticamente.

Con file.write escribiremos en el archivo las teclas presionadas con /n que es un salto de linea para que no se escriban todo junto y se pueda entender.

Con la siguiente linea lo imprimiremos las teclas pulsadas entre dos | |, esto lo hice para que se pudiera entender mejor al leerlo y quedara visualmente mejor.

Con keyboard.on_press ejecutamos la funcion que hemos creado antes con cada pulsacion del teclado y con keyboard.wait() se quedara ejecutando el programa sin fin hasta que el usuario cierre el script.

# 🖥️ - Áreas de mejora 
He pensado que podriamos con alguna tool o herramienta convertir el script de python a ejecutable (.exe) y añadirle algun icono para hacerlo pasar mas desapercibido. O incluso primero encriptar el codigo de python y luego pasarlo a exe y añadirle de alguna manera que se pudiera registrar los eventos desde una sesión remota. La tool que usariamos para pasarlo de python a ejecutable y añadirle un icono se llama "auto-py-to-exe" que podemos instalarla con "pip install auto-py-to-exe". 
