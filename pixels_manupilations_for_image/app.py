from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path):
    img = Image.open(image_path)
    img = img.convert("RGB")  
    pixels = np.array(img)


    pixels[:, :, [0, 2]] = pixels[:, :, [2, 0]]

    key = 128
    encrypted_pixels = pixels ^ key

    encrypted_img = Image.fromarray(encrypted_pixels)
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, output_path):
    img = Image.open(image_path)
    img = img.convert("RGB")  
    pixels = np.array(img)


    key = 128
    decrypted_pixels = pixels ^ key

 
    decrypted_pixels[:, :, [0, 2]] = decrypted_pixels[:, :, [2, 0]]

    decrypted_img = Image.fromarray(decrypted_pixels)
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

def main():

    operation = input("Do you want to encrypt or decrypt an image? (e/d): ").strip().lower()
    if operation not in ["e", "d"]:
        print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
        return

  
    input_path = input("Enter the path to the image file: ").strip()
    output_path = input("Enter the path to save the output image: ").strip()

  
    if operation == "e":
        encrypt_image(input_path, output_path)
    else:
        decrypt_image(input_path, output_path)

if __name__ == "__main__":
    main()