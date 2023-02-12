import tkinter as tk

import TTS

window_width = 500
window_height = 300
window_size = str(window_height)+"x"+str(window_width)
window_title = "Text to speech"
lang_list = TTS.lang_arr.values()

font_fam = "Arial"
font_size1 = 16
font_size2 = 12
font_size3 = 11

main_bg = '#4A4A4A'
enter_text_bg = '#878787'
font_color = '#FFFFFF'
onhold_bg = '#c3c3c3'

""" Send data to gTTS """
def ToTTS():
    TTS.TextToSpeech(enter_text.get(1.0, "end-1c"), lang_sele.get())
""" Send data to gTTS """

""" Start GUI """
window = tk.Tk()
window.title(window_title)
window.geometry(window_size)
""" Start GUI """

""" Variable for select language """
lang_sele = tk.StringVar()
lang_sele.set("English")
""" Variable for select language """

""" Edit data for GUI """
head_label = tk.Label(text="Enter text for text to speech", font=(font_fam, font_size1), bg=main_bg, fg=font_color)

enter_text = tk.Text(window, font=(font_fam, font_size3), height=7, width=40, padx=5, pady=5, bg=enter_text_bg, highlightthickness=0)

button_speech = tk.Button(text="Speech!", font=(font_fam, font_size2), width=10, height=2, command=ToTTS, bg=enter_text_bg, fg=font_color, activebackground=onhold_bg)

lang_label = tk.Label(text="Select language", font=(font_fam, font_size3), bg=main_bg, fg=font_color)

lang_drop = tk.OptionMenu( window , lang_sele , *lang_list)
lang_drop.config(bg=enter_text_bg)
lang_drop.config(fg=font_color)
lang_drop.config(highlightthickness=0)
lang_drop.config(activebackground=onhold_bg)
""" Edit data for GUI """

""" Place GUI """
lang_label.grid(column=0, row=0, sticky=tk.W, padx=20, pady=3)
lang_drop.grid(column=0, row=1, sticky=tk.W, padx=(20,10), pady=3)

head_label.grid(column=0, row=2, sticky=tk.W, padx=20, pady=(10,5))

enter_text.grid(column=0, row=3, sticky=tk.W, padx=(20,10), pady=0)
button_speech.grid(column=1, row=3, sticky=tk.W, padx=0, pady=0)
""" Place GUI """

window.configure(bg=main_bg)
window.minsize(window_width, window_height)
window.maxsize(window_width, window_height)
window.mainloop()