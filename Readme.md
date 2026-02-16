Esse projeto tem como objetivo criar um sistema simples de gerenciamento de funcionários, usando os conceitos de Programação Orientada a Objetos.

Classes:
- Funcionario:
    - Atributos:
        v- _nome
        v- _cargo
        v- _salario
    - métodos:
        v- __init__(self, nome, cargo, salario)
        - getters e setters com @property
        v- aumentar_salario(percentual)
        v- exibir_info()

- Empresa:
    - Atributos:
        v- _nome
        v- _funcionarios (lista)
    - Métodos:
        v- contratar(funcionario)
        - demitir(nome)
        v- listar_funcionarios()
        - folha_pagamento()
        - buscar_por_cargo(cargo)