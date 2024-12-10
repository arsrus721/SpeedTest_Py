import time
from tkinter import Tk, Label, Button
from tkinter import ttk
import speedtest
import threading

st = speedtest.Speedtest()

def run_speedtest():
    progress_bar.start(10) 
    
    download_speed = st.download() / 1_000_000
    upload_speed = st.upload() / 1_000_000
    ping = st.results.ping

    progress_bar.stop()
    
    dwnlbl.configure(text=f"Download: {download_speed:.2f} Mbps")
    upllbl.configure(text=f"Upload: {upload_speed:.2f} Mbps")
    pinglbl.configure(text=f"Ping: {ping:.2f} ms")
    wind.geometry('320x300')

def clicked():
    thread = threading.Thread(target=run_speedtest)
    thread.start()

wind = Tk()
wind.title("SpeedTest")
wind.geometry('220x300')

dwnlbl = Label(wind, text="Download", font=("Italic Bold", 20))  
dwnlbl.grid(column=0, row=0)

pinglbl = Label(wind, text="Ping", font=("Italic Bold", 20))  
pinglbl.grid(column=0, row=1)

upllbl = Label(wind, text="Upload", font=("Italic Bold", 20))  
upllbl.grid(column=0, row=2)

button = Button(wind, text="Start Speed Test", command=clicked)
button.grid(column=0, row=4)

progress_bar = ttk.Progressbar(wind, orient="horizontal", length=200, mode="indeterminate")
progress_bar.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

wind.mainloop()
