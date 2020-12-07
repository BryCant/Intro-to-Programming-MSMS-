import tkinter as tk
from tkinter import ttk


class WilksPerkins:
    def __init__(self):
        self.window = tk.Tk()  # create window containing errthang
        self.window.title("perkinsBryant_Homework4")  # title of window
        self.score = "Your Wilks Score: "  # Default results text
        self.weight_entry = tk.StringVar()  # var will store weight text box contents
        self.bench_entry = tk.StringVar()  # var will store bench max text box contents
        self.squat_entry = tk.StringVar()  # var will store squat max text box contents
        self.deadlift_entry = tk.StringVar()  # var will store deadlift max text box contents
        self.main_frame = ttk.LabelFrame(self.window, text="Wilks Coefficient Calculator", relief=tk.RIDGE, padding=6)
        self.results = ttk.Label(self.window, text="Your Wilks Score:")  # label that will show results
        self.results.grid(row=2, column=1, sticky=tk.W + tk.N)  # place results underneath everything beside quit button
        self.radio_val = tk.IntVar()  # radiobutton value stored as either male(0) or female(1)
        self.create_widgets()  # render each widget instantiated

    def create_widgets(self):
        # Create some room around all the internal frames
        self.window['padx'], self.window['pady'] = 4, 4  # spacing around main_frame
        self.main_frame = ttk.LabelFrame(self.window, text="Wilks Calculator", relief=tk.RIDGE, padding=6)
        self.main_frame.grid(row=1, column=1, padx=6, sticky=tk.E + tk.W + tk.N + tk.S)

        # The Choices via Radiobutton
        self.radio_val.set(0)  # default selected button is male

        sex_label = ttk.Label(self.main_frame, width=17, text="Choose your sex")  # Label for sex radio buttons
        sex_label.grid(row=1, column=1, sticky=tk.W + tk.N)  # placed beside radio buttons

        male_button = ttk.Radiobutton(self.main_frame, text="Male", variable=self.radio_val, value=0)
        female_button = ttk.Radiobutton(self.main_frame, text="Female", variable=self.radio_val, value=1)

        male_button.grid(row=1, column=2, sticky=tk.W)      # place on same column
        female_button.grid(row=1, column=2, sticky=tk.E)    # but stuck to different sides

        # The Data entries
        weight_label = ttk.Label(self.main_frame, text="Weight (lbs)")
        weight_label.grid(row=2, column=1, sticky=tk.W + tk.N)

        bench_label = ttk.Label(self.main_frame, text="Bench Press (lbs)")
        bench_label.grid(row=3, column=1, sticky=tk.W + tk.N)

        squat_label = ttk.Label(self.main_frame, text="Squat (lbs)")
        squat_label.grid(row=4, column=1, sticky=tk.W + tk.N)

        deadlift_label = ttk.Label(self.main_frame, text="Deadlift (lbs)")
        deadlift_label.grid(row=5, column=1, sticky=tk.W + tk.N)

        self.weight_entry = ttk.Entry(self.main_frame, width=25)     # create text boxes, with hints, in main_frame
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

        # Calculate Button
        calculate_button = tk.Button(self.main_frame, text="Calculate", command=self.on_calc)  # a click calls on_calc
        calculate_button.grid(row=5, column=3, sticky=tk.E, padx=2)  # beside last text boxes

        # Quit button in the lower right corner
        quit_button = ttk.Button(self.window, text="Quit", command=self.window.destroy)  # calls built-in destroy()
        quit_button.grid(row=2, column=1, sticky=tk.E)

    def on_calc(self):
        # try/except just in case all text boxed don't have integer values
        try:
            bw = int(self.weight_entry.get()) / 2.20462262185  # body weight conversion from lbs to kg
            total_lift = (int(self.bench_entry.get()) + int(self.squat_entry.get()) + int(self.deadlift_entry.get())) / 2.20462262185

            if self.radio_val.get() == 0:  # if male(0) use male constants
                # all the constants
                a, b, c, d, e, f = -216.047514, 16.2606339, -0.002388645, -0.00113732, 7.01863E-06, -1.291E-08
            else:  # else(1) use female constants
                a, b, c, d, e, f = 594.31747775582, -27.23842536447, 0.82112226871, -0.00930733913, 4.731582E-05, -9.054E-08

            denominator = a + b * bw + c * bw ** 2 + d * bw ** 3 + e * bw ** 4 + f * bw ** 5
            self.score = total_lift * (500 / denominator)
            self.results['text'] = f"Your Wilks Score: {str(self.score)} \n[Wilks Coefficient: {500/denominator}]"
        except:
            self.results['text'] = "Please enter integers into ALL text boxes above"


# Create the entire GUI program and start the GUI event loop
program = WilksPerkins()
program.window.mainloop()
