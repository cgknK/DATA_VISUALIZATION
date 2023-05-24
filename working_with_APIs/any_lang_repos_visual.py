import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response.
prog_lang = 'c'
url = f'https://api.github.com/search/repositories?q=language:{prog_lang}&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable.
response_dict = r.json()
print(type(response_dict))
repo_dicts = response_dict['items']
print(type(repo_dicts))

# Process results.
repo_names, stars, labels = [], [], []
repo_links = []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    # <br /> yerine neden \n kullanmak aynı sonucu vermiyor?
    #label = f"\n{owner}\n\n{description}"
    labels.append(label)

    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_names[-1]}</a>"
    repo_links.append(repo_link)

# Make visualization.
data = [{
    'type': 'bar',
    #'x': repo_names,
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'
        },
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': f'Most-Starred {prog_lang} Projects on Github',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename=f'{prog_lang}.html')

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
"""