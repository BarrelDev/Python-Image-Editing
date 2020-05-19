from PIL import Image, ImageFilter, ImageEnhance

contrastDelta = input("Please enter a value for contrast -> ")
widthMultiplier = input("Please enter a width multiplier -> ")
lengthMultiplier = input("Please enter a length multiplier -> ")
imagePath = input("Please enter an image path -> ")
imageQuality = input("Please enter an image save quality -> ")

image = Image.open(imagePath)  
print("Image loaded !!")

image.show()
print(image.size)

enh=ImageEnhance.Contrast(image)
enh.enhance(int(contrastDelta)).show()
enh.enhance(int(contrastDelta)).save('contrast.png', quality = int(imageQuality))

#Create and Save enlarged image
size_tuple=image.size
print(size_tuple)
sizelist=list(size_tuple)
newwidth=sizelist[0]*int(widthMultiplier)
newheight=sizelist[1]*int(lengthMultiplier)
newsize=(newwidth,newheight)
img_resized=image.resize(newsize)
img_resized.show()
img_resized.save('enlarge.png', quality = int(imageQuality))