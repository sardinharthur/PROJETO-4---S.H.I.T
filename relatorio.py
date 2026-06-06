def listar_clientes(self):
    if len(self.clientes) == 0:
        print("\nNenhum cliente cadastrado.")
        return

    print("\nLISTA DE CLIENTES ATIVOS")
    for cliente in self.clientes:
        print(f"Chamado: {cliente.chamado} | Nome: {cliente.nome} | Status: {cliente.status}")
            
    total_clientes = len(self.clientes)
    print(f"\nTotal de clientes cadastrados: {total_clientes}")
                   

def pesquisar_chamado(self):
    if len(self.clientes) == 0:
        print("\nNenhum cliente cadastrado.")
        return
    while True:
        try:
            chamado = int(input("Digite o número do chamado: "))
            break
        except ValueError:
            print("\nDigite apenas números.\n")

    cliente = None
    try:
        cliente = self.indice.get(chamado)
    except Exception:
        for c in self.clientes:
            if c.chamado == chamado:
                cliente = c
                break

    if cliente:
        cliente.exibir_dados()
        return

    print(f"\nChamado {chamado} não encontrado.")
