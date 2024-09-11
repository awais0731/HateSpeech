import os
import shutil


class GCloudSync:

    def sync_folder_to_gcloud(self, gcp_bucket_url, filepath, filename):

        command = f"gsutil cp {filepath}/{filename} gs://{gcp_bucket_url}/"
        # command = f"gcloud storage cp {filepath}/{filename} gs://{gcp_bucket_url}/"
        os.system(command)

    # def sync_folder_from_gcloud(self, gcp_bucket_url, filename, destination):

    #     command = f"gsutil cp gs://{gcp_bucket_url}/{filename} {destination}/{filename}"
    #     # command = f"gcloud storage cp gs://{gcp_bucket_url}/{filename} {destination}/{filename}"
    #     os.system(command)

    def sync_folder_from_gcloud(self, source, destination):

        try:
        # Copy the file from source to destination
            shutil.copy2(source, destination)
            print(f"File copied successfully from {source} to {destination}")
        except Exception as e:
            print(f"Error copying file: {e}")