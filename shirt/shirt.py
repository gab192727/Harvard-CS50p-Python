from PIL import Image, ImageOps
import sys
import os

try:
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    input_image = sys.argv[1]
    output_image = sys.argv[2]
    valid_extensions = ['.jpg', '.jpeg', '.png']
    input_ext = os.path.splitext(input_image)[1].lower()
    output_ext = os.path.splitext(output_image)[1].lower()

    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        sys.exit("Invalid output")
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    input_img = Image.open(input_image)
    shirt_img = Image.open("shirt.png")
    resized_input_img = ImageOps.fit(input_img, shirt_img.size)
    resized_input_img.paste(shirt_img, (0, 0), shirt_img)
    resized_input_img.save(output_image)
except IndexError:
    sys.exit("Too few command-line arguments")
except FileNotFoundError:
    sys.exit("Input does not exist")
