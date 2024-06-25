from modelos.restaurante import Restaurante

restaurante_pizza = Restaurante('pizza maluca', 'Italiano')
restaurante_pizza.alterar_status()
restaurante_pizza.receber_avaliacao('Bruno', 10)
restaurante_pizza.receber_avaliacao('Carol', 8)
restaurante_pizza.receber_avaliacao('Vini', 5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()