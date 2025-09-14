#  SpaceX Falcon 9 Landing Predictor

> **Will it stick the landing?** Machine learning model that predicts SpaceX Falcon 9 first stage landing success with **83.3% accuracy**.

<div align="center">

![SpaceX](https://img.shields.io/badge/SpaceX-Falcon%209-black?style=for-the-badge&logo=spacex)
![Python](https://img.shields.io/badge/Python-ML-blue?style=for-the-badge&logo=python)
![Accuracy](https://img.shields.io/badge/Accuracy-83.3%25-brightgreen?style=for-the-badge)

</div>

## 🎯 What It Does

Predicts whether SpaceX rockets will successfully land using **90 historical launches** and **6 ML algorithms**. Perfect for understanding what makes rockets stick the landing!

## ⚡ Quick Results

| Feature | Impact | Why It Matters |
|---------|---------|----------------|
|  **GridFins + Legs** | Critical | Both needed for controlled landing |
|  **Block 5** | +40% success | Latest tech = better landings |
|  **Heavy Payload** | -20% success | Physics: harder to slow down |

##  Model Performance

```
 Logistic Regression: 83.3% 
 SVM: 80.0%
 KNN: 75.0%
 Decision Tree: 78.0%
```

##  Try It Yourself

```python
# Clone and predict
git clone https://github.com/yourusername/spacex-predictor
pip install -r requirements.txt
python spacex_analysis.py

# Example prediction
predict_landing(payload=5000, grid_fins=True, legs=True, block=5)
# → "SUCCESS (87% confidence)"
```

##  Tech Stack

**Python** • **Scikit-learn** • **Pandas** • **Jupyter** • **Seaborn** • **Matplotlib**

##  Features Used

- **PayloadMass**: Rocket cargo weight
- **GridFins**: Steering fins for landing
- **Legs**: Landing legs deployment  
- **Block**: Falcon 9 version (1-5)
- **Flights**: Booster experience
- **ReusedCount**: Previous flights

##  Key Insight

> **Block 5 + GridFins + Legs = 95% landing success rate** 🎯

##  ML Algorithms Tested

-  **Logistic Regression** 
-  **Random Forest**  
-  **Gradient Boosting**
-  **Support Vector Machine**
-  **K-Nearest Neighbors**
-  **Decision Tree**


##  Author

Built by **Swaraj Khair** - 

---

 **Star this repo if you love rockets!** 

*"Failure is an option here. If things are not failing, you are not innovating enough." - Elon Musk*