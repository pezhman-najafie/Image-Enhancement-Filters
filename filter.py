import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = 'C:\\Users\\pezhm\\Desktop\\pro\\1.jpeg'
original_image = cv2.imread(image_path)


fig = plt.figure()
plt.title("High Boost",fontsize = 8)
plt.axis('off')
ax = fig.add_subplot(3, 4, 1)
ax.set_title('original',fontsize = 8)
ax.axis('off')
ax.imshow(original_image)

i=1
# 1. High Boost Filter
def apply_high_boost_filter(image, a):
    # Define the kernel for high boost filter
    kernel = np.array([[-1, -1, -1],
                       [-1, 9*a-1, -1],
                       [-1, -1, -1]])

    # Apply the filter using convolution
    high_boost_result = cv2.filter2D(image, -1, kernel)

    return high_boost_result

# Iterate over different values of parameter A for High Boost Filter
for a_value in np.arange(1, 3.2, 0.2):
    result_image = apply_high_boost_filter(original_image, a_value)

    # Display and analyze the obtained image
    i=i+1
    ax = fig.add_subplot(3, 4, i )
    ax.set_title(f'A = {a_value:.2f}', fontsize=8)
    ax.axis('off')
    ax.imshow(result_image, cmap='gray')
plt.show()

# 2. Median Filter

def apply_median_filter(image, size):
    # Apply the median filter
    median_result = cv2.medianBlur(image, size)

    return median_result

fig = plt.figure()
plt.title("median filter", fontsize=8)
plt.axis('off')

ax = fig.add_subplot(2, 3, 1)
ax.set_title('orginal', fontsize=8)
ax.axis('off')
ax.imshow(original_image)

i=1
# Iterate over different sizes for Median Filter
filter_sizes = [3, 5, 7, 9, 11]
for size in filter_sizes:
    result_image = apply_median_filter(original_image, size)

    i=i+1
    # Display and analyze the obtained image
    ax = fig.add_subplot(2, 3, i)
    ax.set_title(f"Median Filter (Size={size}x{size})", fontsize=8)
    ax.axis('off')
    ax.imshow(result_image)

plt.show()



