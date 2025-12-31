import tkinter as tk
import random

choices = ["سنگ", "کاغذ", "قیچی"]

def play(user_choice):
    computer_choice = random.choice(choices)

    user_label.config(text=f"انتخاب تو: {user_choice}")
    comp_label.config(text=f"انتخاب کامپیوتر: {computer_choice}")

    if user_choice == computer_choice:
        result = "مساوی شد 😄"
    elif (user_choice == "سنگ" and computer_choice == "قیچی") or \
         (user_choice == "کاغذ" and computer_choice == "سنگ") or \
         (user_choice == "قیچی" and computer_choice == "کاغذ"):
        result = "تو بردی ✅"
        update_score(user_win=True)
    else:
        result = "کامپیوتر برد ❌"
        update_score(user_win=False)

    result_label.config(text=result)

def update_score(user_win):
    global user_score, comp_score
    if user_win:
        user_score += 1
    else:
        comp_score += 1
    score_label.config(text=f"امتیاز تو {user_score}  -  {comp_score} امتیاز کامپیوتر")

def reset_game():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    user_label.config(text="انتخاب تو: —")
    comp_label.config(text="انتخاب کامپیوتر: —")
    result_label.config(text="شروع کن!")
    score_label.config(text="امتیاز تو 0  -  0 امتیاز کامپیوتر")

# ---------- UI ----------
root = tk.Tk()
root.title("بازی سنگ، کاغذ، قیچی")
root.geometry("420x420")
root.resizable(False, False)

title = tk.Label(root, text="🎮 سنگ، کاغذ، قیچی", font=("Tahoma", 18, "bold"))
title.pack(pady=15)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

rock_btn = tk.Button(btn_frame, text="سنگ 🪨", font=("Tahoma", 14),
                     width=10, command=lambda: play("سنگ"))
rock_btn.grid(row=0, column=0, padx=8, pady=5)

paper_btn = tk.Button(btn_frame, text="کاغذ 📄", font=("Tahoma", 14),
                      width=10, command=lambda: play("کاغذ"))
paper_btn.grid(row=0, column=1, padx=8, pady=5)

scissors_btn = tk.Button(btn_frame, text="قیچی ✂️", font=("Tahoma", 14),
                         width=10, command=lambda: play("قیچی"))
scissors_btn.grid(row=0, column=2, padx=8, pady=5)

user_label = tk.Label(root, text="انتخاب تو: —", font=("Tahoma", 13))
user_label.pack(pady=8)

comp_label = tk.Label(root, text="انتخاب کامپیوتر: —", font=("Tahoma", 13))
comp_label.pack(pady=8)

result_label = tk.Label(root, text="شروع کن!", font=("Tahoma", 16, "bold"))
result_label.pack(pady=15)

user_score = 0
comp_score = 0
score_label = tk.Label(root, text="امتیاز تو 0  -  0 امتیاز کامپیوتر", font=("Tahoma", 12))
score_label.pack(pady=10)

reset_btn = tk.Button(root, text="ریست بازی 🔄", font=("Tahoma", 12),
                      command=reset_game)
reset_btn.pack(pady=10)

exit_btn = tk.Button(root, text="خروج 👋", font=("Tahoma", 12),
                     command=root.destroy)
exit_btn.pack()

root.mainloop()