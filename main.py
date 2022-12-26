from customtkinter import *
import subprocess as sp
from parse_output import *
import threading

def show_output(url, resultBox):
    Headers = ["ID", "EXT", "RESOLUTION", "FILESIZE", "FORMAT"]
    result =  sp.run(['yt-dlp','-q','-F', url],capture_output=True).stdout.decode()
    ids,ext,res,size,formats = parse(result)
    out = [list(a) for a in zip(ids, ext, res, size, formats)]
    for item in Headers:
        resultBox.insert(END, item.ljust(30 - len(item)))
    resultBox.insert(END, "\n"+"_"*80 + "\n")
    for row in out:
        for item in row:
            resultBox.insert(END, item.ljust(30 - len(item)))
        resultBox.insert(END, "\n")
        
    resultBox.insert(END, "\n")
    resultBox.see(END)
    """ resultBox.insert(END, result)"""


def write_output(P,resultBox):
    while True:
        nextline = P.stdout.readline()
        if nextline == b"":
            break
        resultBox.insert(END,nextline)
        resultBox.see(END)
    
        
def download(id_string,url, resultBox):
    # id as string id1,id2,id3 .....
    #replace , with + --> id1+id2+id3
    id_string = id_string.replace(" ","").replace(",","+")
    P = sp.Popen(["yt-dlp","--newline", "-f",id_string,url], shell=True, stdout=sp.PIPE)
    # P = P.split("[download]")
    # for row in P:
    #     resultBox.insert(END, "\n[download]" + row)
    # resultBox.see(END)
    # while True:
    #     nextline = P.stdout.readline()
    #     if nextline == b"":
    #         break
    #     resultBox.insert(END,nextline)
    #     resultBox.see(END)
    thread = threading.Thread(target=write_output, args=(P,resultBox))
    thread.start()
    resultBox.insert(END,"[*]Process completed")
    resultBox.see(END)




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
resultBox = CTkTextbox(master = mainWindow, corner_radius = 10, width = width - 110, height = height - 400)
getResults = CTkButton(master = mainWindow, text = "Get Results", corner_radius= 10, font = textFont, command = lambda : show_output(urlEntry.get(), resultBox =  resultBox))
resultsDialog = CTkLabel(master = mainWindow, text = "Results", corner_radius= 10, font = textFont)
idDialog = CTkLabel(master = mainWindow, text = "Enter ID", corner_radius=10, font = textFont)
idEntry = CTkEntry(master = mainWindow, placeholder_text = "Enter ID's (seperate different id's using ',')", width = 300, height = 30, border_width = 2, corner_radius = 10)
downloadButton = CTkButton(master = mainWindow, text = "Download", corner_radius= 10, font = textFont, command = lambda : download(id_string = idEntry.get(), url = urlEntry.get(), resultBox = resultBox))

urlDialog.pack(padx = 5, pady = 5)
urlEntry.pack(padx = 5, pady = 5)
getResults.pack(padx = 5, pady = 5)
resultsDialog.pack(padx = 5, pady = 5)
resultBox.pack(padx = 5, pady = 5)
idDialog.pack(padx = 5, pady = 5)
idEntry.pack(padx = 5, pady = 5)
downloadButton.pack(padx = 5, pady = 5)


mainWindow.mainloop()