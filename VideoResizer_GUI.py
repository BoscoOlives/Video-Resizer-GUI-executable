# Joan Bosco Olives Florit
import os
import tkinter
from tkinter import *
from tkinter import filedialog
from moviepy.editor import VideoFileClip




def resize_video(path, resolution):

    if resolution == 1:
        height = 720
    else:
        height = 480
    # Obtiene el nombre del archivo sin la ruta
    file_name = os.path.basename(path.get())
    output_path = os.path.join(os.path.dirname(path.get()), file_name.replace('.mp4', '_'+str(height)+'p.mp4'))

    # Carga el video utilizando moviepy
    video = VideoFileClip(path.get())

    # Redimensiona el video a 720p si es necesario
    if video.size[1] < height:
        resized_video = video
    else:
        resized_video = video.resize(height=height)

    # Selecciona el códec adecuado para la salida
    codec = 'libx264'

    # Establece el número de hilos a utilizar para la codificación de video
    num_threads = os.cpu_count()
    print("Número threads totales del pc:", num_threads)
    threads = num_threads-1
    print("Número threads asignados al proceso:", threads)
    # Codifica el video redimensionado y lo guarda en un archivo MP4
    resized_video.write_videofile(output_path, codec=codec, threads=threads)

    # Libera los recursos utilizados por el video
    video.close()
    resized_video.close()

def open_file_dialog():
    # Abre un diálogo para seleccionar un archivo
    file_path = filedialog.askopenfilename()

    # Obtiene el nombre del archivo seleccionado
    if file_path:
        file_name = file_path
        print("Se ha seleccionado el archivo:", file_name)
        return file_name

def main():
    root = Tk()

    root.title("Resize Video - By Boscoolives")
    root.geometry("400x400")
    root['background'] = '#8e9daa'

    label = tkinter.Label(root,
                          text="First use 'Select File' to choose your local video",
                          bg="#8e9daa", font="Helvectica 12 bold italic")

    label.pack(fill=tkinter.BOTH) # se adapta a los margenes de la ventana

    file = StringVar()
    boton1 = tkinter.Button(root, text="Select file", command=lambda: file.set(open_file_dialog()))
    boton1.pack(fill='y', pady=20)

    file_label = Label(root, textvariable=file)
    file_label.pack(fill='y', pady=20)

    # resizes video
    boton2 = tkinter.Button(root, text="Resize Video to 1280x720", command=lambda: resize_video(file, 1))
    boton2.pack(fill='y', pady=20)

    boton3 = tkinter.Button(root, text="Resize Video to 640x480", command=lambda: resize_video(file, 2))
    boton3.pack(fill='y', pady=20)

    root.mainloop()



if __name__ == "__main__":
    main()

