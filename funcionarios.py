class Funcionario:
    def __init__(self, nome: str, cargo: str, salario: float):
        self._nome = nome
        self._cargo = cargo
        self._salario = salario
        
    def __str__(self):        
        return f"Nome: {self._nome}\nCargo: {self._cargo}\nSalário: {self._salario:.2f}"
        
    def exibir_info(self):
        print(f"Nome: {self._nome}\nCargo: {self._cargo}\nSalário: {self._salario:.2f}")
        
    def aumentar_salario(self, percentual: int):
        x = self._salario
        self._salario = (x + (x * (percentual / 100)))