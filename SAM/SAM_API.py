import requests, json
key = str(input()) #needs to be input
DUNS = str(input()) #needs to be input
url_first = 'https://api.data.gov/sam/v1/registrations/'
url_last = '?api_key='
url = url_first + DUNS + url_last + key

r = requests.get(url)

test = r.json()

for i in test:
    for j in test[i]:
        print(test[i][j]['hasKnownExclusion'])
        print(test[i][j]['electronicBusinessPoc']['lastName'])
        print(test[i][j]['electronicBusinessPoc']['firstName'])
        print(test[i][j]['electronicBusinessPoc']['usPhone'])
        print(test[i][j]['electronicBusinessPoc']['email'])
