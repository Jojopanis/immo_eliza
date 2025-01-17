from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error as mae
from sklearn.ensemble import RandomForestRegressor as RFR
import joblib

from preprocessing import df_preprocessed as df, target

y = target
X = df
print(X.head())
X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=42, test_size=0.2)

regressor = RFR(n_jobs=-1)
regressor.fit(X_train, y_train)
score = regressor.score(X_test, y_test)
mean_absolute_error = mae(y_test, regressor.predict(X_test))

joblib.dump(regressor, 'model.pkl', compress=3)

print(f'The model scored {score} with a mae of {mean_absolute_error}')