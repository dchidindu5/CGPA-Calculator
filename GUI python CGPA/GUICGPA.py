import tkinter as tk
import json

class CGPACalculator:
    def __init__(self, master):
        self.master = master
        master.title("CGPA Calculator")
        
        # Create menu bar
        menubar = tk.Menu(master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save Results", command=self.save_results)
        filemenu.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        master.config(menu=menubar)
        
        # Create input fields and labels
        self.credits_label = tk.Label(master, text="Enter Credits:")
        self.credits_label.grid(row=0, column=0)
        self.credits_entry = tk.Entry(master)
        self.credits_entry.grid(row=0, column=1)
        
        self.grade_label = tk.Label(master, text="Enter Grade:")
        self.grade_label.grid(row=1, column=0)
        self.grade_entry = tk.Entry(master)
        self.grade_entry.grid(row=1, column=1)
        
        # Create add course button
        self.add_course_button = tk.Button(master, text="Add Course", command=self.add_course)
        self.add_course_button.grid(row=2, column=0, columnspan=2)
        
        # Create CGPA label
        self.cgpa_label = tk.Label(master, text="")
        self.cgpa_label.grid(row=3, column=0, columnspan=2)
        
        # Create a list to store the credits and grades of all courses
        self.courses = []
        
        # Create a dictionary to store the final results of all courses
        self.results = {}
    
    def add_course(self):
        # Get input values
        try:
            credits = float(self.credits_entry.get())
            grade = self.grade_entry.get().upper()
            if grade not in ['A', 'B', 'C', 'D', 'E', 'F']:
                raise ValueError('Invalid grade!')
        except ValueError as e:
            # Display error message for invalid input values
            self.cgpa_label.config(text=str(e))
            return
        
        # Append course to the list
        self.courses.append((credits, grade))
        
        # Save result to dictionary
        self.results[credits] = grade
        
        # Clear input fields
        self.credits_entry.delete(0, tk.END)
        self.grade_entry.delete(0, tk.END)
        
        # Update CGPA label
        total_credits = sum([course[0] for course in self.courses])
        total_grades = sum([self.grade_to_point(course[1]) * course[0] for course in self.courses])
        cgpa = total_grades / total_credits
        self.cgpa_label.config(text=f"Your CGPA is {cgpa:.2f}")
    
    def save_results(self):
        # Save results to JSON file
        with open("cgpa_results.json", "w") as file:
            json.dump(self.results, file)
    
    def grade_to_point(self, grade):
        if grade == 'A':
            return 5.0
        elif grade == 'B':
            return 4.0
        elif grade == 'C':
            return 3.0
        elif grade == 'D':
            return 2.0
        elif grade == 'E':
            return 1.0
        elif grade == 'F':
            return 0.0

root = tk.Tk()
cgpa_calculator = CGPACalculator(root)
root.mainloop()
