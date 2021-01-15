import pytube as p
from tqdm.auto import tqdm
try:
    url = p.YouTube(input('Enter the url of the video : '))
    video = url.streams.get_by_itag(22)
    vpath = input("Enter the path to store the video : ")
    print("Starting Download.....");video.download(vpath)
    for i in tqdm(range(int(9e6))):
        pass;
    print("Your video is Successfully Downloaded")
except:
    print("Unable to Download your video😥")
