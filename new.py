import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from pathlib import Path


DATA_PATH = Path("data/predictions.csv")

DATA_PATH.parent.mkdir(parents=True, exist_ok=True)

COLUMNS = [
    "student_id",
    "student_name",
    "study_hours",
    "attendance",
    "previous_score",
    "assignments_completed",
    "final_score",
    "internal_marks",
    "total_score",
    "grade",
    "record_date",
]

if not DATA_PATH.exists():
    df = pd.DataFrame(columns=COLUMNS)
    df.to_csv(DATA_PATH, index=False)

else:
    df = pd.read_csv(DATA_PATH)

    if df.empty:
        df = pd.DataFrame(columns=COLUMNS)
        df.to_csv(DATA_PATH, index=False)



plt.style.use("dark_background")
plt.rcParams.update({
    "figure.facecolor": "#0E1117",
    "axes.facecolor": "#0E1117",
    "savefig.facecolor": "#0E1117",
    "axes.grid": True,
    "grid.alpha": 0.2,
})


st.set_page_config(
    page_title="Student Score Analysis",
    page_icon="🎓",
    layout="wide"
)


st.title("🎓 Student Score Analysis Pro")

st.caption(
    "Track student performance, analyse study habits "
    "and explore score insights."
)

st.divider()


st.sidebar.title("🎓 SCORE PRO")

st.sidebar.caption("Student Analytics System")

st.sidebar.divider()


MENU_LABELS = {
    "Dashboard": "🏠 Dashboard",
    "Add Student Record": "➕ Add Student Record",
    "View Student Data": "📋 View Student Data",
    "Score Analysis": "📊 Score Analysis",
}

menu = st.sidebar.radio(
    "MAIN MENU",
    [
        "Dashboard",
        "Add Student Record",
        "View Student Data",
        "Score Analysis"
    ],
    format_func=lambda x: MENU_LABELS[x]
)

st.sidebar.divider()

st.sidebar.caption("Built by Ansh Singh Negi")


if menu == "Add Student Record":

    st.header("➕ Add New Student Record")

    st.write("Enter the details below to create a new student record.")

    with st.container(border=True):

        row1_a, row1_b = st.columns(2)

        with row1_a:
            student_name = st.text_input(
                "Student Name",
                placeholder="e.g. Rahul Sharma"
            )

        with row1_b:
            record_date = st.date_input("Record Date")

        row2_a, row2_b = st.columns(2)

        with row2_a:
            study_hours = st.number_input(
                "Study Hours (per day)",
                min_value=0.0,
                max_value=12.0,
                step=0.5
            )

        with row2_b:
            attendance = st.number_input(
                "Attendance (%)",
                min_value=0,
                max_value=100,
                step=1
            )

        row3_a, row3_b = st.columns(2)

        with row3_a:
            previous_score = st.number_input(
                "Previous Score",
                min_value=0,
                max_value=100,
                step=1
            )

        with row3_b:
            assignments_completed = st.number_input(
                "Assignments Submitted (out of 5 assignments)",
                min_value=0,
                max_value=5,
                step=1,
                help="How many of the 5 assignments did the student submit?"
            )

        final_score = st.number_input(
            "Final Exam Score (out of 80)",
            min_value=0,
            max_value=80,
            step=1
        )

    submit = st.button(
        "💾 Save Record",
        use_container_width=True,
        type="primary"
    )

    if submit:

        if student_name.strip() == "" or not student_name.replace(" ", "").isalpha():
            st.error("Enter a valid name")

        elif study_hours < 0 or study_hours > 12:
            st.error("Enter valid study hours")

        elif attendance < 0 or attendance > 100:
            st.error("Enter valid attendance")

        elif previous_score < 0 or previous_score > 100:
            st.error("Enter valid previous score")

        elif assignments_completed < 0 or assignments_completed > 5:
            st.error("Enter valid assignments completed (0 to 5)")

        elif final_score < 0 or final_score > 80:
            st.error("Enter valid final score (0 to 80)")

        else:


            if attendance >= 90:
                attendance_marks = 5
            elif attendance >= 80:
                attendance_marks = 4
            elif attendance >= 70:
                attendance_marks = 3
            elif attendance >= 60:
                attendance_marks = 2
            else:
                attendance_marks = 1


            if previous_score >= 90:
                previous_marks = 5
            elif previous_score >= 80:
                previous_marks = 4
            elif previous_score >= 70:
                previous_marks = 3
            elif previous_score >= 60:
                previous_marks = 2
            else:
                previous_marks = 1


            if study_hours >= 6:
                study_marks = 5
            elif study_hours >= 4:
                study_marks = 4
            elif study_hours >= 3:
                study_marks = 3
            elif study_hours >= 2:
                study_marks = 2
            else:
                study_marks = 1

            if assignments_completed == 5:
                assignment_marks = 5
            elif assignments_completed == 4:
                assignment_marks = 4
            elif assignments_completed == 3:
                assignment_marks = 3
            elif assignments_completed == 2:
                assignment_marks = 2
            else:
                assignment_marks = 1


            internal_marks = attendance_marks + previous_marks + study_marks + assignment_marks

            total_score = final_score + internal_marks


            if total_score >= 90:
                grade = "A+"
            elif total_score >= 80:
                grade = "A"
            elif total_score >= 70:
                grade = "B+"
            elif total_score >= 60:
                grade = "B"
            elif total_score >= 50:
                grade = "C+"
            elif total_score >= 40:
                grade = "C"
            elif total_score >= 33:
                grade = "D"
            else:
                grade = "F"


            new_data = pd.DataFrame([{
                "student_id": len(df) + 1,
                "student_name": student_name,
                "study_hours": study_hours,
                "attendance": attendance,
                "previous_score": previous_score,
                "assignments_completed": assignments_completed,
                "final_score": final_score,
                "internal_marks": internal_marks,
                "total_score": total_score,
                "grade": grade,
                "record_date": record_date
            }])

            df = pd.concat([df, new_data], ignore_index=True)

            df.to_csv(DATA_PATH, index=False)

            st.success("STUDENT RECORD ADDED SUCCESSFULLY")

            st.subheader("🧾 Result Summary: " + student_name)

            with st.container(border=True):

                r1c1, r1c2, r1c3, r1c4 = st.columns(4)

                r1c1.metric("Attendance Marks", str(attendance_marks) + " / 5")
                r1c2.metric("Previous Score Marks", str(previous_marks) + " / 5")
                r1c3.metric("Study Hours Marks", str(study_marks) + " / 5")
                r1c4.metric("Assignment Marks", str(assignment_marks) + " / 5")

                st.caption(
                    "Assignments Submitted: "
                    + str(assignments_completed) + " out of 5"
                )

                st.divider()

                r2c1, r2c2, r2c3, r2c4 = st.columns(4)

                r2c1.metric("Internal Marks", str(internal_marks) + " / 20")
                r2c2.metric("Final Exam Score", str(final_score) + " / 80")
                r2c3.metric("Total Score", str(total_score) + " / 100")
                r2c4.metric("Grade", grade)


