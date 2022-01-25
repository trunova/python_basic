import re
import requests

if __name__ == "__main__":
    my_req = requests.get('http://www.columbia.edu/~fdc/sample.html')
    text = my_req.text
    result = re.findall(r'<h3 .*>.*</h3>', text)
    subtitles_list = [h[h.find('>') + 1: h.find('<', h.find('>') + 1)] for h in result]
    print(subtitles_list)
