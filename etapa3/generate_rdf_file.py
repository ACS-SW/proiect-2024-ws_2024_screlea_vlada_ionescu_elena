import json
import unicodedata
from rdflib import Graph, Literal, Namespace, RDF, XSD

# Define namespaces for the ontology and RDF
filme_ns = Namespace("http://www.semanticweb.org/ontologies/2024/filme#")
ex_ns = Namespace("http://example.com/example#")

# Function to clean and transform names into valid URI formats
def clean_name(name):
    # Remove diacritics
    name = ''.join(c for c in unicodedata.normalize('NFD', name) if unicodedata.category(c) != 'Mn')
    # Transform to lowercase and replace spaces and hyphens with underscores
    return name.lower().replace(' ', '').replace('-', '').replace('"', '').replace("'", '')

# Read movie data from JSON file "filme.json"
with open('filme.json', 'r') as json_file:
    filme_data = json.load(json_file)

# Read actor data from JSON file "actori.json"
with open('actori.json', 'r') as json_file:
    actori_data = json.load(json_file)

# Read director data from JSON file "regizori.json"
with open('regizori.json', 'r') as json_file:
    regizori_data = json.load(json_file)

# Initialize an RDF graph
g = Graph()

# Function to create movie instances in the ontology
def create_movie_instances(graph, filme_data):
    for movie_data in filme_data:
        movie_id = ex_ns[movie_data['id']]
        graph.add((movie_id, RDF.type, filme_ns.Film))
        graph.add((movie_id, filme_ns.titlu, Literal(movie_data['titlu'])))
        graph.add((movie_id, filme_ns.anul_de_lansare, Literal(movie_data['anul_de_lansare'], datatype=XSD.integer)))
        graph.add((movie_id, filme_ns.genuri, Literal(movie_data['genuri'])))
        graph.add((movie_id, filme_ns.durata, Literal(movie_data['durata'], datatype=XSD.integer)))
        graph.add((movie_id, filme_ns.rating, Literal(movie_data['rating'], datatype=XSD.float)))
        graph.add((movie_id, filme_ns.tip, Literal(movie_data['tip'])))
        graph.add((movie_id, filme_ns.limba, Literal(movie_data['limba'])))
        
        # Add relationships with directors
        directors = movie_data['regizori'].split(', ')
        for director_name in directors:
            clean_director_name = clean_name(director_name)
            director_uri = ex_ns[clean_director_name]
            graph.add((movie_id, filme_ns.Directed_By, director_uri))

        # Add relationships with actors
        actors = movie_data['actori'].split(', ')
        for actor_name in actors:
            clean_actor_name = clean_name(actor_name)
            actor_uri = ex_ns[clean_actor_name]
            graph.add((movie_id, filme_ns.Played_By, actor_uri))

# Function to create actor and director instances in the ontology
def create_person_instances(graph, person_data, person_type):
    for person in person_data:
        clean_person_name = clean_name(person['nume_prenume'])
        person_uri = ex_ns[clean_person_name]
        graph.add((person_uri, RDF.type, filme_ns[person_type]))
        graph.add((person_uri, filme_ns.nume_prenume, Literal(person['nume_prenume'])))
        if person['anul_nasterii']:
            graph.add((person_uri, filme_ns.anul_nasterii, Literal(person['anul_nasterii'], datatype=XSD.integer)))
        if person['anul_decesului']:
            graph.add((person_uri, filme_ns.anul_decesului, Literal(person['anul_decesului'], datatype=XSD.integer)))

# Create movie instances in the ontology
create_movie_instances(g, filme_data)

# Create actor instances in the ontology
create_person_instances(g, actori_data, 'Actor')

# Create director instances in the ontology
create_person_instances(g, regizori_data, 'Regizor')

# Write the RDF graph to a file
g.serialize(destination='filme_ontology.rdf', format='xml')
