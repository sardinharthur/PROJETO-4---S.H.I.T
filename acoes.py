import storage


def lancar_tecnico(self):
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

    if cliente is None:
        print(f"\nChamado {chamado} não encontrado.")
        return

    if cliente.status == "Técnico enviado":
        print(f"\nAviso: O técnico já está a caminho para o chamado {chamado}!")
        return

    print("\nEnviando técnico...")
    print(f"Cliente: {cliente.nome}")
    print(f"Problema: {cliente.problema}")
    print(f"Prazo estimado de resolução: {cliente.prazo_resolucao}")

    cliente.tecnico = "Técnico enviado"
    cliente.status = "Técnico enviado"

    try:
        storage.update_cliente(chamado, tecnico=cliente.tecnico, status=cliente.status)
    except Exception:
        print("Aviso: não foi possível atualizar o chamado no banco de dados.")

    print("\nTécnico enviado com sucesso.")


def excluir_chamado(self):
    if len(self.clientes) == 0:
        print("\nNenhum cliente cadastrado.")
        return

    while True:
        try:
            chamado = int(input("Digite o número do chamado a ser excluído: "))
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

    if cliente is None:
        print(f"\nChamado {chamado} não encontrado.")
        return

    print("\nDados do chamado a ser excluído: ")
    cliente.exibir_dados()
    confirmacao = input("\nDeseja realmente excluir este chamado? (SIM/NAO): ").strip().upper()

    match confirmacao:
        case "SIM":
            try:
                self.clientes.remove(cliente)
            except ValueError:
                pass

            try:
                del self.indice[chamado]
            except Exception:
                pass

            try:
                storage.delete_cliente(chamado)
            except Exception:
                print("Aviso: não foi possível excluir o chamado do banco de dados.")

            print(f"\nChamado {chamado} excluído com sucesso.")
        case "NAO":
            print("\nExclusão cancelada.")
        case _:
            print("\nOpção inválida. Exclusão cancelada.")
    return
