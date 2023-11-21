#Crud de onibus
# Cadatrar novos onibbus com atributos ()
# Excluir Oñibus que sairam de circulação (Armazenados em outro banco)
# Editar Onibus ja em rotas
# Filtrar 
# Pesquisar Onibus em rotas


# Alterações globais
filadeOnibus = []


# menu de opções
def menuPrincipal():
    menu = '''
    ====================================
                OPCOES              
    ====================================
    [1] CADASTRAR ONIBUS
    [2] EDITAR ONIBUS
    [3] EXCLUIR ONIBUS
    [4] PESQUISAR ONIBUS
    [5] MOSTRAR ONIBUS
    [T] TERMINAR SESSAO
    ====================================
    '''
    return menu

#Classe global
class Onibus:
    def __init__(self, cor, rota, id):
        self.cor = cor
        self.rota = rota
        self.id = id

# Filtrar onibus
def filtrar(id):
    if (filadeOnibus == len(0)):
        return ('Não há onibus cadastrados')
    
    for onibus in filadeOnibus:
        if id == onibus:
            return onibus
        



# Opcao de cadastro
def cadastrar():
    id = int(input('Qual o identificador: '))
    rota = input("Informe a rota/nome destinada: ")
    cor = input("Informe a cor: ")

    onibusCriado = Onibus(cor, rota, id)
    filadeOnibus.append(onibusCriado)
    print('Onibus cadastrado com sucesso!')
    return onibusCriado

# Opcao de editar
def editar():
    if (filadeOnibus == len(0)):
        return ('Não há onibus cadastrados')
    
    mostrar()

        

# Opcao de mostrar onibus
def mostrar():
    print("Fila de ônibus: ")
    for onibus in filadeOnibus:
        print("Rota:", onibus.rota, "Cor:", onibus.cor)

# Mostrar menu principal
def principal():
    operacao = True
    while operacao:
        print(menuPrincipal())
        operacao = input("DIGITE O NUMERO DO ACESSO: ")
        if (operacao == '1'):
            cadastrar()
        if (operacao == '2'):
            editar()
        if (operacao == '3'):
            excluir()
        if (operacao == '4'):
            pesquisar()
        if (operacao == '5'):
            mostrar()
        if (operacao.upper() == 'T'):
            print('TERMINANDO...')
            break
    return "COMAMDO NÃO IDENTIFICADO, TENTE NOVAMENTE!"

principal()