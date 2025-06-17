import logging
logging.basicConfig(
    filename='logs/upload.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

try:
    import argparse
    import os
    import shutil
    import boto3
    from botocore.exceptions import BotoCoreError, ClientError
    
    def parse_s3_path(path):
        if not path.startswith('s3://'):
            raise ValueError(f"Invalid S3 path: {path}")
        parts = path[5:].split('/', 1)
        bucket = parts[0]
        prefix = parts[1] if len(parts) > 1 else ''
        return bucket, prefix
    
    def upload_to_s3(source, bucket, prefix):
        s3 = boto3.client('s3')
        for root, dirs, files in os.walk(source):
            for file in files:
                local_path = os.path.join(root, file)
                relative_path = os.path.relpath(local_path, source)
                s3_key = os.path.join(prefix, relative_path)
                s3.upload_file(local_path, bucket, s3_key)
    
    def upload_to_local(source, dest):
        os.makedirs(dest, exist_ok=True)
        for root, dirs, files in os.walk(source):
            for file in files:
                local_path = os.path.join(root, file)
                relative_path = os.path.relpath(local_path, source)
                dest_path = os.path.join(dest, relative_path)
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                shutil.copy(local_path, dest_path)
    
    def main():
        parser = argparse.ArgumentParser()
        parser.add_argument('--source', required=True)
        parser.add_argument('--dest', required=True)
        args = parser.parse_args()
        if args.dest.startswith('s3://'):
            bucket, prefix = parse_s3_path(args.dest)
            upload_to_s3(args.source, bucket, prefix)
        else:
            upload_to_local(args.source, args.dest)
    logging.info("Загрузка результатов успешно выполнено.")
except Exception as e:
    logging.error("Загрузка результатов не выполнено: %s", e)
    raise
