############################################################
######          CRUD (Simples) Para Clientes          ######
######                   DIÊGO AXEL                   ######
######                    CAICÓ-RN                    ######
############################################################

'''imports'''
import menu
import clientes

'''programa principal'''

op_cliente = ""
while op_cliente != "0":
    op_cliente = menu.menu_cliente()
    print()
    if op_cliente == "1":
        clientes.cadastrar_cliente()
    elif op_cliente == "2":
        clientes.exibir_cliente()
    elif op_cliente == "3":
        clientes.alterar_dados()
    elif op_cliente == "4":
        clientes.excluir_cliente()
    elif op_cliente == "5":
        clientes.relatorio_clientes()