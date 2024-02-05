from CaesarAIGCPStreamUpload import CaesarAIGCPStreamUpload
if __name__ == "__main__":
    #client = storage.Client()

    with CaesarAIGCPStreamUpload(bucket_name="caesaraiyoutube-bucket", blob_name='test-blob2') as s:
        for _ in range(1024):
            s.write(b'x' * 1024)