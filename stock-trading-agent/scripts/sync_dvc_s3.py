# import os
# import subprocess

# def sync_dvc_with_s3():
#     # Define the command to sync DVC with S3
#     command = ["dvc", "push"]

#     try:
#         # Execute the command
#         subprocess.run(command, check=True)
#         print("Successfully synchronized DVC data with S3.")
#     except subprocess.CalledProcessError as e:
#         print(f"Error during synchronization: {e}")

# if __name__ == "__main__":
#     sync_dvc_with_s3()