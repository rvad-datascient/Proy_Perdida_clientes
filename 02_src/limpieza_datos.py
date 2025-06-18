  
import pandas as pd  

def limpiar_datos(df):  
    df = df.copy()  
    df.drop(columns=['RowNumber', 'CustomerId', 'Surname'], inplace=True)  
    df.drop_duplicates(inplace=True)  
    df.dropna(subset=['Geography'], inplace=True)  

    df['Age'] = df['Age'].fillna(df['Age'].mean())  
    df['HasCrCard'] = df['HasCrCard'].fillna(df['HasCrCard'].mode()[0])  
    df['IsActiveMember'] = df['IsActiveMember'].fillna(df['IsActiveMember'].mode()[0])  

    df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})  
    df = pd.get_dummies(df, columns=['Geography'], drop_first=True)  

    bool_cols = df.select_dtypes(include='bool').columns  
    df[bool_cols] = df[bool_cols].astype(int)  

    return df  
