from remgb import remove
from PIL import Image
input_path = 'image.jgp'
output_path = 'image.png'
rla = Image.open(input_path)
output = remove(rla)
output.save(output_path)

#Ronan Luiz Alles
