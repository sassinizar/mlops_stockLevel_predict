import pandas as pd
import argparse
import os

def preprocess(input_path, output_path):
    df = pd.read_csv(input_path)

    # Basic preprocessing (example)
    df = df.dropna()
    df['date'] = pd.to_datetime(df['date'])
    df.sort_values('date', inplace=True)
    
    # Feature engineering: 7-day rolling average
    df['rolling_avg'] = df['stock_level'].rolling(window=7, min_periods=1).mean()

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Preprocessed data written to: {output_path} | Shape: {df.shape}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', type=str, required=True)
    parser.add_argument('--output_path', type=str, required=True)
    args = parser.parse_args()

    preprocess(args.input_path, args.output_path)

if __name__ == '__main__':
    main()
