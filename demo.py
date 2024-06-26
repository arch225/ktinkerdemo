from tkinter import *
import customtkinter
from openai import OpenAI
import os
import pickle

root=customtkinter.CTk()
root.title("ChatGpt Bot V1.0")
root.geometry("600x500")
root.iconbitmap("ai_lt.ico")

#Set Colour Scheme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

#Submit to ChatGPT
def speak():
    if chat_entry.get():
        filename="api_key"
        try:
            if os.path.isfile(filename):
                input_file=open(filename,"rb")
                stuff=pickle.load(input_file)
                #Query to ChatGPT
                client = OpenAI(
                # This is the default and can be omitted
                api_key=stuff,)

                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "user", "content": chat_entry.get()}
                    ],
                )
                my_text.insert(END, f"\n\n {response.choices[0].message.content}")
                
            else:
                input_file=open(filename, "wb")
                input_file.close()
                my_text.insert(END, "\n\n Please enter your API Key")

        except Exception as e:
            my_text.insert(END, f"Error: {e}")
    else:
        my_text.insert(END, "You forgot to write anything, Duh..")
#Clear the Screen
def clear():
    my_text.delete(1.0, END)
    chat_entry.delete(0, END)

#Do API Stuff
def key():
    #Resize App
    filename="api_key"
    try:
        if os.path.isfile(filename):
            input_file=open(filename,"rb")
            stuff=pickle.load(input_file)
            api_entry.insert(END, stuff)
        else:
            input_file=open(filename, "wb")
            input_file.close()
        root.geometry("600x650")
        api_frame.pack(pady=30)

    except Exception as e:
        my_text.insert(END, f"Error: {e}")

#Save API Key
def save_key():
    filename= "api_key"
    try:
        output_file=open(filename,'wb')
        pickle.dump(api_entry.get(), output_file)
        api_entry.delete(0, END)
        api_frame.pack_forget()
        root.geometry("600x500")
    except Exception as e:
        my_text.insert(END, f"Error: {e}")

#Create Text Frame
text_frame=customtkinter.CTkFrame(root)
text_frame.pack(pady=20)

#Add Text Widget to Get ChatGPT Responses
my_text=Text(text_frame,
             bg='#343638',
             width=65,
             bd=1,
             fg='#d6d6d6',
             relief="flat",
             wrap=WORD,
             selectbackground='#1f538d')
my_text.grid(row=0, column=0)

text_scroll=customtkinter.CTkScrollbar(text_frame,
                                       command=my_text.yview)
text_scroll.grid(row=0, column=1, sticky="ns")

#Add scrollbar to text widget
my_text.config(yscrollcommand=text_scroll.set)

#Adding text box for chat entry
chat_entry=customtkinter.CTkEntry(root,                
                                  placeholder_text="Ask something to ChatGPT...",
                                  width=500,
                                  height=40,
                                  border_width=1,
                                  corner_radius=10)
chat_entry.pack(pady=20)

#Create Button Frame
button_frame=customtkinter.CTkFrame(root,fg_color="#242424")
button_frame.pack(pady=10)

#Create buttons
submit_button=customtkinter.CTkButton(button_frame,
                                       text="Speak to ChatGPT",
                                       command=speak)
submit_button.grid(row=0, column=0, padx=25)

clear_button=customtkinter.CTkButton(button_frame,
                                       text="Clear Response",
                                       command=clear)
clear_button.grid(row=0, column=1, padx=35)

api_button=customtkinter.CTkButton(button_frame,
                                       text="Update API Key",
                                       command=key)
api_button.grid(row=0, column=2, padx=25)

#Add API Key Frame
api_frame=customtkinter.CTkFrame(root, border_width=1)
api_frame.pack(pady=10)

#Add API Entry widget
api_entry=customtkinter.CTkEntry(api_frame,
                                  placeholder_text="Enter API Key...",
                                  width=350,
                                  height=50,
                                  border_width=1,
                                  corner_radius=10)
api_entry.grid(row=0, column=0, padx=25,pady=20)

#Add API Button
api_save_button=customtkinter.CTkButton(api_frame,
                                         text="Save API Key",
                                         command=save_key)
api_save_button.grid(row=0, column=1, padx=10)


root.mainloop()








