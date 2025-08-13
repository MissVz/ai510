import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from sklearn.ensemble import RandomForestRegressor  # Add this import
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.neighbors import KNeighborsRegressor

url = "housing.csv"
df = pd.read_csv(url)
df = df.drop(['id', 'date'], axis=1)

sns.histplot(df['price'], bins=50, kde=True)
plt.title('Distribution of Housing Prices')
plt.show()

plt.figure(figsize=(14, 10))
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix', size=20)
plt.show()

corr_matrix = df.corr()
high_corr_features = corr_matrix.index[abs(corr_matrix['price']) > 0.5]
df_reduced = df[high_corr_features]

linear_model = LinearRegression()
random_forest_model = RandomForestRegressor(n_estimators=100, random_state=42)
knn_model = KNeighborsRegressor(n_neighbors=5)

X = df_reduced.drop('price', axis=1)
y = df_reduced['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

linear_model.fit(X_train, y_train)
random_forest_model.fit(X_train, y_train)
knn_model.fit(X_train, y_train)

linear_preds = linear_model.predict(X_test)
rf_preds = random_forest_model.predict(X_test)
knn_preds = knn_model.predict(X_test)

linear_rmse = np.sqrt(mean_squared_error(y_test, linear_preds))
linear_r2 = r2_score(y_test, linear_preds)

rf_rmse = np.sqrt(mean_squared_error(y_test, rf_preds))
rf_r2 = r2_score(y_test, rf_preds)

knn_rmse = np.sqrt(mean_squared_error(y_test, knn_preds))
knn_r2 = r2_score(y_test, knn_preds)

print(f'Linear Regression RMSE: {linear_rmse}, R^2: {linear_r2}')
print(f'Random Forest RMSE: {rf_rmse}, R^2: {rf_r2}')
print(f'KNN RMSE: {knn_rmse}, R^2: {knn_r2}')

plt.figure(figsize=(21, 7))

plt.subplot(1, 3, 1)
plt.scatter(y_test, linear_preds, alpha=0.3)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Linear Regression Predictions')

plt.subplot(1, 3, 2)
plt.scatter(y_test, rf_preds, alpha=0.3)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Random Forest Predictions')

plt.subplot(1, 3, 3)
plt.scatter(y_test, knn_preds, alpha=0.3)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('KNN Predictions')

plt.tight_layout()
plt.show()