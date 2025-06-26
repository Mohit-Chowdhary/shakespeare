import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import random
import colorsys
import math
import sys,os

a = ["artless", "bawdy", "beslubbering", "bootless", "churlish", "cockered",
"clouted", "craven", "currish", "dankish", "dissembling", "droning", 
"errant", "fawning", "fobbing", "froward", "frothy", "gleeking", 
"goatish", "gorbellied", "impertinent", "infectious", "jarring", 
"loggerheaded", "lumpish", "mammering", "mangled", "mewling", 
"paunchy", "pribbling", "puking", "puny", "qualling", "rank", 
"reeky", "roguish", "ruttish", "saucy", "spleeny", "spongy", 
"surly", "tottering", "unmuzzled", "vain", "venomed", "villainous", 
"warped", "wayward", "weedy", "yeasty"]

b = ["base-court", "bat-fowling", "beef-witted", "beetle-headed", 
"boil-brained", "clapper-clawed", "clay-brained", "common-kissing", 
"crook-pated", "dismal-dreaming", "dizzy-eyed", "doghearted", 
"dread-bolted", "earth-vexing", "elf-skinned", "fat-kidneyed", 
"fen-sucked", "flap-mouthed", "fly-bitten", "folly-fallen", 
"fool-born", "full-gorged", "guts-griping", "half-faced", 
"hasty-witted", "hedge-born", "hell-hated", "idle-headed", 
"ill-breeding", "ill-nurtured", "knotty-pated", "milk-livered", 
"motley-minded", "onion-eyed", "plume-plucked", "pottle-deep", 
"pox-marked", "reeling-ripe", "rough-hewn", "rude-growing", 
"rump-fed", "shard-borne", "sheep-biting", "spur-galled", 
"swag-bellied", "tardy-gaited", "tickle-brained", "toad-spotted", 
"unchin-snouted", "weather-bitten"]

c = ["apple-john", "baggage", "barnacle", "bladder", "boar-pig", 
"bugbear", "bum-bailey", "canker-blossom", "clack-dish", 
"clotpole", "coxcomb", "codpiece", "death-token", "dewberry", 
"flap-dragon", "flax-wench", "flirt-gill", "foot-licker", 
"fustilarian", "giglet", "gudgeon", "haggard", "harpy", 
"hedge-pig", "horn-beast", "hugger-mugger", "joithead", 
"lewdster", "lout", "maggot-pie", "malt-worm", "mammet", 
"measle", "minnow", "miscreant", "moldwarp", "mumble-news", 
"nut-hook", "pigeon-egg", "pignut", "puttock", "pumpion", 
"ratsbane", "scut", "skainsmate", "strumpet", "varlot", 
"vassal", "whey-face", "wagtail"]
# Generate insult
def generate_insult():
    insult = f"Thou {random.choice(a)} {random.choice(b)} {random.choice(c)}!"
    messagebox.showinfo("Thine Insult", insult)

# GUI setup
app = tk.Tk()
canvas = tk.Canvas(app, highlightthickness=0)
canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

app.title("Shakespearean Insult Generator")
app.geometry("500x400")
app.resizable(True, True)

# Load and prepare image
if hasattr(sys, "_MEIPASS"):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")

img_path = os.path.join(base_path, "shakespeare.jpg")
original_img = Image.open(img_path).convert("RGB")
sh_img = original_img.resize((120, 140), Image.Resampling.LANCZOS)
sh_photo = ImageTk.PhotoImage(sh_img)

# Initial floating state
sh_x, sh_y = 100, 100
sh_dx, sh_dy = 3, 2  # movement per frame

img_label = tk.Label(app, image=sh_photo)
img_label.image = sh_photo
img_label.place(x=100, y=100)
border = canvas.create_rectangle(
    sh_x, sh_y,
    sh_x + 120, sh_y + 140,
    outline="gold", width=30
)

# Insult button and label
label = tk.Label(app, text="Shakespearean Insult Thyself", font=("Georgia", 14))
label.pack(pady=15)

insult_btn = tk.Button(app, text="Roast Me, Bard!", command=generate_insult,
                       width=25, height=2, bg="ivory", fg="black", font=("Courier", 10, "bold"))
insult_btn.pack(pady=10)

def create_firework():
    w = app.winfo_width()
    h = app.winfo_height()
    if w < 100 or h < 100:
        return

    x = random.randint(100, w - 100)
    y = random.randint(100, h - 100)

    sparks = []
    num_sparks = 30
    base_hue = random.random()

    for i in range(num_sparks):
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 6)
        dx = speed * math.cos(angle)
        dy = speed * math.sin(angle)

        # Funky flickering rainbow
        hue = (base_hue + random.uniform(-0.1, 0.1)) % 1.0
        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
        color = f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"

        spark = canvas.create_oval(x, y, x+5, y+5, fill=color, outline="")
        sparks.append((spark, dx, dy, 0, random.uniform(0.5, 1.5)))  # last one is wobble strength

    animate_sparks_chaotic(sparks)




def animate_sparks_chaotic(sparks):
    new_sparks = []
    for spark_id, dx, dy, life, wiggle in sparks:
        # Add chaotic wobble
        offset_x = wiggle * math.sin(life * 0.3 + random.uniform(-0.5, 0.5))
        offset_y = wiggle * math.cos(life * 0.3 + random.uniform(-0.5, 0.5))
        canvas.move(spark_id, dx + offset_x, dy + offset_y)

        life += 1
        if life < 20:
            new_sparks.append((spark_id, dx, dy, life, wiggle))
        else:
            canvas.delete(spark_id)

    if new_sparks:
        app.after(40, lambda: animate_sparks_chaotic(new_sparks))


def firework_loop():
    create_firework()
    app.after(700, firework_loop)

firework_loop()



def float_shakespeare():
    global sh_x, sh_y, sh_dx, sh_dy

    window_width = app.winfo_width()
    window_height = app.winfo_height()
    img_w = 120
    img_h = 140

    # Bounce off walls
    if sh_x + sh_dx < 0 or sh_x + img_w + sh_dx > window_width:
        sh_dx *= -1
    if sh_y + sh_dy < 0 or sh_y + img_h + sh_dy > window_height:
        sh_dy *= -1

    sh_x += sh_dx
    sh_y += sh_dy

    img_label.place(x=sh_x, y=sh_y)
    canvas.coords(border, sh_x, sh_y, sh_x + img_w, sh_y + img_h)

    app.after(20, float_shakespeare)

float_shakespeare()  # Start animation

app.mainloop()