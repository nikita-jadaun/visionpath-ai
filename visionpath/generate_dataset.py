import random
import pandas as pd

educations = [
    "12th",
    "Diploma",
    "BCA",
    "B.Tech",
    "B.Sc",
    "MCA",
    "M.Tech",
    "MBA"
]

careers = [
    "Software Engineer",
    "Data Analyst",
    "Data Scientist",
    "AI Engineer",
    "Cybersecurity Analyst",
    "Cloud Engineer",
    "Web Developer",
    "UI UX Designer",
    "Product Manager"
]

work_styles = [
    "Remote",
    "Hybrid",
    "Office"
]

career_skills = {

    "Software Engineer":
        ["Python","Java","ProblemSolving","Communication"],

    "Data Analyst":
        ["Python","SQL","Communication"],

    "Data Scientist":
        ["Python","SQL","MachineLearning","ProblemSolving"],

    "AI Engineer":
        ["Python","MachineLearning","ProblemSolving","Communication"],

    "Cybersecurity Analyst":
        ["Python","ProblemSolving","Communication"],

    "Cloud Engineer":
        ["Python","Java","ProblemSolving"],

    "Web Developer":
        ["HTML","JavaScript","ProblemSolving"],

    "UI UX Designer":
        ["Communication","ProblemSolving"],

    "Product Manager":
        ["Leadership","Communication","ProblemSolving"]
}

salary_range = {

    "Software Engineer": (6,20),

    "Data Analyst": (6,18),

    "Data Scientist": (10,30),

    "AI Engineer": (12,35),

    "Cybersecurity Analyst": (8,25),

    "Cloud Engineer": (10,28),

    "Web Developer": (5,15),

    "UI UX Designer": (5,18),

    "Product Manager": (12,30)
}

dataset = []

for i in range(1000):

    age = random.randint(18,45)

    education = random.choice(educations)

    experience = random.randint(0,15)

    career = random.choice(careers)

    salary = random.randint(
        salary_range[career][0],
        salary_range[career][1]
    )

    work_style = random.choice(work_styles)

    savings_goal = random.choice([
        10000,
        20000,
        30000,
        40000,
        50000,
        60000,
        80000
    ])

    skills = {

        "Python":0,

        "SQL":0,

        "MachineLearning":0,

        "Java":0,

        "HTML":0,

        "JavaScript":0,

        "Communication":0,

        "Leadership":0,

        "ProblemSolving":0
    }

    required = career_skills[career]

    # Required skills have 90% chance

    for skill in required:

        if random.random() < 0.9:
            skills[skill] = 1

    # Other skills have 30% chance

    for skill in skills:

        if skills[skill] == 0:

            if random.random() < 0.3:
                skills[skill] = 1


    score = 0

    score += experience

    score += sum(skills.values())

    if education in ["M.Tech","MBA","MCA"]:
        score += 3

    elif education in ["B.Tech","BCA","B.Sc"]:
        score += 2

    elif education == "Diploma":
        score += 1


    if salary <= 12 and score >= 5:

        dream_status = "Achievable"

    elif salary <= 20 and score >= 8:

        dream_status = "Achievable"

    elif salary <= 30 and score >= 11:

        dream_status = "Achievable"

    elif score >= 5:

        dream_status = "Challenging"

    else:

        dream_status = "Ambitious"


    dataset.append({

        "Age": age,

        "Education": education,

        "Experience": experience,

        "Python": skills["Python"],

        "SQL": skills["SQL"],

        "MachineLearning": skills["MachineLearning"],

        "Java": skills["Java"],

        "HTML": skills["HTML"],

        "JavaScript": skills["JavaScript"],

        "Communication": skills["Communication"],

        "Leadership": skills["Leadership"],

        "ProblemSolving": skills["ProblemSolving"],

        "DreamCareer": career,

        "DreamSalaryLPA": salary,

        "WorkStyle": work_style,

        "SavingsGoal": savings_goal,

        "DreamStatus": dream_status
    })


df = pd.DataFrame(dataset)


df.to_csv("lifestyle_dataset.csv", index=False)

print(df.head())

print("\nDataset Created Successfully!")

print(f"Total Records : {len(df)}")