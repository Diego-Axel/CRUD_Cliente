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