############################################################
######          CRUD (Simples) Para Clientes          ######
######                   DIÊGO AXEL                   ######
######                    CAICÓ-RN                    ######
############################################################

'''imports'''
import menu
import cadastrar
import exibir_dados as exibir
import alterar_dados as alterar
import excluir
import relatorio
import encerramento as end

'''programa principal'''

op_cliente = ""
while op_cliente != "0":
    op_cliente = menu.menu_cliente()
    print()
    if op_cliente == "1":
        cadastrar.cadastro()
    elif op_cliente == "2":
        exibir.exibir_cliente()
    elif op_cliente == "3":
        alterar.alterar_dados()
    elif op_cliente == "4":
        excluir.excluir_cliente()
    elif op_cliente == "5":
        relatorio.relatorio_clientes()
end.encerramento()
print("Programa encerrado. Até breve.")
print()