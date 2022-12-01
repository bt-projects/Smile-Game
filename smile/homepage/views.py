from django.shortcuts import render
from urllib.request import urlopen
import json

def home(request):
    # store the URL in url as parameter for urlopen
    # url = "https://marcconrad.com/uob/smile/api.php"
    
    # store the response of URL
    # response = urlopen(url)
    
    # storing the JSON response from url in data
    # smileJson = json.loads(response.read())

    ##############################################################
    # context = {
    #     'smileUrl': 'https://marcconrad.com/uob/smile/api.php',
    #      'githubAPI': 'https://api.github.com/',
    # }

    # my_context = data_json
    ##############################################################

    return render(request, 'homepage/index.html')
    # return render(request, 'homepage/index.html', {'smileJson' : smileJson})
    # return print(data_json)
