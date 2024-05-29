import json
from rdflib import Graph, Literal, Namespace, RDF, RDFS, OWL
from rdflib.namespace import XSD

# Definirea spațiilor de nume pentru ontologie și RDF
film = Namespace("http://example.com/film-ontology#")
ex = Namespace("http://example.com/example#")

# Funcție pentru a crea o instanță de film în ontologie
def create_movie_instance(graph, movie_data):
    movie_id = ex[movie_data['id']]
    graph.add((movie_id, RDF.type, film.Film))
    graph.add((movie_id, film.hasTitle, Literal(movie_data['titlu'])))
    graph.add((movie_id, film.hasReleaseYear, Literal(movie_data['anul de lansare'], datatype=XSD.integer)))
    graph.add((movie_id, film.hasRating, Literal(movie_data['rating'], datatype=XSD.float)))
    graph.add((movie_id, film.hasDuration, Literal(movie_data['durata'], datatype=XSD.integer)))
    graph.add((movie_id, film.hasType, Literal(movie_data['tip'])))

    # Adăugarea regizorilor
    directors = movie_data['regizori'].split(', ')
    for director in directors:
        director_uri = ex[director.lower().replace(' ', '_')]
        graph.add((director_uri, RDF.type, film.Director))
        graph.add((movie_id, film.hasDirector, director_uri))
        graph.add((director_uri, film.hasName, Literal(director)))

    # Adăugarea actorilor
    actors = movie_data['actori'].split(', ')
    for actor in actors:
        actor_uri = ex[actor.lower().replace(' ', '_')]
        graph.add((actor_uri, RDF.type, film.Actor))
        graph.add((movie_id, film.hasActor, actor_uri))
        graph.add((actor_uri, film.hasName, Literal(actor)))

# Citirea datelor din fișierul JSON
with open('date.json', 'r') as json_file:
    data = json.load(json_file)

# Inițializarea unui graf RDF
g = Graph()

# Iterarea prin fiecare film și adăugarea în ontologie
for movie_data in data:
    create_movie_instance(g, movie_data)

# Scrierea grafului RDF într-un fișier
g.serialize(destination='film_ontology.rdf', format='xml')
