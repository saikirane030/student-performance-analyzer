import numpy as np
import pandas as pd

df = pd.read_csv('student_data.csv')
df.fillna(df.mean(numeric_only=True), inplace=True)

marks = df[['Math', 'Science', 'English']].to_numpy()
total_marks = np.sum(marks, axis=1)
average_marks = np.mean(marks, axis=1)

df['Total'] = total_marks
df['Average'] = average_marks

high_achievers = df[df['Average'] > 80]

mask_low = (marks < 70)
low_scores = df[np.any(mask_low, axis=1)]

attendance_df = pd.DataFrame({
    'StudentID': [1, 2, 3, 4, 5],
    'Attendance (%)': [90, 85, 80, 95, 70]
})
merged_df = pd.merge(df, attendance_df, on='StudentID')

print("Original Data:")
print(df)
print("\nHigh Achievers:")
print(high_achievers)
print("\nStudents with Low Scores:")
print(low_scores)
print("\nFinal Merged Data:")
print(merged_df)