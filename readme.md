# 🎓 Student Score Analysis System

A **Student Performance Management and Analytics System** developed using Python, NumPy, Pandas, Matplotlib, Seaborn, and Streamlit.

This project helps manage student academic records, calculate internal and final examination scores, automatically assign grades, and analyze student performance through interactive dashboards and data visualizations.

## 🚀 Key Features

### 1. Interactive Dashboard
- Total Number of Students
- Average Student Score
- Highest Student Score
- Pass Percentage
- Recent Student Records

### 2. Add Student Records
- Enter student details.
- Record daily study hours.
- Track attendance percentage.
- Enter previous examination scores.
- Track completed assignments.
- Enter final examination marks.
- Automatically calculate internal marks.
- Automatically calculate total scores.
- Automatically assign grades.

### 3. View Student Data
- Display all student records.
- View complete student information.
- Download student records in CSV format.

### 4. Student Performance Analysis

Interactive data visualizations using Matplotlib and Seaborn:

- Grade Distribution
- Total Score Distribution
- Average Score by Grade
- Study Hours vs Total Score
- Attendance vs Total Score
- Student Performance Correlation Heatmap

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core Programming |
| NumPy | Numerical Computations |
| Pandas | Data Management and Analysis |
| Matplotlib | Data Visualization |
| Seaborn | Statistical Data Visualization |
| Streamlit | Interactive Dashboard Development |

## 📂 Project Structure

```text
student-score-analysis/
│
├── app.py
│
├── data/
│   └── predictions.csv
│
├── requirements.txt
│
└── README.md
```

## ⚙️ Installation and Setup

Follow these steps to run the project locally.

### Step 1: Clone the Repository

```bash
git clone https://github.com/anshnegi2005/student-score-analysis.git
```

### Step 2: Navigate to Project Directory

```bash
cd student-score-analysis
```

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
streamlit run app.py
```

The application will open in your default web browser.

## 📊 Grading System

The system automatically assigns grades based on the total score obtained by students.

| Total Score | Grade |
|---|---|
| 90–100 | A+ |
| 80–89 | A |
| 70–79 | B+ |
| 60–69 | B |
| 50–59 | C+ |
| 40–49 | C |
| 33–39 | D |
| Below 33 | F |

## 📈 Internal Marks Calculation

Internal marks are calculated out of 20 based on four parameters:

| Parameter | Marks |
|---|---:|
| Attendance | 5 |
| Previous Score | 5 |
| Study Hours | 5 |
| Assignments | 5 |
| **Total** | **20** |

**Total Score = Internal Marks + Final Examination Marks**

- Internal Assessment: 20 Marks
- Final Examination: 80 Marks
- Maximum Total Score: 100 Marks

## 💡 Key Learnings

Through this project, I gained practical experience in:

- Data manipulation and analysis using Pandas.
- Numerical computations using NumPy.
- Data visualization using Matplotlib and Seaborn.
- Creating interactive dashboards using Streamlit.
- Handling CSV files and student records.
- Implementing automated score calculations and grade assignment.
- Analyzing relationships between academic performance parameters.

## 🎯 Project Objective

The main objective of this project is to develop a student performance management system that combines academic data management, automated score calculation, and interactive data visualization.

It demonstrates the practical application of Python and data analytics libraries in managing and analyzing student academic performance.

## 👨‍💻 Author

**Ansh Singh Negi**

Python Developer | Data Analytics Enthusiast

## 🔗 GitHub Repository

[Student Score Analysis System](https://github.com/anshnegi2005/student-score-analysis)

