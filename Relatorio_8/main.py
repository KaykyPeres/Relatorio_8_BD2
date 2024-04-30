from Database import Database
from MatchDatabase import MatchDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.235.168.48:7687", "neo4j", "badge-aid-strips")
db.drop_all()

# Criando uma instância da classe matchDatabase para interagir com o banco de dados
Match_db = MatchDatabase(db)

# Criando alguns Players
Match_db.create_Player("Du")
Match_db.create_Player("DuDu")
Match_db.create_Player("eDu")


# Criando algumas partidas e suas relações com os jogadores
Match_db.create_Partida("1", "Du")
Match_db.create_Partida("2", "DuDu")
Match_db.create_Partida("3", "eDu")

# Atualizando o nome de um player
Match_db.update_Player("eDu", "EDu")

Match_db.insert_Player_Partida("Du", "1")
Match_db.insert_Player_Partida("DuDu", "2")
Match_db.insert_Player_Partida("EDu", "3")

# Deletando um player e uma partida
Match_db.delete_aluno("EDu")
Match_db.delete_aula("3")

# Imprimindo todas as informações do banco de dados
print("Players:")
print(Match_db.get_Players())
print("Partidas:")
print(Match_db.get_Partidas())

# Fechando a conexão com o banco de dados
db.close()