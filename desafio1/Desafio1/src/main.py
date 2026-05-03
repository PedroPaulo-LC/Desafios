# main.py

import os
from utils.funcoes import cadastrar_funcionario, gerar_relatorio_texto


# --- FLUXO PRINCIPAL ---

def main():
    # A lista deve ser inicializada fora do while para não ser apagada
    banco_dados = []

    while True:
        print("\n1-Cadastrar | 2-Relatório | 3-Salvar | 4-Sair")
        op = input("Opção: ")

        if op == "1":
            novo = cadastrar_funcionario()
            if novo:
                banco_dados.append(novo)  # Aqui salvamos na memória
                print("Cadastrado com sucesso!")

        elif op == "2":
            print(gerar_relatorio_texto(banco_dados))

        elif op == "3":
            if not banco_dados:
                print("Erro: Cadastre alguém primeiro!")
            else:
                try:
                    conteudo = gerar_relatorio_texto(banco_dados)
                    with open("relatorio_folha.txt", "w", encoding="utf-8") as f:
                        f.write(conteudo)
                    print("Arquivo 'relatorio_folha.txt' gerado!")
                except Exception as e:
                    print(f"Falha ao salvar: {e}")

        elif op == "4":
            print("Saindo...")
            break


if __name__ == "__main__":
    main()