import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    
    def upload_files(self, file_from, file_to):
        for root, dirs, files in os.walk(file_from):
            relative_path = os.path.relpath(local_path, file_from)
            dropbox_path = os.path.join(file_to, relative_path)

        with open(local_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))








def main():
    access_token = "sl.A52VOUc_dLV2J8w34u3lWudjF3lUrv22eznhdAJRz5ogOLxH_UuSS47rHXrVy4ppRPnlScM_c_oTdvZdnyoURI9NY2O1FGDQJqf0H9ZIPcU_j61ZVHhiaFWh4xnTz306-P8b7WY"
    transferData = TransferData(access_token)

    fileSource = input("Enter the file path to transfer:- ")
    fileDestination = input("Enter the full path to upload to dropbox:- ")
    transferData.upload_files(fileDestination, fileSource)
    print("File has been successfully uploaded.")