elif menu == "View Student Data":

    st.header("📋 Student Records")

    st.dataframe(df, use_container_width=True, hide_index=True)

    st.download_button(
        label="📥 Download CSV",
        data=df.to_csv(index=False),
        file_name="student_data.csv",
        mime="text/csv"
    )



if menu == "Score Analysis":

    st.header("📈 Score Insights")

    if df.empty:
        st.warning("No student records available. Please add student data first.")

    else:


        col_a, col_b = st.columns(2)

        with col_a:

            st.subheader("1. Grade Distribution")

            plt.figure(figsize=(6, 3.5))

            sns.countplot(
                data=df,
                x="grade",
                order=["A+", "A", "B+", "B", "C+", "C", "D", "F"]
            )

            plt.xlabel("Grade")
            plt.ylabel("Number of Students")
            plt.title("Grade Distribution")

            st.pyplot(plt.gcf())
            plt.close()


        with col_b:

            st.subheader("2. Total Score Distribution")

            plt.figure(figsize=(6, 3.5))

            sns.histplot(
                data=df,
                x="total_score",
                kde=True
            )

            plt.xlabel("Total Score")
            plt.ylabel("Number of Students")
            plt.title("Total Score Distribution")

            st.pyplot(plt.gcf())
            plt.close()


        st.divider()

        col_c, col_d = st.columns(2)

        with col_c:

            st.subheader("3. Average Score by Grade")

            plt.figure(figsize=(6, 3.5))

            sns.barplot(
                data=df,
                x="grade",
                y="total_score",
                order=["A+", "A", "B+", "B", "C+", "C", "D", "F"],
                errorbar=None
            )

            plt.xlabel("Grade")
            plt.ylabel("Average Total Score")
            plt.title("Average Score by Grade")

            st.pyplot(plt.gcf())
            plt.close()


        with col_d:

            st.subheader("4. Study Hours vs Total Score")

            plt.figure(figsize=(6, 3.5))

            sns.scatterplot(
                data=df,
                x="study_hours",
                y="total_score",
                hue="grade",
                palette="viridis"
            )

            plt.xlabel("Study Hours")
            plt.ylabel("Total Score")
            plt.title("Study Hours vs Student Performance")

            st.pyplot(plt.gcf())
            plt.close()


        st.divider()

        col_e, col_f = st.columns(2)

        with col_e:

            st.subheader("5. Attendance vs Total Score")

            plt.figure(figsize=(6, 4.5))

            sns.lineplot(
                data=df,
                x="attendance",
                y="total_score",
                marker="o",
                errorbar=None
            )

            plt.xlabel("Attendance (%)")
            plt.ylabel("Total Score")
            plt.title("Attendance vs Total Score")

            st.pyplot(plt.gcf())
            plt.close()


        with col_f:

            st.subheader("6. Student Performance Correlation")

            plt.figure(figsize=(6, 4.5))

            sns.heatmap(
                df.drop(columns=["student_id"]).corr(numeric_only=True),
                annot=True,
                annot_kws={"size": 7},
                cmap="coolwarm",
            )

            plt.title("Student Performance Correlation")

            st.pyplot(plt.gcf())
            plt.close()



if menu == "Dashboard":

    st.header("📊 Dashboard Overview")

    st.caption("Overview of student academic performance")

    st.divider()



    total_students = len(df)

    if total_students > 0:

        average_score = df["total_score"].mean()

        highest_score = df["total_score"].max()

        passed_students = len(df[df["total_score"] >= 33])

        if total_students > 0:
            pass_percentage = (passed_students / total_students) * 100
        else:
            pass_percentage = 0

    else:

        average_score = 0
        highest_score = 0
        pass_percentage = 0



    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Students",
        total_students,
        help="Total number of saved student records"
    )

    col2.metric(
        "Average Score",
        str(round(average_score, 2)),
        help="Mean of total score (out of 100)"
    )

    col3.metric(
        "Highest Score",
        highest_score,
        help="Highest total score (out of 100)"
    )

    col4.metric(
        "Pass Percentage",
        str(round(pass_percentage, 2)) + "%",
        help="Students with total score of 33 or more are counted as pass"
    )

    st.divider()



    st.subheader("📋 Recent Student Records")

    if df.empty:

        st.warning("No student records available. Please add student data.")

    else:

        recent_records = df.tail(5).loc[::-1]

        st.dataframe(
            recent_records,
            use_container_width=True,
            hide_index=True
        )
