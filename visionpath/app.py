from flask import Flask, render_template
import joblib
from flask import request
import pandas as pd


app = Flask(__name__)

# Load Model
model = joblib.load("lifestyle_model.pkl")

# Load Encoders
education_encoder = joblib.load("education_encoder.pkl")
career_encoder = joblib.load("career_encoder.pkl")
workstyle_encoder = joblib.load("workstyle_encoder.pkl")
status_encoder = joblib.load("status_encoder.pkl")



@app.route("/")
def home():
    return render_template("index.html")




@app.route("/predict", methods=["POST"])
def predict():

    age = int(request.form["Age"])
    education = request.form["Education"]
    experience = int(request.form["Experience"])

    # Convert range slider (0-10) to binary (0/1) for model compatibility
    def slider_to_binary(val):
        return 1 if int(val) >= 5 else 0

    python_skill = slider_to_binary(request.form["Python"])
    sql = slider_to_binary(request.form["SQL"])
    ml = slider_to_binary(request.form["MachineLearning"])
    java = slider_to_binary(request.form["Java"])
    html = slider_to_binary(request.form["HTML"])
    javascript = slider_to_binary(request.form["JavaScript"])
    communication = slider_to_binary(request.form["Communication"])
    leadership = slider_to_binary(request.form["Leadership"])
    problem_solving = slider_to_binary(request.form["ProblemSolving"])

    career = request.form["DreamCareer"]
    salary = int(request.form["DreamSalaryLPA"])
    workstyle = request.form["WorkStyle"]
    savings = int(request.form["SavingsGoal"])

    # Encode categorical values
    education = education_encoder.transform([education])[0]
    career = career_encoder.transform([career])[0]
    workstyle = workstyle_encoder.transform([workstyle])[0]

    # Create DataFrame
    input_data = pd.DataFrame([{
        "Age": age,
        "Education": education,
        "Experience": experience,
        "Python": python_skill,
        "SQL": sql,
        "MachineLearning": ml,
        "Java": java,
        "HTML": html,
        "JavaScript": javascript,
        "Communication": communication,
        "Leadership": leadership,
        "ProblemSolving": problem_solving,
        "DreamCareer": career,
        "DreamSalaryLPA": salary,
        "WorkStyle": workstyle,
        "SavingsGoal": savings
    }])

    prediction = model.predict(input_data)[0]

    result = status_encoder.inverse_transform([prediction])[0]

