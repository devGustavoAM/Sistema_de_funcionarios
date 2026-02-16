from funcionarios import *
from empresa import *

empresa1 = Empresa("WLM Itaipu Norte")

funcionario1 = Funcionario("Gustavo Araújo de Menezes", "Auxiliar de Almoxarifado", 3500)
funcionario2 = Funcionario("Beatriz Cavalcanti", "Analista de RH", 4800)
funcionario3 = Funcionario("Marcos Vinícius Rocha", "Desenvolvedor Backend", 7500)
funcionario4 = Funcionario("Juliana Farias", "Gerente de Projetos", 9200)
funcionario5 = Funcionario("Ricardo Nunes", "Coordenador de Logística", 5600)
funcionario6 = Funcionario("Camila Oliveira", "Designer UI/UX", 6300)
funcionario7 = Funcionario("Fernando Souza", "Assistente Administrativo", 2800)
funcionario8 = Funcionario("Patrícia Almeida", "Especialista em Marketing", 7100)


def main():
    empresa1.contratar(funcionario1)
    empresa1.contratar(funcionario2)
    empresa1.contratar(funcionario3)
    empresa1.contratar(funcionario4)
    empresa1.contratar(funcionario5)
    empresa1.contratar(funcionario6)
    empresa1.contratar(funcionario7)
    empresa1.contratar(funcionario8)
    
if __name__ == "__main__":
    main()