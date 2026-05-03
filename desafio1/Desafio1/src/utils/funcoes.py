# funcoes.py

# --- FUNÇÕES DE CÁLCULO (Regras de Negócio) ---

def calcular_estagiario(valor):
    # Estagiário: sem descontos
    return valor, 0.0, 0.0, valor

def calcular_clt(valor):
    # CLT: 8% INSS. IRRF 10% se > 2000
    inss = valor * 0.08
    irrf = (valor * 0.10) if valor > 2000 else 0.0
    liquido = valor - inss - irrf
    return valor, inss, irrf, liquido

def calcular_freelancer(valor_h, horas):
    # Freelancer: bruto = h * v. Desconto fixo 5%
    bruto = valor_h * horas
    desconto = bruto * 0.05
    liquido = bruto - desconto
    return bruto, desconto, 0.0, liquido


# --- FUNÇÕES DE GERENCIAMENTO ---

def cadastrar_funcionario():
    """Solicita dados e retorna um dicionário preenchido."""
    try:
        nome = input("Nome: ").strip()
        if not nome:
            raise ValueError("Nome obrigatório.")

        tipo = input("Tipo (Estagiario/CLT/Freelancer): ").strip().lower()

        if tipo == 'freelancer':
            v_h = float(input("Valor por hora: "))
            hrs = float(input("Horas trabalhadas: "))
            if v_h <= 0 or hrs <= 0:
                raise ValueError("Valores devem ser positivos.")
            bruto, desc_inss, desc_irrf, liquido = calcular_freelancer(v_h, hrs)

        elif tipo in ['clt', 'estagiario']:
            sal = float(input("Salário: "))
            if sal <= 0:
                raise ValueError("Salário deve ser positivo.")
            if tipo == 'clt':
                bruto, desc_inss, desc_irrf, liquido = calcular_clt(sal)
            else:
                bruto, desc_inss, desc_irrf, liquido = calcular_estagiario(sal)
        else:
            raise ValueError("Tipo de funcionário inválido.")

        return {
            "nome": nome, "tipo": tipo.capitalize(),
            "bruto": bruto, "inss": desc_inss,
            "irrf": desc_irrf, "liquido": liquido
        }
    except ValueError as e:
        print(f"Erro: {e}")
        return None

def gerar_relatorio_texto(lista):
    """Transforma a lista de dicionários na string do relatório."""
    if not lista:
        return "Nenhum funcionário cadastrado."

    texto = "=== Relatório de Folha de Pagamento ===\n"
    total = 0
    for f in lista:
        texto += f"Nome: {f['nome']}\nTipo: {f['tipo']}\n"
        texto += f"Salário Bruto: R$ {f['bruto']:.2f}\n"
        texto += f"Desconto INSS: R$ {f['inss']:.2f}\n"
        texto += f"Desconto IRRF: R$ {f['irrf']:.2f}\n"
        texto += f"Salário Líquido: R$ {f['liquido']:.2f}\n"
        texto += "-" * 30 + "\n"
        total += f['liquido']

    texto += f"Total pago pela empresa: R$ {total:.2f}"
    return texto