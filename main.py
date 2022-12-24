from customtkinter import *
import subprocess as sp

def show_output(url, resultBox):
    result =  sp.run(['yt-dlp', '-F', url],capture_output=True).stdout.decode()
    resultBox.insert(END, result)
    
def download(id_string,url):
    # id as string id1,id2,id3 .....
    #replace , with + --> id1+id2+id3
    id_string.relace(',', '+')
    sp.Popen(['yt-dlp','-f',id_string,url]) 

set_default_color_theme("blue")
set_appearance_mode("dark")

mainWindow = CTk()
width = mainWindow.winfo_screenwidth()
height = mainWindow.winfo_screenheight()
dim = str(width) + "x" + str(height)
mainWindow.title("MainWindow")
mainWindow.geometry(dim)

textFont = CTkFont(family = "Times New Roman", size = 14)

urlDialog = CTkLabel(master = mainWindow, text = "Enter YouTube URL", corner_radius=10, font = textFont)
urlEntry = CTkEntry(master = mainWindow, placeholder_text = "Enter YouTube URL", width = 300, height = 30, border_width = 2, corner_radius = 10)

resultFrame = CTkFrame(master = mainWindow, width = width - 100, height = height - 400)
resultBox = CTkTextbox(master = resultFrame, corner_radius = 10, width = width - 110, height = height - 400)
scroll = CTkScrollbar(master = resultFrame, command=resultBox.yview)
scroll.pack(side=RIGHT, fill=Y)
resultBox.configure(yscrollcommand=scroll.set)
resultBox.pack(side=TOP, expand=TRUE, fill=BOTH)

getResults = CTkButton(master = mainWindow, text = "Get Results", corner_radius= 10, font = textFont, command = lambda : show_output(urlEntry.get(), resultBox =  resultBox))
resultsDialog = CTkLabel(master = mainWindow, text = "Results", corner_radius= 10, font = textFont)
idDialog = CTkLabel(master = mainWindow, text = "Enter ID", corner_radius=10, font = textFont)
idEntry = CTkEntry(master = mainWindow, placeholder_text = "Enter ID's (seperate different id's using ',')", width = 300, height = 30, border_width = 2, corner_radius = 10)
downloadButton = CTkButton(master = mainWindow, text = "Download", corner_radius= 10, font = textFont, command = lambda : download(id_string = idEntry.get(), url = urlEntry.get()))

urlDialog.pack(padx = 5, pady = 5)
urlEntry.pack(padx = 5, pady = 5)
getResults.pack(padx = 5, pady = 5)
resultsDialog.pack(padx = 5, pady = 5)
resultFrame.pack(padx = 5, pady = 5)
idDialog.pack(padx = 5, pady = 5)
idEntry.pack(padx = 5, pady = 5)
downloadButton.pack(padx = 5, pady = 5)



mainWindow.mainloop()