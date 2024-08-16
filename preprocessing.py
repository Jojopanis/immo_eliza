import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
import joblib

df = pd.read_json('final_dataset.json')

df.drop(df[['Url', 'Country', 'FloodingZone', 'Locality', 'MonthlyCharges', 'PostalCode', 'PropertyId','RoomCount']], axis=1, inplace=True)

def remove_outliers(df:pd.DataFrame, columns:list, factor=1.5):
    for col in columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - factor * IQR
        upper_bound = Q3 + factor * IQR
        df[col] = df[col].clip(lower_bound, upper_bound)
    return df

def remove_irrelevant(df:pd.DataFrame):
    df = df[df['TypeOfSale'].isin(['residential_sale', 'residential_monthly_rent'])]

target = df['Price']
int_features = ['BedroomCount', 'BathroomCount', 'ConstructionYear', 'NumberOfFacades', 'ShowerCount', 'ToiletCount']
float_features = ['GardenArea', 'LivingArea', 'SurfaceOfPlot']

categorical_features = ['District', 'Fireplace', 'Furnished', 'Garden', 'Kitchen', 'PEB', 'Province', 'Region', 'StateOfBuilding', 'SubtypeOfProperty', 'SwimmingPool', 'Terrace', 'TypeOfProperty', 'TypeOfSale']

features_to_keep = int_features + float_features + categorical_features

preprocessor = ColumnTransformer(
    transformers=[
        ("int", SimpleImputer(strategy="most_frequent"), int_features),
        ("float", SimpleImputer(strategy="mean"), float_features),
        ("cat", OneHotEncoder(handle_unknown='ignore', sparse_output=False), categorical_features)
    ],
    remainder="passthrough"
)

X = preprocessor.fit_transform(df[features_to_keep])

feature_names = preprocessor.get_feature_names_out()

df_preprocessed = pd.DataFrame(X, columns=feature_names)

joblib.dump(preprocessor, "preprocessor_compressed.pkl", compress=3)