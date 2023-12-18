import qrcode
from PIL import Image

# Your Google Maps link
google_maps_link = "https://maps.app.goo.gl/Mgn6UBmDPTxyHBrBA"

# Generate QR code with larger box size and higher error correction
qr = qrcode.QRCode(
    version=1,  # Automatically adjusted if necessary
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Higher error correction
    box_size=20,  # Larger box size
    border=4,  # Border size
)
qr.add_data(google_maps_link)
qr.make(fit=True)

# Set the fill color to red and background to black
img = qr.make_image(fill_color="red", back_color="black")

# Optional: Embed a logo or image in the bottom right corner
# Uncomment and adjust the following lines if you want to include a logo
#logo = Image.open("qr1.jpg")  # Replace with the path to your logo
#logo.thumbnail((510, 510))  # Resize logo. Adjust the size as needed

# Calculate logo position for bottom right corner
#logo_x_position = img.size[0] - logo.size[0] - 10  # 10 pixels from the right edge
#logo_y_position = img.size[1] - logo.size[1] - 10  # 10 pixels from the bottom edge
#logo_position = (logo_x_position, logo_y_position)

# Paste the logo onto the QR code
#img.paste(logo, logo_position)

# Save the QR code as an image file
img.save("enhanced_red_black_google_maps_qr_code.png")
