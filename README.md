# Laboratorio 5
# Pablo Salas Gómez, C27061

# Diagrama UML


# Dependencias
argparse==1.4.0
Pillow==10.1.0
mathplotlib==3.8.0
opencv-python==4.8.0

# Uso del programa
Para ejecutar el programa es necesario hacerlo desde la terminal incluyendo los argumentos necesarios, los cuales son "--biblioteca" y "--imagen", tambien se puede usar "-h" para mostrar la documentación sobre como usar el programa.
El argumento "--biblioteca" acepta 3 opciones, las cuales son: "OpenCV", "PIL" y "Matplotlib", si se elige alguna de estas tres se usará la respectiva biblioteca para mostrar la imagen, si se escribe algo que no corresponde a alguna de las opciones el programa envia un mensaje de error pidiendo que se usen las opciones correctas.
El argumento "--imagen" recibe la dirección de la imagen que se desea mostrar, si se escribe una dirección corecta el programa se ejecutará de forma normal y mostrará la imagen, si se escribe una dirección que no existe el programa enviará un mensaje de error diciendo que la imagen no existe.
La forma de escribir en la terminal para ejecutar el programa correctamente es la siguiente:
proces_imagenes.py --biblioteca Biblioteca --imagen Path_imagen
