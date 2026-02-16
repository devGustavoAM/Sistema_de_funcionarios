from funcionarios import *

class Empresa:
    _contratados = 0
    
    def __init__(self, nome: str, funcionarios: list = []):
        self._nome = nome
        self._funcionarios = funcionarios
        
    def contratar(self, funcionario: Funcionario):
        self._funcionarios.append(funcionario)
        self._contratados += 1
        
    def demitir(self, nome):
        pass
    
    def listar_funcionarios(self):
        print(f"Funcionários contratados: {self._contratados}")
        for funcionario in self._funcionarios:
            print(funcionario)