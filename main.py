############################################################
######          CRUD (Simples) Para Clientes          ######
######                   DIÊGO AXEL                   ######
######                    CAICÓ-RN                    ######
############################################################

'''imports'''
import menu
import cadastrar
import exibir_dados as exdd
import alterar_dados as altd
import excluir
import relatorio
import os

'''programa principal'''

op_cliente = ""
while op_cliente != "0":
    op_cliente = menu.menu_cliente()
    print()
    if op_cliente == "1":
        cadastrar.cadastro()
    elif op_cliente == "2":
        exdd.exibir_cliente()
    elif op_cliente == "3":
        altd.alterar_dados()
    elif op_cliente == "4":
        excluir.excluir_cliente()
    elif op_cliente == "5":
        relatorio.relatorio_clientes()

os.system('celar || cls')