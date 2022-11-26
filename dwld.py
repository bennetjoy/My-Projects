from download import download

url = input("Enter link of file to download: ")
file_path="D:\\trials"
filet = ["file","zip","tar","tar.gz"]
for i in range(0,len(filet)):
    print(i,".",filet[i])
k = int(input("Select file type:"))
ft = filet[k]
#path = download(url, file_path, kind="zip")
#path = download(url, file_path, progressbar=True)
path = download(url, file_path, replace=True)
#path = download(url, file_path, timeout=10)
#path = download(url, file_path, verbose=True)