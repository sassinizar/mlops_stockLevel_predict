import pandas as pd
import xgboost as xgb
import joblib
import argparse
import os

def train_model(input_path, model_output_path):
    df = pd.read_csv(input_path)
    
    # Assume 'stock_level' is the target
    X = df.drop(columns=['stock_level', 'date'])  # remove non-feature cols
    y = df['stock_level']
    
    model = xgb.XGBRegressor(n_estimators=100, max_depth=5, learning_rate=0.1)
    model.fit(X, y)

    os.makedirs(os.path.dirname(model_output_path), exist_ok=True)
    joblib.dump(model, model_output_path)
    print(f"Model saved to {model_output_path}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', type=str, required=True)
    parser.add_argument('--model_output_path', type=str, required=True)
    args = parser.parse_args()

    train_model(args.input_path, args.model_output_path)

if __name__ == '__main__':
    main()
