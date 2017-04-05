from wand.image import Image

img1 = Image(filename='images/filename.jpg')
img2 = Image(filename='images/filename1.jpg')

# Normalize the two images in order to avoid exposition-related issues
img1.normalize()
img2.normalize()

# Create a 64 x 64 thumbnail for every image
img1.resize(64, 64)
img2.resize(64, 64)

# Compare the two images using root mean square metric
comparison = img1.compare(img1, metric='root_mean_square')[1]