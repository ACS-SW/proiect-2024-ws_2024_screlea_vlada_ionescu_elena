acum asta e ontologia 
<?xml version="1.0"?>

<rdf:RDF xmlns="http://www.semanticweb.org/ontologies/2024/filme#"
     xml:base="http://www.semanticweb.org/ontologies/2024/filme"
     xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
     xmlns:owl="http://www.w3.org/2002/07/owl#"
     xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
     xmlns:xsd="http://www.w3.org/2001/XMLSchema#">

    <!-- Clase -->
    
    <!-- Clasa Film -->
    <owl:Class rdf:about="#Film">
        <rdfs:label>Film</rdfs:label>
        <rdfs:comment>Entitate care reprezintă un film.</rdfs:comment>
    </owl:Class>

    <!-- Clasa Actor -->
    <owl:Class rdf:about="#Actor">
        <rdfs:label>Actor</rdfs:label>
        <rdfs:comment>Entitate care reprezintă un actor.</rdfs:comment>
    </owl:Class>

    <!-- Clasa Regizor -->
    <owl:Class rdf:about="#Regizor">
        <rdfs:label>Regizor</rdfs:label>
        <rdfs:comment>Entitate care reprezintă un regizor.</rdfs:comment>
    </owl:Class>

    <!-- Proprietăți -->

    <!-- Proprietatea id -->
    <owl:DatatypeProperty rdf:about="#id">
        <rdfs:label>id</rdfs:label>
        <rdfs:domain rdf:resource="#Film"/>
        <rdfs:domain rdf:resource="#Actor"/>
        <rdfs:domain rdf:resource="#Regizor"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#string"/>
    </owl:DatatypeProperty>

    <!-- Proprietatea titlu -->
    <owl:DatatypeProperty rdf:about="#titlu">
        <rdfs:label>titlu</rdfs:label>
        <rdfs:domain rdf:resource="#Film"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#string"/>
    </owl:DatatypeProperty>

    <!-- Proprietatea anul_de_lansare -->
    <owl:DatatypeProperty rdf:about="#anul_de_lansare">
        <rdfs:label>anul_de_lansare</rdfs:label>
        <rdfs:domain rdf:resource="#Film"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#integer"/>
    </owl:DatatypeProperty>

    <!-- Proprietatea genuri -->
    <owl:DatatypeProperty rdf:about="#genuri">
        <rdfs:label>genuri</rdfs:label>
        <rdfs:domain rdf:resource="#Film"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#string"/>
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#List"/>
    </owl:DatatypeProperty>

    <!-- Proprietatea durata -->
    <owl:DatatypeProperty rdf:about="#durata">
        <rdfs:label>durata</rdfs:label>
        <rdfs:domain rdf:resource="#Film"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#integer"/>
    </owl:DatatypeProperty>

    <!-- Proprietatea rating -->
    <owl:DatatypeProperty rdf:about="#rating">
        <rdfs:label>rating</rdfs:label>
        <rdfs:domain rdf:resource="#Film"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#float"/>
    </owl:DatatypeProperty>

    <!-- Proprietatea tip -->
    <owl:DatatypeProperty rdf:about="#tip">
        <rdfs:label>tip</rdfs:label>
        <rdfs:domain rdf:resource="#Film"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#string"/>
    </owl:DatatypeProperty>

    <!-- Proprietatea limba -->
    <owl:DatatypeProperty rdf:about="#limba">
        <rdfs:label>limba</rdfs:label>
        <rdfs:domain rdf:resource="#Film"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#string"/>
    </owl:DatatypeProperty>

    <!-- Proprietatea anul_nașterii -->
    <owl:DatatypeProperty rdf:about="#anul_nașterii">
        <rdfs:label>anul_nașterii</rdfs:label>
        <rdfs:domain rdf:resource="#Actor"/>
        <rdfs:domain rdf:resource="#Regizor"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#integer"/>
    </owl:DatatypeProperty>

    <!-- Proprietatea anul_decedării -->
    <owl:DatatypeProperty rdf:about="#anul_decedării">
        <rdfs:label>anul_decedării</rdfs:label>
        <rdfs:domain rdf:resource="#Actor"/>
        <rdfs:domain rdf:resource="#Regizor"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#integer"/>
    </owl:DatatypeProperty>

    <!-- Relații -->

    <!-- Relația Directed_By -->
    <owl:ObjectProperty rdf:about="#Directed_By">
        <rdfs:label>Directed_By</rdfs:label>
        <rdfs:domain rdf:resource="#Film"/>
        <rdfs:range rdf:resource="#Regizor"/>
    </owl:ObjectProperty>

    <!-- Relația Played_By -->
    <owl:ObjectProperty rdf:about="#Played_By">
        <rdfs:label>Played_By</rdfs:label>
        <rdfs:domain rdf:resource="#Film"/>
        <rdfs:range rdf:resource="#Actor"/>
    </owl:ObjectProperty>

</rdf:RDF>
