

from django.shortcuts import render
import requests

from projectapp.models import Repositories, Language


def search(request):
    query = []
    languages = list(map(lambda x: x[0], Language.objects.all().values_list('repo_language')))

    for language in languages:
        query.append(Repositories.objects.filter(repository_language__repo_language=language))

    return render(request, 'search.html',
                  {'repositories': dict(zip(list(map(lambda x: x + '_repositories', languages)), query)),
                   'languages': languages})


def __get_final_data(repositories):
    final_data = {'total_count': 0, 'items': []}

    for repo in repositories:
        for repository in Repositories.objects.filter(repo_address=repo):

            labels_url = '+'.join(['label:"{}"'.format(x) for x in repository.repository_label.all() if x])
            if labels_url:
                labels_url = '+' + labels_url

            for language in repository.repository_language.all():
                url = 'http://projectapp.github.com/search/issues?q=language:{language}+no:assignee+repo:{repo}' \
                      '{labels_url}&page={index}&per_page=20'.format(language=language, labels_url=labels_url,
                                                                     repo=repo, index=1)
                try:
                    res = requests.get(url)
                    res = res.json()

                    if res['items']:
                        final_data['items'].append(repository.repo_address)

                        final_data['items'].extend(res['items'])
                except AttributeError:
                    pass

    return final_data


def result(request):
    lang = request.GET['l']
    if request.GET.getlist('repo'):
        final_data = __get_final_data(request.GET.getlist('repo'))

    else:
        repositories = Repositories.objects.filter(repository_language__repo_language=lang)
        final_data = __get_final_data(repositories)

    if final_data['items']:
        return render(request, 'result.html', {'items': final_data['items'], 'message': 'You have some results'})

    return render(request, 'result.html', {'message': 'There is no match'})





