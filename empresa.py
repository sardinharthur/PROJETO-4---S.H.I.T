from dados import cadastrar_clientes, alterar_status
from relatorio import listar_clientes, pesquisar_chamado
from acoes import lancar_tecnico, excluir_chamado
import storage

class Empresa:
#listar, pesquisar, cadastrar, alterar status, excluir chamado, enviar técnico
#dividir em mais 3 arquivos py: além cliente.py, empresa.py, main.py, colocar o relatório.py, ações.py, dados.py
#decomposição -> func de cadastrar cliente e alterar status da pra por em um arquivo só de DADOS separado.

    def __init__(self):
        storage.init_db()
        self.clientes = []
        self.indice = {}
        # carregar clientes do banco
        rows = storage.load_all_clients()
        max_chamado = 0
        from cliente import Cliente
        for r in rows:
            cliente = Cliente(
                r.get("nome"),
                r.get("chamado"),
                r.get("problema"),
                r.get("cpf"),
                r.get("contato"),
                r.get("tipo_problema"),
                r.get("prazo_resolucao"),
                r.get("valor_manutencao"),
                r.get("peca"),
                r.get("quantidade_peca"),
                r.get("valor_peca"),
                r.get("forma_pagamento"),
                r.get("status_pagamento"),
                r.get("observacao_financeira"),
            )
            cliente.tecnico = r.get("tecnico")
            cliente.status = r.get("status") or cliente.status
            self.clientes.append(cliente)
            self.indice[cliente.chamado] = cliente
            if cliente.chamado and cliente.chamado > max_chamado:
                max_chamado = cliente.chamado

        self.proximo_chamado = max_chamado + 1 if max_chamado > 0 else 1

    def cadastrar_clientes(self):
        cadastrar_clientes(self)

    def alterar_status(self):
        alterar_status(self)

    #decomposição -> arquivo de relatório : listagem e pesquisar e pesquisar separado para um de RELATÓRIO.py

    def listar_clientes(self):
        listar_clientes(self)

    def pesquisar_chamado(self):
        pesquisar_chamado(self)

    #decomposição de enviar técnico ou exlcuir chamado para um arquivo só de AÇÕES.py            

    def lancar_tecnico(self):
        lancar_tecnico(self)

    def excluir_chamado(self):
        excluir_chamado(self)
