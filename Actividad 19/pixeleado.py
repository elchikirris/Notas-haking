from PIL import Image
import numpy as np 
image1 = Image.open('scrambled1.png')
image2 = Image.open('scrambled2.png')

array = np.asarray(image1)
array2 = np.asarray(image2)

result_array = np.add(array ,array2)

im = Image.fromarray(result_array, mode= "RGB")

im.show()