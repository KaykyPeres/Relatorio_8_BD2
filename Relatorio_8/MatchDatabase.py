class MatchDatabase:
    def __init__(self, database):
        self.db = database

    def create_Player(self, name):
        query = "CREATE (:Player {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)


    def create_Partida(self, name, Player_name):
        query = "MATCH (p:Player {name: $Player_name}) CREATE (:Aula {name: $name})<-[:MINISTRA]-(p)"
        parameters = {"name": name, "Player_name": Player_name}
        self.db.execute_query(query, parameters)

    def get_Player(self):
        query = "MATCH (p:Player) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]


    def get_Partida(self):
        query = "MATCH (a:Partida)<-[:MINISTRA]-(p:Player) RETURN a.name AS name, p.name AS Player_name"
        results = self.db.execute_query(query)
        return [(result["name"], result["Player_name"]) for result in results]

    def update_Player(self, old_name, new_name):
        query = "MATCH (p:Player {name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)

    def insert_Player_Partida(self, Player_name, Partida_name):
        query = "MATCH (a:Player {name: $Player_name}) MATCH (b:Partida {name: $Partida_name}) CREATE (a)-[:JOGA]->(b)"
        parameters = {"Player_name": Player_name, "Partida_name": Partida_name}
        self.db.execute_query(query, parameters)


    def delete_Player(self, name):
        query = "MATCH (p:Player {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def delete_Partida(self, name):
        query = "MATCH (a:Partida {name: $name})<-[:Joga]-(p:Professor) DETACH DELETE a"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)