import tkinter as tk
import subprocess

# Create the main window
window = tk.Tk()

# Set the window title
window.title("Time Input")

# Create a label and a time input field
tk.Label(window, text="Enter time (in seconds):").pack()
time_input = tk.Entry(window)
time_input.pack()

# Create a submit button
def submit():
    # Get the time value from the input field
    time = time_input.get()
    # Convert the time value to an integer
    time = int(time)
    # Run the script for the specified time
    subprocess.run(["python", "C:/Users/wolfi/OneDrive/Desktop/Coding/Lock In Program - Alpha/program.py"], timeout = time)
    subprocess.terminate()

submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.pack()
#while True:
#    window.update()
# Run the main loop
window.mainloop()
