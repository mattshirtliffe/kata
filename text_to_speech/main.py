#http://sahandsaba.com/thirty-python-language-features-and-tricks-you-may-not-know.html
import requests

def create_mp3():
    url= 'http://tts-api.com/tts.mp3?q="You are a cunt"'
    r = requests.get(url, stream=True)
    with open('cunt.mp3', 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()



if __name__ == "__main__":
    create_mp3()
