from minio import Minio
import pandas as pd
import os
import argparse

def download_from_minio(bucket, object_name, file_path, endpoint, access_key, secret_key):
    client = Minio(endpoint, access_key=access_key, secret_key=secret_key, secure=False)
    client.fget_object(bucket, object_name, file_path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bucket', type=str, required=True)
    parser.add_argument('--object_name', type=str, required=True)
    parser.add_argument('--output_path', type=str, default='/app/data/raw.csv')
    parser.add_argument('--endpoint', type=str, default='minio:9000')
    parser.add_argument('--access_key', type=str, default='minioadmin')
    parser.add_argument('--secret_key', type=str, default='minioadmin')
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.output_path), exist_ok=True)
    download_from_minio(args.bucket, args.object_name, args.output_path, args.endpoint, args.access_key, args.secret_key)

    df = pd.read_csv(args.output_path)
    print(f"Downloaded {args.object_name} with shape: {df.shape}")

if __name__ == '__main__':
    main()
