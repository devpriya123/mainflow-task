import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("student-mat.csv", sep=";")
print("Data loaded successfully!")
# 2. Data Exploration
print(data.head())   
print("\Dataset Info:")
print(data.info()) 

print("\nMissing values:")
print(data.isnull().sum())

data = data.drop_duplicates()

average_score = data['G3'].mean()
print(f"\nAverage math score (G3):{average_score: .2f}")

students_above_15 = len(data[data['G3']> 15])
print(f"number of students scoring above 15: {students_above_15}")

correlation = data['studytime'].corr(data['G3'])
print(f"correlation between study time and final grade: {correlation:.2f}")

average_grade_by_gender = data.groupby('sex')['G3'].mean()
print("\naverage final grade by gender:")
print(average_grade_by_gender)

# 5. Data Visualization
# histogram of final grades
plt.figure(figsize=(8, 6))
plt.hist(data["G3"], bins=10, color="skyblue", edgecolor="black")
plt.xlabel("Final Grade (G3)")
plt.ylabel("Frequency")
plt.title("Distribution of Final Grades")
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x="studytime", y="G3", hue='sex')
plt.xlabel("Study Time (hours/week)")
plt.ylabel("Final Grade (G3)")
plt.title("Study Time vs. Final Grade")
plt.show()

plt.figure(figsize=(8, 6))
average_grade_by_gender.plot(kind="bar", color=["blue", "pink"])
plt.xlabel("Gender")
plt.ylabel("Average Final Grade (G3)")
plt.title("Average Scores by Gender")
plt.xticks(rotation=0)
plt.show()