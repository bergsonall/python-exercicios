import os
restaurantes = [{'nome':'Sushi', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

def voltar_menu_principal():
    input('\nDigite Enter para voltar ao menu pricipal')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def opcao_invalida():
    os.system('cls')
    print('Opção invalida.')
    voltar_menu_principal()

def exibir_nome_app():
    print('Sabor-Express \n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar estado do restaurante')
    print('4. Sair\n')

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novo restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_restaurante = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    dados_cadastro = {'nome':nome_restaurante, 'categoria':categoria_restaurante, 'ativo':False}
    restaurantes.append(dados_cadastro)
    print(f'Restaurante {nome_restaurante} cadastrado com sucesso.\n')
    voltar_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Lista de restaurantes:')
    print(f'{"Nome restaurante".center(20)} | {"Categoria".center(20)} | {"Status".center(10)}')
    for r in restaurantes:
        nome = r['nome']
        categoria = r['categoria']
        ativo = 'Ativo' if r['ativo'] else 'Desativado'
        print(f'- {nome.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_menu_principal()

def mudar_estado_restaurante():
    exibir_subtitulo('Alterando o estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja mudar o estado: ')
    restaurante_encontrado = False

    for r in restaurantes:
        if nome_restaurante == r['nome']:
            restaurante_encontrado = True
            r['ativo'] = not r['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso.' if r['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso.'
            print(mensagem)
    if not restaurante_encontrado:
        print('Este nome de restaurante nao foi encontrado.')
    voltar_menu_principal()

def finalizar_app():
    exibir_subtitulo('App finalizado')

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                mudar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_app()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()