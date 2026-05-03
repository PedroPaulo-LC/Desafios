produtos = []
vendas = []

def cadastrar_produto():
    try:
        nome = input("Nome do produto: ").strip()
        if not nome:
            print("Nome inválido!")
            return

        for p in produtos:
            if p["nome"].lower() == nome.lower():
                print("Produto já existe!")
                return

        preco = float(input("Preço: "))
        if preco <= 0:
            print("Preço inválido!")
            return

        estoque = int(input("Estoque: "))
        if estoque < 0:
            print("Estoque inválido!")
            return

        produtos.append({
            "nome": nome,
            "preco": preco,
            "estoque": estoque
        })

        print("Produto cadastrado com sucesso!")

    except:
        print("Erro: entrada inválida!")


def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado!")
        return False

    print("\n=== PRODUTOS ===")
    for i, p in enumerate(produtos):
        print(f"{i+1}. {p['nome']} - R$ {p['preco']:.2f} - Estoque: {p['estoque']}")
    return True


def calcular_venda(produto, quantidade):
    valor_bruto = produto["preco"] * quantidade

    desconto = 0
    if quantidade > 10:
        desconto = valor_bruto * 0.05

    valor_final = valor_bruto - desconto
    produto["estoque"] -= quantidade

    return {
        "produto": produto["nome"],
        "quantidade": quantidade,
        "valor_bruto": valor_bruto,
        "desconto": desconto,
        "valor_final": valor_final
    }


def realizar_venda():
    if not listar_produtos():
        return

    try:
        cliente = input("Nome do cliente: ").strip()
        if not cliente:
            print("Nome inválido!")
            return

        escolha = int(input("Escolha o produto (número): ")) - 1

        if escolha < 0 or escolha >= len(produtos):
            print("Produto inválido!")
            return

        produto = produtos[escolha]

        quantidade = int(input("Quantidade: "))
        if quantidade <= 0:
            print("Quantidade inválida!")
            return

        if quantidade > produto["estoque"]:
            print("Estoque insuficiente!")
            return

        venda = calcular_venda(produto, quantidade)
        venda["cliente"] = cliente

        vendas.append(venda)

        print("Venda realizada com sucesso!")

    except:
        print("Erro: entrada inválida!")


def gerar_relatorio():
    if not vendas:
        print("Nenhuma venda realizada!")
        return

    total = 0

    print("\n=== RELATÓRIO ===")

    for v in vendas:
        print(f"\nCliente: {v['cliente']}")
        print(f"Produto: {v['produto']}")
        print(f"Quantidade: {v['quantidade']}")
        print(f"Valor Bruto: R$ {v['valor_bruto']:.2f}")
        print(f"Desconto: R$ {v['desconto']:.2f}")
        print(f"Valor Final: R$ {v['valor_final']:.2f}")

        total += v["valor_final"]

    print(f"\nTotal arrecadado: R$ {total:.2f}")


def salvar_relatorio():
    try:
        with open("relatorio_vendas.txt", "w", encoding="utf-8") as f:
            total = 0

            f.write("=== RELATÓRIO ===\n")

            for v in vendas:
                f.write(f"\nCliente: {v['cliente']}\n")
                f.write(f"Produto: {v['produto']}\n")
                f.write(f"Quantidade: {v['quantidade']}\n")
                f.write(f"Valor Bruto: R$ {v['valor_bruto']:.2f}\n")
                f.write(f"Desconto: R$ {v['desconto']:.2f}\n")
                f.write(f"Valor Final: R$ {v['valor_final']:.2f}\n")

                total += v["valor_final"]

            f.write(f"\nTotal arrecadado: R$ {total:.2f}\n")

        print("Relatório salvo com sucesso!")

    except:
        print("Erro ao salvar arquivo!")
