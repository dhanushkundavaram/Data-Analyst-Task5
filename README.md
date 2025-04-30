# Data-Analyst-Task5
#  Titanic Dataset - Exploratory Data Analysis (EDA)


##  Dataset
The dataset used is the [Titanic Dataset from Kaggle](https://www.kaggle.com/c/titanic/data).  
File used: `train.csv`

---
### 1. Dataset Overview
- Shape: 891 rows × 12 columns.
- No duplicate rows found.

### 2. Value Counts
- **Sex**: More males (~65%) than females.
- **Pclass**: Most passengers in 3rd class.
- **Embarked**: Majority from Southampton (S).


### 3. Pairplot Insights
- Survivors: Lower Pclass, Higher Fare, Slightly younger.

### 4. Survival by Sex
- Females had much higher survival rate.

### 5. Survival by Class
- 1st class > highest survival  
- 3rd class > lowest survival

### 6. Age Distribution
- Most passengers aged 20–40  
- Right-skewed

### 7. Fare Distribution
- Skewed right, most fares < $100  
- Some outliers (high fare)

### 8. Age vs Survival (Boxplot)
- Survivors generally younger  
- Wide age range in non-survivors

### 9. Fare vs Survival (Boxplot)
- Survivors paid higher fares

### 10. Age vs Fare (Scatterplot)
- High-fare, young passengers survived more  
- Dense non-survivor cluster: low-fare, mid-age

---

## 📤 Deliverables
- `Titanic_EDA.py`
- `README.md` 
