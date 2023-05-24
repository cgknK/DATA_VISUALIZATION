# Bazı diller için hatalar var
# test_ yazmak için kodun tekrar düzeltilmesi gerekiyor
from time import sleep

import requests

from plotly.graph_objs import Bar
from plotly import offline

def get_input_to_formatted(user_input):
    raw_prog_langs = user_input.split(',')
    prog_langs = [ v.strip().lower() for v in raw_prog_langs]
    while '' in prog_langs:
        prog_langs.remove('')
    return prog_langs

def get_url(prog_lang):
    url = f'https://api.github.com/search/repositories?q=language:{prog_lang}&sort=stars'
    #headers = {'Accept': 'application/vnd.github.v3+json'}
    return url

def get_request_response(url):
    #r_list.append(requests.get(url, headers=headers))
    r = requests.get(url)

    # Store API response in a variable.
    response_dict = r.json()
    repo_dicts = response_dict['items']

    if r.status_code == 200:
        pass
    else:
        pass

    return repo_dicts

def get_project_data(repo_dicts):
    """Return data needed for each project in visualization."""
    repo_links, stars, labels = [], [], []
    for repo_dict in repo_dicts:
        repo_name = repo_dict['name']
        repo_url = repo_dict['html_url']
        repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
        repo_links.append(repo_link)

        stars.append(repo_dict['stargazers_count'])

        owner = repo_dict['owner']['login']
        description = repo_dict['description']
        label = f"{owner}<br />{description}"
        # <br /> yerine neden \n kullanmak aynı sonucu vermiyor?
        #label = f"\n{owner}\n\n{description}"
        labels.append(label)
    
    return repo_links, stars, labels

def make_visualization(repo_links, stars, labels, prog_lang):
    # Make visualization.
    data = [{
        'type': 'bar',
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
    offline.plot(fig, filename=f'abc_{prog_lang}.html')

if __name__ == '__main__':
    #raw_inputs = input("You can use ',' for sep. langs: ")
    test_inputs = "JavaScript, RubY,C,Java,, , Go, c++, pythoN "
    prog_langs = get_input_to_formatted(test_inputs)
    for prog_lang in prog_langs:
        url = get_urls(prog_lang)
        repo_dicts = get_requests_responses(url)
        repo_links, stars, labels = get_project_data(repo_dicts)
        make_visualization(repo_links, stars, labels, prog_lang)