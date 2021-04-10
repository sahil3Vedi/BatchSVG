import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

input_files = os.listdir("./input")

for input_file in input_files:
    input_loc = os.path.join("./input",input_file)
    img = mpimg.imread(input_loc)
    imgplot = plt.imshow(img)
    plt.axis('off')
    output_loc = os.path.join("./output",input_file.split('.')[0]+".svg")
    plt.savefig(output_loc, format="svg")
    plt.clf()
