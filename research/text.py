import json
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

df = pd.read_csv('./research/data.csv', index_col=0)
x_cols = df.drop(columns=['age'])
