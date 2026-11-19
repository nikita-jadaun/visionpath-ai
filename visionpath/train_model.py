import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# =====================================
# Load Dataset
# =====================================

df = pd.read_csv("dataset/lifestyle_dataset.csv")
# If your dataset is inside a folder:
# df = pd.read_csv("dataset/lifestyle_dataset.csv")

# =====================================
# Display Dataset
# =====================================

print("First 5 Rows:\n")
print(df.head())

print("\n==============================")
print("Dataset Information")
print("==============================")
print(df.info())

print("\n==============================")
print("Missing Values")
print("==============================")
print(df.isnull().sum())

print("\n==============================")
print("Data Types")
print("==============================")
print(df.dtypes)

# =====================================
# Create Separate Label Encoders
# =====================================

education_encoder = LabelEncoder()
career_encoder = LabelEncoder()
workstyle_encoder = LabelEncoder()
status_encoder = LabelEncoder()

# =====================================
# Encode Categorical Columns
# =====================================

df["Education"] = education_encoder.fit_transform(df["Education"])

df["DreamCareer"] = career_encoder.fit_transform(df["DreamCareer"])

df["WorkStyle"] = workstyle_encoder.fit_transform(df["WorkStyle"])

df["DreamStatus"] = status_encoder.fit_transform(df["DreamStatus"])

# =====================================
# Print Encoded Dataset
# =====================================

print("\n==============================")
print("Encoded Dataset")
print("==============================")
print(df.head())

# =====================================
# Print Label Mappings
# =====================================

print("\n==============================")
print("Education Mapping")
print("==============================")

for i, value in enumerate(education_encoder.classes_):
    print(f"{i} -> {value}")

print("\n==============================")
print("Dream Career Mapping")
print("==============================")

for i, value in enumerate(career_encoder.classes_):
    print(f"{i} -> {value}")

print("\n==============================")
print("Work Style Mapping")
print("==============================")

for i, value in enumerate(workstyle_encoder.classes_):
    print(f"{i} -> {value}")

print("\n==============================")
print("Dream Status Mapping")
print("==============================")

for i, value in enumerate(status_encoder.classes_):
    print(f"{i} -> {value}")

# =====================================
# Save Encoders
# =====================================

joblib.dump(education_encoder, "education_encoder.pkl")
joblib.dump(career_encoder, "career_encoder.pkl")
joblib.dump(workstyle_encoder, "workstyle_encoder.pkl")
joblib.dump(status_encoder, "status_encoder.pkl")

print("\nAll Label Encoders Saved Successfully!")

# =====================================
# Separate Features and Target
# =====================================

X = df.drop("DreamStatus", axis=1)

y = df["DreamStatus"]

# =====================================
# Split Dataset
# =====================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# =====================================
# Display Shapes
# =====================================

print("\n==============================")
print("Training & Testing Shapes")
print("==============================")

print("X_train :", X_train.shape)
print("X_test  :", X_test.shape)
print("y_train :", y_train.shape)
print("y_test  :", y_test.shape)

print("\nData Preprocessing Completed Successfully!")

# =====================================
# Train Decision Tree Model
# =====================================

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

# =====================================
# Prediction
# =====================================

y_pred = model.predict(X_test)

# =====================================
# Accuracy
# =====================================

accuracy = accuracy_score(y_test, y_pred)

print("\n==============================")
print("Model Accuracy")
print("==============================")

print(f"Accuracy : {accuracy*100:.2f}%")

# =====================================
# Confusion Matrix
# =====================================

print("\n==============================")
print("Confusion Matrix")
print("==============================")

print(confusion_matrix(y_test, y_pred))

# =====================================
# Classification Report
# =====================================

print("\n==============================")
print("Classification Report")
print("==============================")

print(classification_report(y_test, y_pred))

# =====================================
# Save Model
# =====================================

joblib.dump(model, "lifestyle_model.pkl")

print("\nModel Saved Successfully!")