import imageio.v3 as imageio
import numpy as np
import matplotlib.pyplot as plt

# Membaca gambar RGB
gambar_rgb = imageio.imread('daunsingkong.jpg')

# Mengonversi gambar RGB ke Grayscale menggunakan metode luminositas
gambar_gray = np.dot(gambar_rgb[..., :3], [0.2989, 0.587, 0.114]).astype(np.uint8)

# Menghitung histogram intensitas piksel (0-255)
histogram, bins = np.histogram(gambar_gray.flatten(), bins=256, range=(0, 255))

# Plot histogram
plt.figure(figsize=(10, 6))
plt.plot(histogram, color='black')
plt.title('Histogram Intensitas Gambar Grayscale')
plt.xlabel('Intensitas (0-255)')
plt.ylabel('Jumlah Piksel')
plt.show()

# Menghitung jumlah total piksel untuk setiap intensitas
total_piksel_per_intensitas = dict(enumerate(histogram))

# Menentukan intensitas dominan
intensitas_dominan = np.argmax(histogram)
jumlah_piksel_dominan = histogram[intensitas_dominan]

print("a. Jumlah total piksel untuk setiap intensitas:", total_piksel_per_intensitas)
print(f"b. Intensitas yang dominan adalah {intensitas_dominan} dengan jumlah piksel sebanyak {jumlah_piksel_dominan}.")
