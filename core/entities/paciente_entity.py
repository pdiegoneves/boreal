from core.dataproviders.paciente_dpo import paciente_dpo

class Paciente():
    def __init__(self, id, nome, data_de_nascimento, identificador, sexo):
        self.id = id
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
        self.identificador = identificador
        self.sexo = sexo
    
    