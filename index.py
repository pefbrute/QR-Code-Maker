import qrcode
from PIL import Image

# Your link
link = "https://en.wikipedia.org/wiki/Cat"

FILL_COLOR = "brown"
BACK_COLOR = "white"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20,
    border=4,
)
qr.add_data(link)
qr.make(fit=True)

img = qr.make_image(fill_color=FILL_COLOR, back_color=BACK_COLOR)

# Optional if needed to add logo in right bottom corner
#LOGO_SIZE = 450  # Adjust the size of the logo

#logo = Image.open("qr3.jpg")  # Replace with the path to your logo
#logo.thumbnail((LOGO_SIZE, LOGO_SIZE))  # Resize logo

# Check if the logo has an alpha channel
#if logo.mode in ('RGBA', 'LA'):
#    logo_mask = logo.split()[-1]
#else:
#    logo_mask = None

# Calculate logo position for the bottom right corner
#logo_position = (img.size[0] - logo.size[0], img.size[1] - logo.size[1])

# Paste the logo onto the QR code using the correct mask
#img.paste(logo, logo_position, logo_mask)

# Save the QR code as an image file
img.save("QR in right bottom corner.png")
