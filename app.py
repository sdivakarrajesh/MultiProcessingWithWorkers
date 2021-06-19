from tasks import add, download
from tqdm import tqdm
urls = [
    "https://www.youtube.com/watch?v=bUN5uSu_VQM",
    "https://www.youtube.com/watch?v=67oe0_s9EIw",
    "https://www.youtube.com/watch?v=MZoO8QVMxkk",
    "https://www.youtube.com/watch?v=tXW1bOnPHdE",
]
for url in tqdm(urls):
    download.delay(url)
