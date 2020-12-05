import tkinter as tk
from tkinter import ttk


class WilkesWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("perkinsBryant_Homework4")
        self.score = "Your Wilkes Score is "
        self.weight_entry = tk.StringVar()
        self.bench_entry = tk.StringVar()
        self.squat_entry = tk.StringVar()
        self.deadlift_entry = tk.StringVar()
        self.main_frame = ttk.LabelFrame(self.window, text="Wilkes Coefficient Calculator", relief=tk.RIDGE, padding=6)
        self.weight_final = ttk.Label(self.window, text="Your Wilks Score:")
        self.weight_final.grid(row=2, column=1, sticky=tk.W + tk.N)
        self.radio_val = tk.IntVar()
        self.create_widgets()
        self.m_a, self.m_b, self.m_c, self.m_d, self.m_e, self.m_f = -216.047514, 16.260634, -0.002388645, -0.0011373, 7.0186E-06, -1.29E-08
        self.f_a, self.f_b, self.f_c, self.f_d, self.f_e, self.f_f = 594.3175, -27.238, 0.8212, -0.00931, 4.732E-05, -9.054E-08

    def create_widgets(self):
        # Create some room around all the internal frames
        self.window['padx'], self.window['pady'] = 4, 4

        self.main_frame = ttk.LabelFrame(self.window, text="Wilkes Calculator", relief=tk.RIDGE, padding=6)
        self.main_frame.grid(row=1, column=1, padx=6, sticky=tk.E + tk.W + tk.N + tk.S)

        # The Choices
        self.radio_val.set(0)

        sex_label = ttk.Label(self.main_frame, width=17, text="Choose your sex")
        sex_label.grid(row=1, column=1, sticky=tk.W + tk.N)

        male_button = ttk.Radiobutton(self.main_frame, text="Male", variable=self.radio_val, value=0)
        female_button = ttk.Radiobutton(self.main_frame, text="Female", variable=self.radio_val, value=1)

        male_button.grid(row=1, column=2, sticky=tk.W)
        female_button.grid(row=1, column=2, sticky=tk.E)

        # The Data entries
        weight_label = ttk.Label(self.main_frame, text="Weight (lbs)")
        weight_label.grid(row=2, column=1, sticky=tk.W + tk.N)

        bench_label = ttk.Label(self.main_frame, text="Bench Press (lbs)")
        bench_label.grid(row=3, column=1, sticky=tk.W + tk.N)

        squat_label = ttk.Label(self.main_frame, text="Squat (lbs)")
        squat_label.grid(row=4, column=1, sticky=tk.W + tk.N)

        deadlift_label = ttk.Label(self.main_frame, text="Deadlift (lbs)")
        deadlift_label.grid(row=5, column=1, sticky=tk.W + tk.N)

        self.weight_entry = ttk.Entry(self.main_frame, width=25)
        self.weight_entry.grid(row=2, column=2, sticky=tk.N, pady=5)
        self.weight_entry.insert(tk.END, "Enter weight here")

        self.bench_entry = ttk.Entry(self.main_frame, width=25)
        self.bench_entry.grid(row=3, column=2, sticky=tk.N, pady=5)
        self.bench_entry.insert(tk.END, "Enter bench max here")

        self.squat_entry = ttk.Entry(self.main_frame, width=25)
        self.squat_entry.grid(row=4, column=2, sticky=tk.N, pady=5)
        self.squat_entry.insert(tk.END, "Enter squat max here")

        self.deadlift_entry = ttk.Entry(self.main_frame, width=25)
        self.deadlift_entry.grid(row=5, column=2, sticky=tk.N, pady=5)
        self.deadlift_entry.insert(tk.END, "Enter deadlift max here")

        # The Commands
        calculate_button = tk.Button(self.main_frame, text="Calculate", command=self.on_calc)
        calculate_button.grid(row=5, column=3, sticky=tk.E, padx=2)

        # Quit button in the lower right corner
        quit_button = ttk.Button(self.window, text="Quit", command=self.window.destroy)
        quit_button.grid(row=2, column=1, sticky=tk.E)

    def on_calc(self):
        try:
            bw = int(self.weight_entry.get()) / 2.205
            total_lift = (int(self.bench_entry.get()) + int(self.squat_entry.get()) + int(self.deadlift_entry.get())) / 2.205

            if self.radio_val.get() == 0:
                denominator = self.m_a + self.m_b * bw + self.m_c * bw ** 2 + self.m_d * bw ** 3 + self.m_e * bw ** 4 + self.m_f * bw ** 5
            else:
                denominator = self.f_a + self.f_b * bw + self.f_c * bw ** 2 + self.f_d * bw ** 3 + self.f_e * bw ** 4 + self.f_f * bw ** 5

            self.score = total_lift * (500 / denominator)
            self.weight_final['text'] = "Your Wilkes Score:" + str(self.score)
        except:
            self.weight_final['text'] = "Please enter integers into the text boxes above"


# Create the entire GUI program and start the GUI event loop
program = WilkesWindow()
program.window.mainloop()
