## Search Engine

Simple search engine using elasticsearch and django framework.
Data is stored in indexes in elasticsearch server.


### Prerequisites

Django version : 2.0.3
elasticsearch : 7.3.2


### Overview of interaction with elasticsearch index using python


#### Needed imports 
```
from elasticsearch_dsl import Document, Text
from elasticsearch_dsl.connections import connections
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
```

#### Define a default Elasticsearch client
```
connections.create_connection(hosts=['localhost'])
client = Elasticsearch()
```

#### Define a class that contains the same attributs as the index in the elasticsearch server
 Exemple
```
class Candidat(Document):
    email = Text()
    url = Text()
    name = Text()
    phone = Text()
    listeSkills = Text()
    raw = Text()

    # Define the name of the index in server
    class Index:
        name = 'base_candidat'

    def save(self, **kwargs):
        return super(Candidat, self).save(**kwargs)

```
#### Function For saving 
```
def saveCandidate(context):
    Candidat.init()
    candidat = Candidat(email = context['email'] , url = context['url'] , name = context['name'] ,phone = context['phone'] , raw = context['raw'] )
    candidat.save()
```
#### Function for searching
```
def retrieveCandidate(str):
    s = Search(using=client)
    s = Search().using(client).index('base_candidat').query("match", raw=str)
    s.execute()
    for hit in s:
        print(hit)
    return(s)

```

### Run Project

* set environement for python
* Run elasticsearch server 
* Populate index with appropriate data
* navigate to $Your_Path/project and run python manage.py runserver

