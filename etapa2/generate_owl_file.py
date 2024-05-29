<?xml version="1.0"?>

<rdf:RDF
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
    xmlns:owl="http://www.w3.org/2002/07/owl#"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
    xmlns:film="http://example.com/film-ontology#"
    xml:base="http://example.com/film-ontology">

    <owl:Ontology rdf:about="">
        <owl:imports rdf:resource="http://www.w3.org/2002/07/owl#"/>
    </owl:Ontology>

    <!-- Declararea claselor principale: Film, Regizor, Actor -->
    <owl:Class rdf:about="Film"/>
    <owl:Class rdf:about="Director"/>
    <owl:Class rdf:about="Actor"/>

    <!-- Proprietățile filmului -->
    <owl:DatatypeProperty rdf:about="hasTitle"/>
    <owl:DatatypeProperty rdf:about="hasReleaseYear"/>
    <owl:DatatypeProperty rdf:about="hasRating"/>
    <owl:DatatypeProperty rdf:about="hasDuration"/>
    <owl:DatatypeProperty rdf:about="hasType"/>

    <!-- Proprietăți pentru regizor și actor -->
    <owl:DatatypeProperty rdf:about="hasName"/>

    <!-- Relații cu regizorii și actorii -->
    <owl:ObjectProperty rdf:about="hasDirector"/>
    <owl:ObjectProperty rdf:about="hasActor"/>

    <!-- Definirea relațiilor dintre entități -->
    <rdf:Description rdf:about="Film">
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Class"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="hasDirector"/>
                <owl:someValuesFrom rdf:resource="Director"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="hasActor"/>
                <owl:someValuesFrom rdf:resource="Actor"/>
            </owl:Restriction>
        </rdfs:subClassOf>
    </rdf:Description>

    <!-- Declararea restricțiilor pentru relațiile cu regizorii și actorii -->

    <!-- Regizorul poate regiza cel puțin un film -->
    <rdf:Description rdf:about="Director">
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Class"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="hasDirector"/>
                <owl:minCardinality rdf:datatype="http://www.w3.org/2001/XMLSchema#nonNegativeInteger">1</owl:minCardinality>
            </owl:Restriction>
        </rdfs:subClassOf>
    </rdf:Description>

    <!-- Actorul poate juca în cel puțin un film -->
    <rdf:Description rdf:about="Actor">
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Class"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="hasActor"/>
                <owl:minCardinality rdf:datatype="http://www.w3.org/2001/XMLSchema#nonNegativeInteger">1</owl:minCardinality>
            </owl:Restriction>
        </rdfs:subClassOf>
    </rdf:Description>

</rdf:RDF>
