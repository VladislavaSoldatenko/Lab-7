from PIL import Image, ImageTk
import requests
from io import BytesIO
import tkinter as tk
import random 


def load_image():
    response = requests.get(f"https://randomfox.ca/images/{random.randint(1,124)}.jpg")
    data_image = Image.open(BytesIO(response.content)) 
    image = ImageTk.PhotoImage(data_image)
    label.config(image=image)
    label.image = image


root = tk.Tk()
root.geometry('1000x800')
root.resizable(0, 0)


tk.Button(root, text='Сменить картинку', command=load_image).pack()
label=tk.Label(root)
label.pack()

root.mainloop()
