import os
import pyttsx3
import PyPDF2
import tkinter as tk
from tkinter import filedialog
import re
from pathlib import Path

downloads_path = str(Path.home() / "Downloads")

def select_pdf():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    return file_path

def pdf_to_audio(pdf_path):
    text = ""
    file_name_without_extension = os.path.splitext(pdf_path)[0].split("/")[-1]
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        for page_num in range(num_pages):
            # if page_num > 10:
            #     break
            try:
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
            except:
                print(f"Error en la página {page_num + 1}.")

    text = text.replace("\t", " ")
    text = _get_fixed_text(text)
    paragraphs = text.split("\n")
    # Set groups of 50 paragraphs
    paragraphs_groups = [paragraphs[i:i+50] for i in range(0, len(paragraphs), 50)]
    print(f"Se guardarán {len(paragraphs_groups)} archivos de audio.")
    for i, group in enumerate(paragraphs_groups):
        file_name = f"{file_name_without_extension}_{i+1}" 
        path_to_save = f"{downloads_path}/{file_name}.mp3"
        _save_audio("\n".join(group), path_to_save)


def _save_audio(text, path_to_save):
    engine = pyttsx3.init()
    voice_id = _get_spanish_voice()
    if not voice_id:
        raise Exception("No se ha encontrado una voz en español.")
    
    engine.setProperty("voice", voice_id)
    engine.setProperty("rate", 150)  # Ajusta la velocidad del habla
    engine.save_to_file(text, path_to_save)
    engine.runAndWait()
    print(f"El archivo {path_to_save} ha sido guardado.")

def _get_spanish_voice():
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    for voice in voices:
        if "spanish" in voice.name.lower():
            return voice.id
    return None

def _get_fixed_text(text):
    fixed_text = re.sub(r"\n(?=[a-zA-Z])", " ", text)
    return fixed_text


def main():
    pdf_path = select_pdf()
    if pdf_path:
        pdf_to_audio(pdf_path)
        print("La conversión ha sido completada.")
    else:
        print("No se ha seleccionado ningún archivo PDF.")





if __name__ == "__main__":
    main()


