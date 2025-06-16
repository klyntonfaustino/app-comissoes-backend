# App de Comissões - Backend

API simples para cálculo de comissões para motoristas, feita com FastAPI.

## Funcionalidades

- Recebe valor da carga e percentual da comissão via query parameters
- Calcula a comissão e retorna o valor
- Estruturada para expansão e integração com front-end ou outras APIs

## Tecnologias usadas

- Python 3.12
- FastAPI
- Uvicorn (servidor ASGI)
- Pydantic (validação de dados)

## Como rodar localmente

1. Clone o repositório:
```bash
git clone git@github.com:klyntonfaustino/app-comissoes-backend.git
cd app-comissoes-backend

2. Crie e ative o ambiente virtual:
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate   # Windows

3. Instale as dependências:
pip install fastapi uvicorn

4. Rode a aplicação:
uvicorn main:app --reload

5. Acesse no navegador ou via API client:
http://127.0.0.1:8000/comissao?valor_carga=1500&percentual_comissao=12

## Estrutura do projeto

app-comissoes-backend/
├── app/
│   ├── __init__.py
│   └── routes.py          # Define as rotas da API
├── main.py                # Arquivo principal da API FastAPI
├── README.md              # Documentação do projeto
├── .gitignore             # Arquivos ignorados pelo Git
└── venv/                  # Ambiente virtual (não commitado)

Como contribuir
Faça um fork deste repositório

Crie uma branch com sua feature: git checkout -b minha-feature

Commit suas mudanças: git commit -m "Descrição da feature"

Faça push da branch: git push origin minha-feature

Abra um Pull Request

Qualquer dúvida, me chama!
Klynton Faustino
