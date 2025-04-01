# import os
# import boto3
# from botocore.exceptions import NoCredentialsError

# class DataSync:
#     def __init__(self, local_directory, s3_bucket, s3_directory):
#         self.local_directory = local_directory
#         self.s3_bucket = s3_bucket
#         self.s3_directory = s3_directory
#         self.s3_client = boto3.client('s3')

#     def upload_files(self):
#         for root, dirs, files in os.walk(self.local_directory):
#             for file in files:
#                 local_file_path = os.path.join(root, file)
#                 relative_path = os.path.relpath(local_file_path, self.local_directory)
#                 s3_file_path = os.path.join(self.s3_directory, relative_path)

#                 try:
#                     self.s3_client.upload_file(local_file_path, self.s3_bucket, s3_file_path)
#                     print(f'Uploaded {local_file_path} to s3://{self.s3_bucket}/{s3_file_path}')
#                 except FileNotFoundError:
#                     print(f'The file {local_file_path} was not found')
#                 except NoCredentialsError:
#                     print('Credentials not available')

#     def download_files(self):
#         paginator = self.s3_client.get_paginator('list_objects_v2')
#         for page in paginator.paginate(Bucket=self.s3_bucket, Prefix=self.s3_directory):
#             if 'Contents' in page:
#                 for obj in page['Contents']:
#                     s3_file_path = obj['Key']
#                     if s3_file_path.endswith('/'):
#                         continue  # Skip directories
#                     local_file_path = os.path.join(self.local_directory, os.path.relpath(s3_file_path, self.s3_directory))

#                     os.makedirs(os.path.dirname(local_file_path), exist_ok=True)

#                     try:
#                         self.s3_client.download_file(self.s3_bucket, s3_file_path, local_file_path)
#                         print(f'Downloaded s3://{self.s3_bucket}/{s3_file_path} to {local_file_path}')
#                     except NoCredentialsError:
#                         print('Credentials not available')

# if __name__ == "__main__":
#     local_dir = 'data/'  # Local directory to sync
#     s3_bucket_name = 'your-s3-bucket-name'  # Replace with your S3 bucket name
#     s3_dir = 'data/'  # S3 directory to sync

#     data_sync = DataSync(local_dir, s3_bucket_name, s3_dir)
#     data_sync.upload_files()
#     data_sync.download_files()