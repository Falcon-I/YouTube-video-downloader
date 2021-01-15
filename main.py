import pytube as p
from tqdm.auto import tqdm
try:
    url = p.YouTube(input('Enter the url of the video : '))
    video = url.streams.get_by_itag(22)
    print("Starting Download.....");video.download()
    for i in tqdm(range(int(9e6))):
        pass;
    print("Your video is Successfully Downloaded")
except:
    print("Unable to Download your video😥")
