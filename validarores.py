'''Arquivo para as minhas funções a respeito da validação'''

'''imports'''
import re

#################################################
#####            VALIDAR -EMAIL             #####
#################################################

def validar_email(email): # Função para verificar se o e-mail é válido (GPT)
    padrao = re.compile(r'^[\w-]+@[a-z\d]+\.[\w]{2,3}$')
    return padrao.match(email) is not None


#################################################
#####            VALIDAR CELULAR            #####
#################################################

def validar_numero(numero): # Função para validar telefone (GPT)
    padrao = re.compile(r'^\(\d{2}\) \d{4,5}-\d{4}$')
    return padrao.match(numero) is not None