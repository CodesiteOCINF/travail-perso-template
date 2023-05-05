class DocumentInfos:

    title = u'Fonctionnement des Routeurs'
    first_name = 'Pierre'
    last_name = 'Dey'
    author = f'{Dey} {Pierre}'
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