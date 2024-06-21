import gdown

# Google Drive URL and output file path
url = 'https://drive.google.com/file/d/1BhCW8ms4qfbSYi3sdzsvJDNZNknQKX0U/view?usp=drive_link'
output = 'resnest50-528c19ca.pth'

# Download the file
gdown.download(url, output, quiet=False)
