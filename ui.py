from tkinter import *
from tkinter import ttk 
from duration import calculate_total_video_length

def printDetails():
    folderPathVar =folderPath.get()
    calculate_total_video_length(folderPathVar,durationOutput)
    # outputString= "The total duration of videos in the folder is "+duration+"\n"
    # durationOutput.insert("1.0",outputString)
    

root = Tk()
root.geometry("410x400")
root.title("Duration Calculator")
content = ttk.Frame(root)

Path_label = ttk.Label(content,text="Enter Folder Path:")
folderPath = ttk.Entry(content,width=40)
submitButton =ttk.Button(content,text="Calculate",command=printDetails)
durationOutput = Text(content,width=43,height=18)
scrollbar = Scrollbar(content)
durationOutput.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=durationOutput.yview)

    


content.grid(column=0,row=0)
Path_label.grid(column=0,row=0,pady=20)
folderPath.grid(column=1,row=0,padx=0,pady=0)
submitButton.grid(column=1,row=1,pady=0)
durationOutput.grid(columnspan=2,column=0,row=2,padx=20,pady=10)
scrollbar.grid(row=2,column=2,sticky='ns')

root.mainloop()

