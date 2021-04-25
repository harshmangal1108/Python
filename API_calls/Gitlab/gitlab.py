import requests

res = requests.get(
    'https://gitlab.example.com/api/v4/projects/users/harsh.mangal1108/projects')

print(res)