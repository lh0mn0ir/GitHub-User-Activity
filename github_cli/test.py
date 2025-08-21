import requests

name  = input("Entrez votre nom d'utilisateur GitHub: ")
url = f"https://api.github.com/users/{name}"

response = requests.get(url)# récupérer l'url 
print(response.status_code)# afficher le code de statut de la réponse

data = response.json()# récupérer les données de l'utilisateur en JSON
print(data)

print(data['login'])
print(data['bio'])
print(data['public_repos'])

# -----------------------------------------------------------
# Les endpoints de l'API GitHub
#
# 1. Obtenir les informations d'un utilisateur
#    - GET https://api.github.com/users/{username}
#
# 2. Obtenir les dépôts d'un utilisateur
#    - GET https://api.github.com/users/{username}/repos
#
# 3. Obtenir les informations d'un dépôt
#    - GET https://api.github.com/repos/{owner}/{repo}
#
# 4. Obtenir les commits d'un dépôt
#    - GET https://api.github.com/repos/{owner}/{repo}/commits