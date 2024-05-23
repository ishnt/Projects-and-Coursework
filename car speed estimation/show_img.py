import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def display_image(image_path):
    # Read the image
    img = mpimg.imread(image_path)
    
    # Display the image
    plt.imshow(img)
    plt.axis('off')  # Turn off axis
    plt.show()

# Example usage
image_path = "E:\car speed estimation\919c5719579d855d1fa9e1c128a80d64.jpg"
display_image(image_path)
