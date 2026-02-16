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
        for i, funcionario in enumerate(self._funcionarios):
            if funcionario._nome.lower() == nome.lower():
                demitido = self._funcionarios.pop(i)
                print(f"Funcionário {demitido._nome} foi demitido!")
                self._contratados -= 1
    
    def listar_funcionarios(self):
        print(f"Funcionários contratados: {self._contratados}")
        for funcionario in self._funcionarios:
            x = f"Salário: {self._nome}"
            a = '=' * len(x)
            print(a)
            print(funcionario)
            
    def folha_de_pagamento(self):
        folha_pag = 0
        for funcionario in self._funcionarios:
            folha_pag += funcionario._salario
        print(f"Total da folha: R$ {folha_pag:.2f}\nTotal de funcionários: {self._contratados}\nMédia salarial: R$ {(folha_pag / self._contratados):.2f}")