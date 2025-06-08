root = Tk()
root.title("Placement Predictor & Career Roadmap")
root.geometry("800x950")

input_frame = Frame(root)
input_frame.pack(pady=10)

entries = {}
fields = ['CGPA', 'Internships', 'Projects', 'Workshops/Certifications', 'SSC_Marks', 'HSC_Marks']
for i, field in enumerate(fields):
    Label(input_frame, text=f"{field}:").grid(row=i, column=0, sticky=W)
    entry = Entry(input_frame)
    entry.grid(row=i, column=1)
    entries[field] = entry

result_label = Label(input_frame, text="Predicted Placement Percentage: N/A", font=('Helvetica', 12, 'bold'))
result_label.grid(row=7, column=0, columnspan=2, pady=10)
metrics_label = Label(input_frame, text="", font=('Helvetica', 10))
metrics_label.grid(row=8, column=0, columnspan=2, pady=5)

def on_predict():
    try:
        inputs = [float(entries[field].get()) for field in fields]
        for i, key in enumerate(feature_weights):
            inputs[i] *= feature_weights[key]
        inputs = np.array(inputs).reshape(1, -1)
        scaled_input = scaler.transform(inputs)
        poly_input = poly.transform(scaled_input)
        placement_probability = model.predict_proba(poly_input)[0][1] * 100
        result_label.config(text=f"Predicted Placement Percentage: {placement_probability:.2f}% ({best_model_name})")

        roadmap_button.config(state=NORMAL)
        metrics_text = f"Accuracy: {accuracy*100:.2f}% | F1 Score: {f1:.2f}\nPrecision: {precision:.2f} | Recall: {recall:.2f}"
        metrics_label.config(text=metrics_text)
    except Exception as e:
        messagebox.showerror("Input Error", f"Enter valid numeric values.\nDetails: {str(e)}")

Button(input_frame, text="Predict Placement", command=on_predict).grid(row=6, column=0, columnspan=2, pady=10)


roadmap_frame = Frame(root)
roadmap_frame.pack(pady=20)
Label(roadmap_frame, text="Branch:").grid(row=0, column=0, sticky=W)
branch_combobox = ttk.Combobox(roadmap_frame, values=[], width=30)
branch_combobox.grid(row=0, column=1)
Label(roadmap_frame, text="Technical Interest:").grid(row=1, column=0, sticky=W)
interest_combobox = ttk.Combobox(roadmap_frame, width=30)
interest_combobox.grid(row=1, column=1)
Label(roadmap_frame, text="Skill Level (1-10):").grid(row=2, column=0, sticky=W)
skill_level_combobox = ttk.Combobox(roadmap_frame, values=list(range(1, 11)), width=30)
skill_level_combobox.grid(row=2, column=1)
roadmap_button = Button(roadmap_frame, text="Get Learning Resources", command=lambda: show_roadmap(), state=DISABLED)
roadmap_button.grid(row=3, column=0, columnspan=2, pady=10)
link_frame_label = Label(root, text="Recommended Learning Resources:", font=('Helvetica', 12, 'bold'))
link_frame_label.pack()
link_frame = Frame(root)
link_frame.pack(padx=10, pady=10, fill=BOTH, expand=True)