# Career Roadmap Data
    career_roadmaps = {
        "Software Engineer": {
            "skills": ["Python", "Java", "SQL", "ProblemSolving"],
            "roadmap": [
                ("Learn DSA & Algorithms", "Master data structures, algorithms, and problem-solving on platforms like LeetCode.", "0-3 months"),
                ("Build Projects", "Create 2-3 full-stack projects using modern frameworks (React, Node.js, Django).", "3-6 months"),
                ("Master System Design", "Learn system design concepts, microservices, and cloud deployment (AWS/Azure).", "6-9 months"),
                ("Contribute to Open Source", "Contribute to popular GitHub repos to build your developer profile.", "6-12 months"),
                ("Prepare for Interviews", "Practice mock interviews, solve 100+ coding problems, and build your resume.", "9-12 months"),
            ]
        },
        "Data Analyst": {
            "skills": ["Python", "SQL", "Communication", "ProblemSolving"],
            "roadmap": [
                ("Master SQL & Excel", "Become proficient in complex SQL queries, joins, and Excel analytics.", "0-2 months"),
                ("Learn Python for Data Analysis", "Master Pandas, NumPy, Matplotlib, and Seaborn libraries.", "2-4 months"),
                ("Build a Portfolio", "Analyze 3 real-world datasets and create dashboards using Tableau/Power BI.", "4-6 months"),
                ("Statistics & Business Acumen", "Learn statistical analysis, A/B testing, and business metrics.", "4-7 months"),
                ("Apply for Internships", "Start applying for data analyst internships and junior positions.", "6-12 months"),
            ]
        },
        "Data Scientist": {
            "skills": ["Python", "MachineLearning", "SQL", "ProblemSolving"],
            "roadmap": [
                ("Strengthen Math & Stats", "Master linear algebra, calculus, probability, and statistical inference.", "0-3 months"),
                ("Master ML Algorithms", "Learn supervised/unsupervised learning, deep learning, and NLP.", "3-6 months"),
                ("Build ML Projects", "Implement end-to-end ML projects with deployment using Flask/FastAPI.", "6-9 months"),
                ("Kaggle Competitions", "Participate in Kaggle competitions to gain practical experience.", "6-12 months"),
                ("Publish Research", "Write blogs or research papers on your ML experiments and findings.", "9-12 months"),
            ]
        },
        "AI Engineer": {
            "skills": ["Python", "MachineLearning", "Java", "ProblemSolving"],
            "roadmap": [
                ("Deep Learning Foundations", "Master neural networks, CNNs, RNNs, Transformers, and GANs.", "0-3 months"),
                ("Learn AI Frameworks", "Get proficient with TensorFlow, PyTorch, and Hugging Face libraries.", "3-6 months"),
                ("Build AI Applications", "Create AI-powered apps (chatbots, image recognition, recommendation systems).", "6-9 months"),
                ("MLOps & Deployment", "Learn model deployment, Docker, Kubernetes, and CI/CD for ML.", "6-10 months"),
                ("Advanced Specialization", "Dive deep into NLP, Computer Vision, or Reinforcement Learning.", "9-12 months"),
            ]
        },
        "Cybersecurity Analyst": {
            "skills": ["Python", "ProblemSolving", "Communication", "Leadership"],
            "roadmap": [
                ("Networking Fundamentals", "Master TCP/IP, DNS, HTTP, and network security protocols.", "0-2 months"),
                ("Learn Security Tools", "Get hands-on with Wireshark, Nmap, Metasploit, and Burp Suite.", "2-4 months"),
                ("Certifications", "Prepare for CompTIA Security+, CEH, or CISSP certifications.", "4-8 months"),
                ("Practice CTF Challenges", "Participate in Capture The Flag challenges on HackTheBox, TryHackMe.", "4-10 months"),
                ("Build Security Projects", "Create security tools, write penetration testing reports, and audit systems.", "8-12 months"),
            ]
        },
        "Cloud Engineer": {
            "skills": ["Python", "SQL", "ProblemSolving", "Communication"],
            "roadmap": [
                ("Cloud Fundamentals", "Learn AWS/Azure/GCP core services: EC2, S3, Lambda, VPC.", "0-2 months"),
                ("Infrastructure as Code", "Master Terraform, CloudFormation, and Docker containerization.", "2-5 months"),
                ("Kubernetes & Orchestration", "Learn Kubernetes for container orchestration and microservices.", "5-8 months"),
                ("CI/CD & DevOps", "Set up Jenkins, GitHub Actions, and monitoring with Prometheus/Grafana.", "6-9 months"),
                ("Cloud Architecture", "Design scalable cloud architectures and prepare for AWS Solutions Architect cert.", "9-12 months"),
            ]
        },
        "Web Developer": {
            "skills": ["HTML", "JavaScript", "Python", "ProblemSolving"],
            "roadmap": [
                ("Master Frontend Basics", "Deep dive into HTML5, CSS3, JavaScript (ES6+), and responsive design.", "0-2 months"),
                ("Learn a Framework", "Master React.js or Vue.js with state management and routing.", "2-4 months"),
                ("Backend Development", "Learn Node.js/Express or Django for backend APIs and databases.", "4-6 months"),
                ("Full Stack Projects", "Build 3 full-stack projects with authentication, databases, and deployment.", "6-9 months"),
                ("Deploy & Showcase", "Deploy projects on Vercel/Netlify, build a portfolio site, and freelance.", "9-12 months"),
            ]
        },
        "UI UX Designer": {
            "skills": ["HTML", "JavaScript", "Communication", "Leadership"],
            "roadmap": [
                ("Design Fundamentals", "Learn color theory, typography, layout, and design principles.", "0-2 months"),
                ("Master Figma", "Become proficient in Figma for wireframing, prototyping, and design systems.", "2-4 months"),
                ("User Research", "Learn user research methods, personas, journey mapping, and usability testing.", "3-5 months"),
                ("Build a Portfolio", "Redesign 3 existing apps and create case studies for your portfolio.", "5-8 months"),
                ("Get Certified", "Take Google UX Design Certificate or similar programs.", "6-10 months"),
            ]
        },
        "Product Manager": {
            "skills": ["Communication", "Leadership", "ProblemSolving", "SQL"],
            "roadmap": [
                ("Learn Product Management", "Master product lifecycle, roadmap planning, and agile methodologies.", "0-2 months"),
                ("Data-Driven Decisions", "Learn SQL, A/B testing, analytics tools (Google Analytics, Mixpanel).", "2-4 months"),
                ("Build a Product", "Create a MVP, gather user feedback, and iterate on the product.", "4-6 months"),
                ("Networking & Mentorship", "Connect with PMs on LinkedIn, attend product conferences.", "4-8 months"),
                ("Apply for APM Roles", "Apply for Associate Product Manager programs at top tech companies.", "8-12 months"),
            ]
        }
    }

    # Get roadmap for the selected career (default to Software Engineer)
    career_key = request.form["DreamCareer"]
    roadmap_data = career_roadmaps.get(career_key, career_roadmaps["Software Engineer"])

    # Analyze skill gaps
    skill_gaps = []
    for skill_name in roadmap_data["skills"]:
        skill_value = int(request.form.get(skill_name, "0"))
        if skill_value >= 7:
            skill_gaps.append({"name": skill_name, "status": "strong", "label": "✅ Strong"})
        elif skill_value >= 4:
            skill_gaps.append({"name": skill_name, "status": "needs-work", "label": "⚠️ Needs Work"})
        else:
            skill_gaps.append({"name": skill_name, "status": "gap", "label": "❌ Gap"})

    # Determine which roadmap items are completed/current based on experience
    roadmap_items = []
    exp_level = experience
    for i, (title, desc, duration) in enumerate(roadmap_data["roadmap"]):
        if i < exp_level and result == "Achievable":
            roadmap_items.append({"title": title, "desc": desc, "duration": duration, "status": "completed"})
        elif i == exp_level or (i == 0 and exp_level == 0):
            roadmap_items.append({"title": title, "desc": desc, "duration": duration, "status": "current"})
        else:
            roadmap_items.append({"title": title, "desc": desc, "duration": duration, "status": "upcoming"})

    if result == "Achievable":
        message = "🎉 Great! Your profile strongly matches your dream lifestyle. Keep up the momentum!"
    elif result == "Challenging":
        message = "📈 You're close! Focus on closing the skill gaps below and gaining more experience."
    else:
        message = "🚀 Your dream is ambitious! Follow the roadmap below step by step to make it happen."

    return render_template(
    "result.html",
    prediction=result,
    message=message,
    age=age,
    education=request.form["Education"],
    experience=experience,
    career=request.form["DreamCareer"],
    salary=salary,
    workstyle=request.form["WorkStyle"],
    roadmap=roadmap_items,
    skill_gaps=skill_gaps
)

if __name__ == "__main__":
    app.run(debug=True)
