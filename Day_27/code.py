import tkinter as tk


def main():
    window= tk.Tk()
    window.title("Miles to Kilometers Converter")
    window.geometry("375x200")
    
    label1 = tk.Label(window, text="Enter Miles:")
    
    label2 = tk.Label(window, text="Kilometers:")

    label1.place(x=50,y=30)
    
    textbox1 = tk.Entry(window, width=12)

    textbox1.place(x=200,y=35)
    
    label2.place(x=50,y=100)
    
    label3 = tk.Label(window, text=" ")

    label3.place(x=180,y=100)

    def btn1_click():
        kilometers = round(float(textbox1.get()) * 1.60934,5)
        label3.configure(text = str(kilometers)+ '  Kilometers')
        
    btn1 = tk.Button(window, text="Convert", command=btn1_click)
    btn1.place(x=90,y=150)
    window.mainloop()
    

main()