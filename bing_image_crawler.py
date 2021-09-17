from bing_image_downloader import downloader

def image_download(token:str,img_count:int = 200,path:str = "dataset"):
    query_string = token
    limit = img_count
    out_dir = path
    downloader.download(token, limit=limit,  output_dir=out_dir,
                        adult_filter_off=True, force_replace=False,
                        timeout=60)
screen = '''
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
| 1. Make a list of names of images/class labels to be downloaded |
|    in a txt file.                                               |
| 2. Place the txt file in the same path.                         |
| 3. Enter image count of each class label                                                |
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


'''
print(screen)
file_name = input("Enter txt file name: ")
img_count = int(input("Enter image count: "))
file = open("{}".format(file_name),"r")
content = file.read()
content_list = content.split("\n")
file.close()
for token in content_list:
    image_download(token,img_count)



