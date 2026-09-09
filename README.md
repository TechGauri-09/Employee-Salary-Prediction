# Employee Salary Prediction

A Machine Learning project that predicts employee salaries based on experience, education, department, and skills. Built as part of the Nettech Data Science Internship.

## 📌 Objective

Build a Machine Learning model to predict employee salaries using features like experience, education, department, and skills, and deploy it via a web interface for real-time predictions.

## 📊 Dataset

Manually created dataset with 100+ records containing the following columns:

| Column | Description |
|---|---|
| Experience | Years of work experience (0–20) |
| Age | Employee age |
| Education | 12th / Diploma / Bachelor's / Master's / PhD |
| Department | IT / HR / Sales / Finance / Marketing / Operations |
| Skills | Primary skill (Python, SQL, Excel, Power BI, Java, Communication) |
| Salary | Target variable — annual salary in INR |

Salary values were generated using a formula based on experience, education level, and controlled random noise to simulate realistic data.

## ⚙️ Tech Stack

- **Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib
- **Web Framework:** Flask
- **Model Persistence:** Pickle

## 🚀 Project Workflow

1. **Data Preprocessing** – Handled categorical encoding (LabelEncoder) and checked for missing values
2. **Train-Test Split** – 80-20 split for model evaluation
3. **Model Training** – Compared multiple regression models:
   - Linear Regression
   - Decision Tree Regressor
   - Random Forest Regressor
4. **Model Evaluation** – Used R² Score, MAE, and RMSE to select the best-performing model
5. **Visualization** – Plotted Actual vs Predicted Salary to visually assess model accuracy
6. **Model Saving** – Saved the trained model and encoders using Pickle for reuse
7. **Prediction Interface** – Built a Flask web app for real-time salary prediction based on user input

## 🖥️ Running the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/TechGauri-09/Employee-Salary-Prediction.git
   cd Employee-Salary-Prediction
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:
   ```bash
   python interface.py
   ```

4. Open your browser at `http://127.0.0.1:5000`

## 📈 Results

The model achieves strong predictive performance, with predicted salaries closely matching actual salaries across the dataset range (visualized in `actual_vs_predicted.png`).

## 🔮 Future Improvements

- Expand dataset size for better generalization
- Add more features (location, company size, etc.)
- Deploy the app on a cloud platform

## 👤 Author

**Gauri Thakare**
- GitHub: [TechGauri-09](https://github.com/TechGauri-09)
- LinkedIn: [gauri-thakare](https://linkedin.com/in/gauri-thakare-aba165320)
