from gtts import gTTS
import PyPDF2
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
filelocation = askopenfilename()

with open(filelocation, "rb")as f:
    pdf = PyPDF2.PdfFileReader(f)
    myText = ""
    for pageNum in range(pdf.numPages):
        pageObj = pdf.getPage(pageNum)
        myText += pageObj.extractText()
print(myText)

final_output = gTTS(text=myText, lang='en')
print("generating speech...")
final_output.save("Generated_Speech.mp3")
os.system("start Generated_Speech.mp3")
print("successfully generated")
