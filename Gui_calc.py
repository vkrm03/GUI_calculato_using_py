import time
import tkinter as tk
import secret

window = tk.Tk()
window.title("Calculator")
window_width = 360
window_height = 550
window.geometry(f"{window_width}x{window_height}")

ans = []
def on_button_click(value):
    if ans_lable.cget("text") == "|":
        ans_lable.config(text="")
    current_text = ans_lable.cget("text")
    update_value = str(current_text) + str(value)
    ans_lable.config(text=update_value)
    if len(update_value) > max_characters:
        reduce_font_size()
def on_button_click_for_ans():
    operation = ans_lable.cget("text")
    if operation== "845726":
        window.withdraw()
        secret.secrets()
    try:
        answer = eval(operation)
        ans.append(answer)
        ans_lable.config(text=answer)
    except SyntaxError:
        ans_lable.config(text="Error")
def on_button_click_to_backspace():
    text = ans_lable.cget("text")
    ans_lable.config(text=text[0:len(text)-1])
def clear_button_click():
    ans_lable.config(text="|")

i = 1
def reduce_font_size():
    global i
    lable_y = 4
    current_font_size = ans_lable.cget("font")[10:12]
    new_font_size = max(int(current_font_size) - 2, min_font_size)
    ans_lable.config(font=("Helvetica", new_font_size), pady=lable_y)
    lable_y = lable_y - 1
    ans_lable.grid(row=0, column=0, columnspan=4, padx=5, pady=5+i)
    i = i + 1

def reset_font_size():
    ans_lable.config(font=("Helvetica", default_font_size))

def close():
    exit()
default_font_size = 35
min_font_size = 20
max_characters = 10

ans_lable = tk.Label(window, text="|", font=("Helvetica", 35), width=0, height=0)
ans_lable.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
clear_btn = tk.Button(window, text="C", width=10, height=5, command=clear_button_click)
clear_btn.grid(row=1, column=0, padx=5, pady=5)
seven_btn = tk.Button(window, text="7", width=10, height=5, command=lambda: on_button_click("7"))
seven_btn.grid(row=2, column=0, padx=5, pady=5)
four_btn = tk.Button(window, text="4", width=10, height=5, command=lambda: on_button_click("4"))
four_btn.grid(row=3, column=0, padx=5, pady=5)
one_btn = tk.Button(window, text="1", width=10, height=5, command=lambda: on_button_click("1"))
one_btn.grid(row=4, column=0, padx=5, pady=5)
exiting_btn = tk.Button(window, text="Exit", width=10, height=5, command=lambda : close())
exiting_btn.grid(row=5, column=0, padx=5, pady=5)
percent_btn = tk.Button(window, text="%", width=10, height=5, command=lambda: on_button_click("%"))
percent_btn.grid(row=1, column=1, padx=5, pady=5)
eight_btn = tk.Button(window, text="8", width=10, height=5, command=lambda: on_button_click("8"))
eight_btn.grid(row=2, column=1, padx=5, pady=5)
five_btn = tk.Button(window, text="5", width=10, height=5, command=lambda: on_button_click("5"))
five_btn.grid(row=3, column=1, padx=5, pady=5)
two_btn = tk.Button(window, text="2", width=10, height=5, command=lambda: on_button_click("2"))
two_btn.grid(row=4, column=1, padx=5, pady=5)
zero_btn = tk.Button(window, text="0", width=10, height=5, command=lambda: on_button_click("0"))
zero_btn.grid(row=5, column=1, padx=5, pady=5)
erase_btn = tk.Button(window, text="<-", width=10, height=5, command=lambda: on_button_click_to_backspace())
erase_btn.grid(row=1, column=2, padx=5, pady=5)
nine_btn = tk.Button(window, text="9", width=10, height=5, command=lambda: on_button_click("9"))
nine_btn.grid(row=2, column=2, padx=5, pady=5)
six_btn = tk.Button(window, text="6", width=10, height=5, command=lambda: on_button_click("6"))
six_btn.grid(row=3, column=2, padx=5, pady=5)
three_btn = tk.Button(window, text="3", width=10, height=5, command=lambda: on_button_click("3"))
three_btn.grid(row=4, column=2, padx=5, pady=5)
dot_btn = tk.Button(window, text=".", width=10, height=5, command=lambda: on_button_click("."))
dot_btn.grid(row=5, column=2, padx=5, pady=5)
divide_btn = tk.Button(window, text="/", width=10, height=5, command=lambda: on_button_click("/"))
divide_btn.grid(row=1, column=3, padx=5, pady=5)
multiplay_btn = tk.Button(window, text="x", width=10, height=5, command=lambda: on_button_click("*"))
multiplay_btn.grid(row=2, column=3, padx=5, pady=5)
subract_btn = tk.Button(window, text="-", width=10, height=5, command=lambda: on_button_click("-"))
subract_btn.grid(row=3, column=3, padx=5, pady=5)
add_btn = tk.Button(window, text="+", width=10, height=5, command=lambda: on_button_click("+"))
add_btn.grid(row=4, column=3, padx=5, pady=5)
result_btn = tk.Button(window, text="=", width=10, height=5, command=lambda: on_button_click_for_ans())
result_btn.grid(row=5, column=3, padx=5, pady=5)

window.mainloop()
