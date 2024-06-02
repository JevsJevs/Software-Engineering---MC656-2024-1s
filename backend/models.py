class Atleta:
    def __init__(self, id, nome, genero, idade, noc):
        self.id = id
        self.nome = nome
        self.genero = genero
        self.idade = idade
        self.noc = noc

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'genero': self.genero,
            'idade': self.idade,
            'noc': self.noc,
        }
    
class Esporte:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
        }

class Evento:
    def __init__(self, id, nome, esporte):
        self.id = id
        self.nome = nome
        self.esporte = esporte

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'esporte': self.esporte
        }

class Medalha:
    def __init__(self, id, atleta, evento, tipo):
        self.id = id
        self.atleta = atleta
        self.evento = evento
        self.tipo = tipo

    def to_dict(self):
        return {
            'id': self.id,
            'atleta': self.atleta,
            'evento': self.evento,
            'tipo': self.tipo
        }
    
class NOC:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
        }

class Countries:
    def __init__(self, id, alpha_2, alpha_3, en, pt):
        self.id = id
        self.alpha_2 = alpha_2
        self.alpha_3 = alpha_3
        self.en = en
        self.pt = pt


    def to_dict(self):
        return {
            'id': self.id,
            'alpha_2': self.alpha_2,
            'alpha_3': self.alpha_3,
            'en': self.en,
            'pt': self.pt
        }