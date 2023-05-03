class DocumentInfos:

    title = u'Fonctionnement des Routeurs (modifier dans `source/infos.py`)'
    first_name = 'Pierre (infos.py)'
    last_name = 'Dey (infos.py)'
    author = f'{first_name} {last_name}'
    year = u'2023'
    month = u'Avril'
    seminary_title = u'Travail personnel OCI'
    tutor = u"Cédric Donner"
    release = "(Version finale)"
    repository_url = "https://github.com/<username>/<reponame>"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

infos = DocumentInfos()