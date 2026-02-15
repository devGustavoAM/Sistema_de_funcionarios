Esse projeto tem como objetivo criar um sistema simples de gerenciamento de funcionários, usando os conceitos de Programação Orientada a Objetos.

Classes:
- Funcionario:
    - Atributos:
        - _nome
        - _cargo
        - _salario
    - métodos:
        - __init__(self, nome, cargo, salario)
        - getters e setters com @property
        - aumentar_salario(percentual)
        - exibir_info()

- Empresa:
    - Atributos:
        - _nome
        - _funcionarios (lista)
    - Métodos:
        - contratar(funcionario)
        - demitir(nome)
        - listar_funcionarios()
        - folha_pagamento()
        - buscar_por_cargo(cargo)