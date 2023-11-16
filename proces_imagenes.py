# Se importan todas las librerias utilizadas.
import argparse
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Clase padre que almacena el nombre de la imagen y crea el método para mostarla
class Procesamiento:
    def __init__(self, archivo):
        self.archivo = archivo

    def mostrar_imagen(self):
        pass

# Las clases hijas cambian el método de mostrar la imagen en cada una, según la biblioteca a la que corresponde.
class PIL(Procesamiento):
    def mostrar_imagen(self):
        img = Image.open(self.archivo)
        img.show()

class OpenCV(Procesamiento):
    def mostrar_imagen(self):
        img = cv2.imread(self.archivo)
        cv2.imshow(self.archivo, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

class Matplotlib(Procesamiento):
    def mostrar_imagen(self):
        img = mpimg.imread(self.archivo)
        plt.imshow(img)
        plt.show()

# Se crean los argumentos esperados, y su respectiva documentación.
def parse_args():
    parser = argparse.ArgumentParser(description="Procesamiento de Imagenes")
    parser.add_argument("--biblioteca", choices=["PIL", "Matplotlib", "OpenCV"], required=True, help="Biblioteca para procesamiento de imagenes")
    parser.add_argument("--imagen", required=True, help="Ruta de la imagen a procesar")
    return parser.parse_args()

def main():
    args = parse_args()

    # Se comprueban los argumentos pasados, para ver si son validos o no.
    if args.biblioteca == 'PIL':
        imagen = PIL(args.imagen)

    elif args.biblioteca == 'Matplotlib':
        imagen = Matplotlib(args.imagen)
        
    elif args.biblioteca == 'OpenCV':
        imagen = OpenCV(args.imagen)
        
    else:
        print("Biblioteca no valida. Selecciona PIL, Matplotlib o OpenCV.")
        return

    # Se comprueba que no ocurran errores al usar el archivo de la imagen.
    try:
        imagen.mostrar_imagen()
    except Exception as e:
        print(f"Error al procesar la imagen: {e}")

if __name__ == "__main__":
    main()