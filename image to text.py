# #working
#image to text


# from PIL import Image
# import pytesseract

# # Specify the correct path to tesseract.exe
# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Viswajith\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# def image_to_text(image_path):
#     """
#     Converts an image to text using pytesseract OCR.
    
#     :param image_path: Path to the image file
#     :return: Extracted text from the image
#     """
#     # Open the image using PIL
#     img = Image.open(image_path)
    
#     # Use pytesseract to do OCR on the image
#     text = pytesseract.image_to_string(img)
    
#     return text

# # Example usage
# image_path = r'C:\Users\Viswajith\Pictures\Screenshots\Screenshot 2024-10-21 114041.png'
# extracted_text = image_to_text(image_path)

# print("Extracted Text:\n", extracted_text)








##image to text using tkinter

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract

# Specify the correct path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Viswajith\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def image_to_text(image_path):
    """
    Converts an image to text using pytesseract OCR.
    
    :param image_path: Path to the image file
    :return: Extracted text from the image
    """
    # Open the image using PIL
    img = Image.open(image_path)
    
    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(img)
    
    return text

def open_image():
    # Open file dialog to select an image
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")])
    
    if file_path:
        # Extract text from the image
        extracted_text = image_to_text(file_path)
        
        # Display the extracted text in the text box
        text_box.delete(1.0, tk.END)  # Clear previous content
        text_box.insert(tk.END, extracted_text)
        
        # Display the image in the GUI
        img = Image.open(file_path)
        img.thumbnail((300, 300))
        img = ImageTk.PhotoImage(img)
        image_label.config(image=img)
        image_label.image = img  # Keep a reference to avoid garbage collection

# Set up the Tkinter window
root = tk.Tk()
root.title("Image to Text OCR")
root.geometry("800x600")

# Create a button to open the file dialog
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack(pady=20)

# Create a label to display the image
image_label = tk.Label(root)
image_label.pack(pady=10)

# Create a text box to display the extracted text
text_box = tk.Text(root, height=20, width=80)
text_box.pack(pady=20)

# Run the Tkinter main loop
root.mainloop()






