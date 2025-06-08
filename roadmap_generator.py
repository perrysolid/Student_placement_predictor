branch_fields = {
    'Computer Science': ['Web Development', 'Machine Learning', 'Cybersecurity', 'App Development'],
    'Electronics': ['Embedded Systems', 'IoT', 'VLSI Design', 'Signal Processing'],
    'Mechanical': ['CAD', 'Thermodynamics', 'Robotics', 'Manufacturing Processes'],
    'Civil': ['Structural Design', 'Construction Management', 'Surveying', 'GIS'],
    'Electrical': ['Power Systems', 'Control Systems', 'Electric Vehicles', 'Smart Grids'],
    'Chemical': ['Process Engineering', 'Fluid Mechanics', 'Chemical Reactions']
}


roadmap_links = {
    "Artificial Intelligence": {
        "elementary": [
            "https://www.coursera.org/learn/ai-for-everyone",
            "https://www.udacity.com/course/ai-for-beginners--ud410"
        ],
        "intermediate": [
            "https://www.coursera.org/specializations/deep-learning",
            "https://www.edx.org/professional-certificate/harvardx-artificial-intelligence"
        ],
        "advanced": [
            "https://openai.com/research",
            "https://ai.stanford.edu/courses/"
        ]
    },
    "Machine Learning": {
        "elementary": [
            "https://www.coursera.org/learn/machine-learning",
            "https://www.kaggle.com/learn/intro-to-machine-learning"
        ],
        "intermediate": [
            "https://www.coursera.org/specializations/machine-learning",
            "https://www.udacity.com/course/machine-learning-engineer-nanodegree--nd009t"
        ],
        "advanced": [
            "https://stanford.edu/~shervine/teaching/cs-229",
            "https://www.deeplearning.ai/ai-notes/"
        ]
    },
    "Cloud Computing": {
        "elementary": [
            "https://www.coursera.org/learn/cloud-computing-basics",
            "https://aws.amazon.com/training/course-descriptions/cloud-practitioner-essentials/"
        ],
        "intermediate": [
            "https://www.coursera.org/professional-certificates/aws-cloud-solutions-architect",
            "https://cloud.google.com/certification/cloud-architect"
        ],
        "advanced": [
            "https://www.edx.org/professional-certificate/linuxfoundationx-cloud-computing",
            "https://www.cloudarchitecture.institute/"
        ]
    },
    "Cybersecurity": {
        "elementary": [
            "https://www.coursera.org/learn/cybersecurity-fundamentals",
            "https://www.udacity.com/course/intro-to-cybersecurity--ud1337"
        ],
        "intermediate": [
            "https://www.sans.org/cyber-security-training/",
            "https://www.coursera.org/professional-certificates/google-cybersecurity"
        ],
        "advanced": [
            "https://www.offensive-security.com/",
            "https://www.blackhat.com/training/"
        ]
    },
    "5G/6G Network Technologies": {
        "elementary": [
            "https://www.coursera.org/learn/5g-fundamentals",
            "https://www.edx.org/course/5g-fundamentals"
        ],
        "intermediate": [
            "https://www.ieee.org/conferences/networking/5g-summit.html",
            "https://www.3gpp.org/technologies/5g-system-overview"
        ],
        "advanced": [
            "https://www.5gamericas.org/",
            "https://5gobservatory.eu/"
        ]
    },
    "Embedded Systems": {
        "elementary": [
            "https://www.coursera.org/learn/introduction-embedded-systems",
            "https://www.udemy.com/topic/embedded-systems/"
        ],
        "intermediate": [
            "https://www.edx.org/professional-certificate/embedded-systems-design",
            "https://www.udacity.com/course/embedded-systems-nanodegree--nd156"
        ],
        "advanced": [
            "https://ocw.mit.edu/courses/6-088-introduction-to-embedded-systems-fall-2005/",
            "https://www.embedded.com/"
        ]
    },
    "Robotics": {
        "elementary": [
            "https://www.coursera.org/learn/robotics-fundamentals",
            "https://www.edx.org/learn/robotics"
        ],
        "intermediate": [
            "https://www.udacity.com/course/robotics-software-engineer--nd209",
            "https://www.coursera.org/specializations/robotics"
        ],
        "advanced": [
            "https://www.ri.cmu.edu/education/",
            "https://www.robotics.org/"
        ]
    },
    "Smart Grid Technologies": {
        "elementary": [
            "https://www.coursera.org/learn/smart-grid-fundamentals",
            "https://www.edx.org/course/smart-grid-fundamentals"
        ],
        "intermediate": [
            "https://www.ieee.org/conferences/networking/smart-grid-summit.html",
            "https://www.coursera.org/specializations/smart-grid-technology"
        ],
        "advanced": [
            "https://smartgrid.ieee.org/",
            "https://www.energy.gov/oe/activities/technology-development/grid-modernization-and-smart-grid"
        ]
    },
    "Automotive Engineering": {
        "elementary": [
            "https://www.coursera.org/learn/automotive-engineering-basics",
            "https://www.udemy.com/topic/automotive-engineering/"
        ],
        "intermediate": [
            "https://www.edx.org/professional-certificate/automotive-engineering",
            "https://www.udacity.com/course/automotive-engineer-nanodegree--nd013"
        ],
        "advanced": [
            "https://www.sae.org/learn",
            "https://www.automotive-engineering.org/"
        ]
    },
    "Sustainable Infrastructure": {
        "elementary": [
            "https://www.coursera.org/learn/sustainable-infrastructure",
            "https://www.edx.org/course/sustainable-infrastructure"
        ],
        "intermediate": [
            "https://www.coursera.org/specializations/sustainable-infrastructure",
            "https://www.worldgreenbuilding.org/education"
        ],
        "advanced": [
            "https://www.sustainableinfrastructure.org/",
            "https://www.istructe.org/sustainability/"
        ]
    },
    "Biotechnology": {
        "elementary": [
            "https://www.coursera.org/learn/biotech-fundamentals",
            "https://www.edx.org/learn/biotechnology"
        ],
        "intermediate": [
            "https://www.coursera.org/specializations/biotechnology",
            "https://www.udacity.com/course/biotechnology-nanodegree"
        ],
        "advanced": [
            "https://www.nature.com/subjects/biotechnology",
            "https://www.biosociety.org/"
        ]
    }
}

def open_link(link):
    webbrowser.open(link)

def update_technical_interests(event):
    branch = branch_combobox.get()
    technical_areas = branch_fields.get(branch, [])
    interest_combobox.config(values=technical_areas)
    interest_combobox.set('')
    roadmap_button.config(state=DISABLED)

def on_interest_select(event):
    if branch_combobox.get() and interest_combobox.get() and skill_level_combobox.get():
        roadmap_button.config(state=NORMAL)
    else:
        roadmap_button.config(state=DISABLED)

def show_roadmap():
    branch = branch_combobox.get()
    interest = interest_combobox.get()
    skill_level = int(skill_level_combobox.get())
    if interest not in branch_fields.get(branch, []):
        messagebox.showerror("Error", f"{interest} is not a valid field for {branch}.")
        return
    level = 'elementary' if skill_level <= 4 else 'intermediate' if skill_level <= 7 else 'advanced'
    links = roadmap_links.get(interest, {}).get(level, [])
    for widget in link_frame.winfo_children():
        widget.destroy()
    if links:
        for link in links:
            btn = Button(link_frame, text=link, command=lambda l=link: open_link(l), wraplength=550, justify=LEFT)
            btn.pack(anchor='w', padx=5, pady=2)
    else:
        messagebox.showinfo("Info", "No resources available for this selection.")
