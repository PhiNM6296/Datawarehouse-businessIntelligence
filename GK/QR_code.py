

import qrcode

def generate_qr_code(link, filename='qrcode.png'):
    # Create an instance of the QRCode class
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to the QRCode instance
    qr.add_data(link)
    qr.make(fit=True)

    # Create an image from the QRCode instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(filename)

if __name__ == "__main__":
    # Replace 'https://example.com' with your desired link
    link_to_convert = 'https://forms.gle/JJYcd5tU3UbSmeBA9'
    
    # Replace 'qrcode.png' with your desired output filename
    output_filename = 'qrcode.png'

    # Generate the QR code
    generate_qr_code(link_to_convert, output_filename)
    print(f"QR code generated and saved as {output_filename}")
