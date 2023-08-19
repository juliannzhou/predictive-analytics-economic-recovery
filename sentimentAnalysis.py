import requests


def getSentiment(arr):
  print("Start of sentiment processing")

  for sentence in arr:
    endpoint = 'https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/64fe256b-5059-4fe4-b738-5ef6a6c6e114/v1/analyze'
    username = 'apikey'
    password = '1tIpm_GEJKcb0mbVr9fkiL4V1EYNpUEIAdI-MDuglQ38'
    parametersIBM = {
      'features': 'emotion,sentiment',
      'version': '2018-11-16',
      'text': sentence,
      'language': 'en',
    }
    resp = requests.get(endpoint,
                        params=parametersIBM,
                        auth=(username, password))
    data = resp.json()
    senti = data['sentiment']['document']['score']
    print('Sentiment score:', senti)


sentence1 = "I hate this thing so much, it really makes me mad."
sentence2 = "This is amamzing, and I would recommend it to everyone."
sentence3 = "The sky is blue, the sun is shining, and the clouds are white and fluffy."
arr = [sentence1, sentence2, sentence3]
getSentiment(arr)
"""
Discontinued due to change in Twitter API policy
"""
