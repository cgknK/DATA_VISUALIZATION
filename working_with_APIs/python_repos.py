import requests

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
#r = requests.get(url, headers)
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
# Store API response in a variable.
# API'ın json formatında bir cevap vereceğini nerden biliyoruz?
response_dict = r.json()
print(type(response_dict))
print(f"Total repositories: {response_dict['total_count']}")

# Process results.
print(response_dict.keys())
""" items yada values neden UnicodeEncodeError veriyor
print(response_dict['items']) --> bu da 
print(response_dict.items())"""
print(response_dict['incomplete_results'])

# Explore information about the repositories.
repo_dicts = response_dict['items']
print("repo_dicts type: ", type(repo_dicts))
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository.
#repo_dict = repo_dicts[0]
#print("repo_dict type: ", type(repo_dict))
#print(f"\nKeys: {len(repo_dict)}")
"""
for key in sorted(repo_dict.keys()):
    print(key)
"""

# 249k star alan repo görmeme rağmen burada daha az star'lı ve sürekli farklı
#repolar çıkıyor. Bunları kayıt altına name + i++ alıp incele. Değişimin nedeni?
rows_json = ["\nSelected information about each repository:"]
print(rows_json[0])
for repo_dict in repo_dicts:
    name = f"Name: {repo_dict['name']}"
    print(name)
    owner_login = f"Owner: {repo_dict['owner']['login']}"
    print(owner_login)
    stargazers_count = f"Stars: {repo_dict['stargazers_count']}"
    print(stargazers_count)
    html_url = f"Repository: {repo_dict['html_url']}"
    print(html_url)
    created_at = f"Created: {repo_dict['created_at']}"
    print(created_at)
    updated_at = f"Updated: {repo_dict['updated_at']}\n"
    print(updated_at)
    #encode sorunu var bende, çözüm ara
    #print(f"Description: {repo_dict['description']}")