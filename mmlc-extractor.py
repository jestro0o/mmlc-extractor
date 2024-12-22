#Requisites: installed tkinter, Steam and MMLC1 (Mega Man Legacy Collection 1)

import tkinter as tk

#All HEADERS, OFFSETS and JAPANOFFSETS i took from here: https://gist.github.com/VideogameScrapbook/e1dc851234b0bdba97b0c73cf9f52aed

HEADERS = [b'\x4E\x45\x53\x1A\x08\x00\x21\x00\x00\x00\x00\x00\x00\x00\x00\x00',
           b'\x4E\x45\x53\x1A\x10\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00',
           b'\x4E\x45\x53\x1A\x10\x10\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00',
           b'\x4E\x45\x53\x1A\x20\x00\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00',
           b'\x4E\x45\x53\x1A\x10\x20\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00',
           b'\x4E\x45\x53\x1A\x20\x00\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00']

OFFSETS = [{'PRG': [0x2AEEB0, 0x20000], 'CHA': None},
           {'PRG': [0x8ED70, 0x40000], 'CHA': None},
           {'PRG': [0xCEDB0, 0x40000], 'CHA': [0x10EDB0, 0x20000]},
           {'PRG': [0x12EDF0, 0x80000], 'CHA': None},
           {'PRG': [0x1AEE30, 0x40000], 'CHA': [0x1EEE30, 0x40000]},
           {'PRG': [0x22EE70, 0x80000], 'CHA': None}]

JAPANOFFSETS = [{'PRG': [0x512230, 0x20000], 'CHA': None},
           {'PRG': [0x2F20F0, 0x40000], 'CHA': None},
           {'PRG': [0x332130, 0x40000], 'CHA': [0x372130, 0x20000]},
           {'PRG': [0x392170, 0x80000], 'CHA': None},
           {'PRG': [0x4121B0, 0x40000], 'CHA': [0x4521B0, 0x40000]},
           {'PRG': [0x4921F0, 0x80000], 'CHA': None}]

def getpath():
    path = entry.get()

    if path == "":
        label['text'] = "Error! You haven't written anything."
    else:
        gamepath = path + "\\steamapps\\common\\Suzy\\Proteus.exe"
        try:
            f = open(gamepath, "rb")
            try:
                exe = f.read()
            finally:
                f.close()
        except FileNotFoundError:
            label['text'] = "Error! File not found, try again."
        for i, game in enumerate(HEADERS):
            for section in ['PRG', 'CHA']:
                if OFFSETS[i][section]:
                    start = OFFSETS[i][section][0]
                    size = OFFSETS[i][section][1]
                    end = start + size
                    game += exe[start:end]
            out = open("Mega Man " + str(i+1) + " (U) (Legacy Collection).nes", "wb")
            try:
                out.write(game)
            finally:
                out.close()
    
        for i, game in enumerate(HEADERS):
            for section in ['PRG', 'CHA']:
                if JAPANOFFSETS[i][section]:
                    start = JAPANOFFSETS[i][section][0]
                    size = JAPANOFFSETS[i][section][1]
                    end = start + size
                    game += exe[start:end]
            out = open("Rockman " + str(i+1) + " (J).nes", "wb")
            try:
                out.write(game)
            finally:
                label['text'] = "Done!"
                root.geometry("300x100")
                out.close()


root = tk.Tk()
root.title("MMLC RPC v0.1")
root.geometry("500x100")

label = tk.Label(root, text="Hello! Please, type here your Steam directory (remember to use backslash instead of slash):")
label.pack(pady = 10)

entry = tk.Entry(root)
entry.pack(padx = 20, side = tk.RIGHT)

btn = tk.Button(root, width=5, height=1, text="Submit", command=getpath)
btn.pack(side = tk.RIGHT)

root.mainloop()