import dropbox

class Transfer_data:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BFbiem4lJeopuf1WamWGP0sU_3uG29hcPLhoBZg_PXUnjFF6OpjTuNxio3HDdZeIthcP_evo4vLcC3W_0qFUfxquSE53C-4hlXrMnpPZnmcOfNzXeGjH7AHbEZsJcM90rrfejzaU'
    transfer_data = Transfer_data(access_token)
    file_from = input("Enter the path to transfer: ")
    file_to = input("Enter the full path to upload to dropbox: ")
    transfer_data.upload_file(file_from, file_to)
    print("The folder has been uploaded")

main()


