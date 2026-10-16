import numpy as np
from sklearn.linear_model import LinearRegression
hours=np.array([1,2,3,4,5]).reshape(-1,1)
marks=np.array([35,45,55,65,75])
model=LinearRegression()
model.fit(hours,marks)
study_hours=6
predicted_marks=model.predict([[study_hours]])
print("study hours:",study_hours)
print("predicted marks:",predicted_marks[0])