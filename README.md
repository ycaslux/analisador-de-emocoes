#  Analisador de Texto

Aplicação web para análise de sentimentos em textos, com histórico de análises e interface visual simples.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)

---

##  Funcionalidades

- Análise de sentimento de textos (positivo, negativo ou neutro)
- Contagem de palavras e caracteres
- Histórico de análises realizadas
- Exclusão de análises do histórico
- API REST com Flask

---

##  Demonstração

> Digite um texto → clique em Analisar -> veja o sentimento detectado e o histórico completo.

---

## 🛠️ Tecnologias

- **Back-end:** Python 3, Flask, Flask-CORS
- **Front-end:** HTML, CSS, JavaScript (Fetch API)
- **Arquitetura:** API REST + interface estática

---

##  Como rodar localmente

### Pré-requisitos

- [Python 3.8+](https://www.python.org/downloads/) instalado
- Terminal (CMD, PowerShell ou bash)

### Passo a passo

**1. Clone o repositório**
```bash
git clone https://github.com/ycaslux/analisador-de-emocoes.git
cd analisador-de-texto
```

**2. Crie e ative um ambiente virtual**

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Inicie a API**
```bash
python app.py
```

**5. Abra o front-end**

Abra o arquivo `index.html` diretamente no navegador. A API estará rodando em `http://127.0.0.1:5000`.

---

## 📡 Endpoints da API

| Método | Rota | Descrição |
|--------|------|-----------|
| `POST` | `/analise` | Envia um texto para análise |
| `GET` | `/analises` | Lista todas as análises |
| `DELETE` | `/analise/<id>` | Remove uma análise pelo ID |

### Exemplo de requisição

```bash
curl -X POST http://127.0.0.1:5000/analise \
  -H "Content-Type: application/json" \
  -d '{"texto": "Hoje foi um dia maravilhoso!"}'
```

### Exemplo de resposta

```json
{
  "id": 1,
  "texto": "Hoje foi um dia maravilhoso!",
  "sentimento": "positivo",
  "quantidade_palavras": 6,
  "quantidade_caracteres": 28,
  "data_hora": "17/03/2026 14:30:00"
}
```

---

## 📁 Estrutura do projeto

```
analisador-de-texto/
├── app.py            # API Flask (back-end)
├── index.html        # Interface web (front-end)
├── requirements.txt  # Dependências Python
├── .gitignore        # Arquivos ignorados pelo Git
└── README.md         # Documentação
```

---

## 👤 Autor

**Lucas Gralha**  
[![GitHub](https://img.shields.io/badge/GitHub-ycaslux-181717?style=flat&logo=github)](https://github.com/ycaslux)
