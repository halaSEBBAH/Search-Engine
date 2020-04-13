# #    writen by : Hala Sebbah
# #    Email : sebbah.hala@gmail.com


from elasticsearch_dsl import Document, Date, Integer, Keyword, Text
from elasticsearch_dsl.connections import connections
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search


# Define a default Elasticsearch client
connections.create_connection(hosts=['localhost'])
client = Elasticsearch()


class Candidat(Document):
    email = Text()
    url = Text()
    name = Text()
    phone = Text()
    listeSkills = Text()
    raw = Text()

    class Index:
        name = 'base_candidat'

    def save(self, **kwargs):
        return super(Candidat, self).save(**kwargs)


def saveCandidate(context):
    Candidat.init()
    candidat = Candidat(email = context['email'] , url = context['url'] , name = context['name'] ,phone = context['phone'] , raw = context['raw'] )
    candidat.save()


def retrieveCandidate(str):
    s = Search(using=client)
    s = Search().using(client).index('base_candidat').query("match", raw=str)
    s.execute()
    for hit in s:
        print(hit)
    return(s)