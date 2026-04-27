import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# --------- TRAIN MODEL ---------
data = {
    "Math": [8, 2, 7, 3, 9, 1],
    "Science": [9, 3, 8, 2, 9, 2],
    "Arts": [2, 8, 3, 9, 1, 9],
    "Sports": [6, 5, 7, 4, 8, 3],
    "Interest": ["Tech", "Arts", "Tech", "Arts", "Tech", "Arts"]
}

df = pd.DataFrame(data)
X = df[["Math", "Science", "Arts", "Sports"]]
y = df["Interest"]

model = DecisionTreeClassifier()
model.fit(X, y)

# --------- GUI FUNCTION ---------
def predict_interest():
    try:
        math = int(entry_math.get())
        science = int(entry_science.get())
        arts = int(entry_arts.get())
        sports = int(entry_sports.get())

        # Validate range
        for val in [math, science, arts, sports]:
            if val < 1 or val > 10:
                raise ValueError

        prediction = model.predict([[math, science, arts, sports]])

        result_label.config(
            text=f"Suggested Interest Area: {prediction[0]}",
            fg="green"
        )

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter numbers between 1 and 10.")

# --------- CREATE WINDOW ---------
root = tk.Tk()
root.title("AI Student Interest Analyzer")
root.geometry("400x350")
root.configure(bg="#f0f0f0")

# --------- TITLE ---------
title = tk.Label(root, text="Student Interest Analyzer", font=("Arial", 16, "bold"), bg="#f0f0f0")
title.pack(pady=10)

# --------- INPUT FIELDS ---------
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=10)

tk.Label(frame, text="Math (1-10):", bg="#f0f0f0").grid(row=0, column=0, pady=5)
entry_math = tk.Entry(frame)
entry_math.grid(row=0, column=1)

tk.Label(frame, text="Science (1-10):", bg="#f0f0f0").grid(row=1, column=0, pady=5)
entry_science = tk.Entry(frame)
entry_science.grid(row=1, column=1)

tk.Label(frame, text="Arts (1-10):", bg="#f0f0f0").grid(row=2, column=0, pady=5)
entry_arts = tk.Entry(frame)
entry_arts.grid(row=2, column=1)

tk.Label(frame, text="Sports (1-10):", bg="#f0f0f0").grid(row=3, column=0, pady=5)
entry_sports = tk.Entry(frame)
entry_sports.grid(row=3, column=1)

# --------- BUTTON ---------
predict_btn = tk.Button(root, text="Analyze Interest", command=predict_interest, bg="#4CAF50", fg="white")
predict_btn.pack(pady=15)

# --------- RESULT ---------
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0")
result_label.pack(pady=10)

# --------- RUN ---------
root.mainloop()