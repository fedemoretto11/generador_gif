import imageio

archivos = ["uno.jpg", "dos.jpg", "tres.jpg"]
imagenes = []

for file in archivos:
    imagenes.append(imageio.imread(file))
    
imageio.mimsave("fede.gif", imagenes, duration = 0.4)

