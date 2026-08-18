# Deploy na Oracle Cloud Infrastructure (OCI)

Este projeto foi preparado para utilizar OCI Generative AI e para ser executado em container na Oracle Cloud.

## 1. Criar/configurar o projeto no OCI Generative AI

1. Acesse o Console da Oracle Cloud.
2. Abra o serviço Generative AI.
3. Crie ou selecione um projeto.
4. Na aba **How to use / Como usar**, obtenha a URL de inferência, o OCID do projeto, a chave de API do Generative AI e escolha um modelo disponível na sua região.
5. Configure as variáveis presentes em `.env.example`.

Nunca envie a chave real para o GitHub.

## 2. Testar localmente

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
streamlit run app.py
```

Linux/macOS:

```bash
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
streamlit run app.py
```

## 3. Gerar a imagem Docker

```bash
docker build -t corpmind-ai .
docker run --env-file .env -p 8501:8501 corpmind-ai
```

A aplicação ficará disponível na porta 8501.

## 4. Publicar a imagem no OCI Container Registry

Crie um repositório no Container Registry da sua região e publique a imagem Docker seguindo as instruções apresentadas pelo próprio Console OCI para autenticação, tag e push.

## 5. Criar um OCI Container Instance

No Console OCI:

1. Abra **Developer Services > Container Instances**.
2. Crie uma nova Container Instance.
3. Selecione a imagem publicada no OCI Container Registry.
4. Configure a porta 8501.
5. Adicione as quatro variáveis `OCI_GENAI_*` como variáveis de ambiente do container.
6. Utilize uma subnet com acesso de entrada compatível com a demonstração do projeto.
7. Inicie a instância e teste o endereço público.

## 6. Evidência obrigatória para o Challenge

Depois que a aplicação estiver online:

1. Abra a URL pública do CorpMind AI.
2. Faça uma pergunta de teste, por exemplo: `Qual é o valor do vale-alimentação?`.
3. Tire uma captura de tela mostrando a aplicação e a resposta.
4. Salve o arquivo no repositório, por exemplo em `assets/deploy-oci.png`.
5. Inclua a imagem e a URL pública no README principal.

## Referências oficiais Oracle

- OCI Generative AI: https://docs.oracle.com/en-us/iaas/Content/generative-ai/home.htm
- Como usar um projeto do Generative AI: https://docs.oracle.com/en-us/iaas/Content/generative-ai/use-project.htm
- OCI Container Instances: https://docs.oracle.com/en-us/iaas/Content/container-instances/home.htm
