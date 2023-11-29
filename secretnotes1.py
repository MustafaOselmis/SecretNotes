import tkinter
from PIL import Image,ImageTk
from cryptography.fernet import Fernet
from tkinter import messagebox

key = Fernet.generate_key()
cipher_suite = Fernet(key)

def cryptandsavefile():
    text_content = textbox1.get("1.0","end-1c") #1.satırın 0.sütunundan sonuna kadar alır
    text_content2 = entry1.get()

    #with open("Txt1","w",encoding="utf-8") as file: # bu fonksiyonun yazılanı dosyaya aktarır
        #file.write(text_content)
    space = b'\n '    

    text_content2 = bytes(text_content2,"utf-8")
    text_content = bytes(text_content,"utf-8")
    sifreli_mesaj = cipher_suite.encrypt(text_content)
    with open("Txt1","ab") as file:
        file.write(text_content2 + space)
        file.write(sifreli_mesaj + space)    

def decrypt():
    master_key = entry2.get()

    if not master_key:
        messagebox.showerror("Error", "Enter Your Master Key")
        return

    # Master key doğru mu kontrol et
    correct_master_key = master_key  # "your_master_key" yerine kendi belirlediğiniz master key'i kullanın
    if master_key != correct_master_key:
        messagebox.showerror("Error", "Incorrect Master Key")
        return

    encrypted_text = textbox1.get("1.0", "end-1c")
    encrypted_data = bytes(encrypted_text, "utf-8")

    decrypted_data = cipher_suite.decrypt(encrypted_data)
    decoded_text = decrypted_data.decode("utf-8")

    # Çözülen veriyi textbox1'a ekle
    textbox1.delete("1.0", "end")
    textbox1.insert("1.0", decoded_text)
    




fontX= ("Arial","18")
#screen
window = tkinter.Tk()
window.title("Secret Notes")
window.config(padx=20,pady=20,bg="grey")
window.minsize(width=400,height=800)

# Upload the image
img = Image.open(r"C:\Users\must\Desktop\python_temelleri\SecretNotes\kilit.png")
img = img.resize((200, 200))
photo = ImageTk.PhotoImage(img)

# Show the image
label1 = tkinter.Label(window, image=photo,bg="grey")
label1.pack()

# Title label

label2 = tkinter.Label(text="Enter Your Title",bg="grey", fg="black",padx=20,pady=10,font=fontX)
label2.pack()

#entry 1

entry1 = tkinter.Entry(width=20)
entry1.pack()

# Enter your secret label

label3= tkinter.Label(text="Enter Your Secret",bg="grey", fg="black",padx=20,pady=20,font=fontX)
label3.pack()

# textbox

textbox1 = tkinter.Text(window,height=10,width=20)
textbox1.pack()

# master key label
label4 = tkinter.Label(text="Enter Your Master Key",bg="grey", fg="black",padx=20,pady=10,font=fontX)
label4.pack()

# entry 2

entry2 = tkinter.Entry(width=20)
entry2.pack(ipady=5)

# button 1 = Save / Encrpyt

button1 = tkinter.Button()
button1.config(text="Save & Encrpyt",command=cryptandsavefile)
button1.pack(pady=5)

# button 2 = Decrpyt

button2 = tkinter.Button()
button2.config(text="Decrypt",command=decrypt)
button2.pack(pady=1)

window.mainloop()