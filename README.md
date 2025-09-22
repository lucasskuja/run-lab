# run-lab

> Projeto de estudo para deploy de funções Python no Google Cloud Run

## Estrutura do Projeto

- `app.py`: Arquivo principal Flask, expõe as rotas HTTP.
- `funcoes/`: Pasta com funções separadas para cada operação:
  - `cadastrar.py`: Função para cadastrar pessoa
  - `alterar.py`: Função para alterar cadastro
  - `deletar.py`: Função para deletar pessoa
- `requirements.txt`: Dependências Python
- `Dockerfile`: Configuração para build da imagem Docker

## Como rodar localmente com Docker

1. **Build da imagem:**
   ```powershell
   docker build -t run-lab:latest .
   ```
2. **Executar o container:**
   ```powershell
   docker run -p 8080:8080 run-lab:latest
   ```
3. O serviço estará disponível em http://localhost:8080

## Testando as rotas

### PowerShell (recomendado)

#### Cadastrar pessoa (POST)
```powershell
$body = @{ nome = "João"; idade = 30 } | ConvertTo-Json
Invoke-RestMethod -Uri http://localhost:8080/cadastrar -Method Post -Body $body -ContentType "application/json"
```

#### Alterar cadastro (PUT)
```powershell
$body = @{ nome = "João"; idade = 31 } | ConvertTo-Json
Invoke-RestMethod -Uri http://localhost:8080/alterar -Method Put -Body $body -ContentType "application/json"
```

#### Deletar pessoa (DELETE)
```powershell
$body = @{ nome = "João" } | ConvertTo-Json
Invoke-RestMethod -Uri http://localhost:8080/deletar -Method Delete -Body $body -ContentType "application/json"
```

## Deploy no Google Cloud Run

1. Faça login no Google Cloud:
   ```powershell
   gcloud auth login
   ```
2. Configure o projeto:
   ```powershell
   gcloud config set project SEU_ID_PROJETO
   ```
3. Faça build e push da imagem para o Container Registry:
   ```powershell
   gcloud builds submit --tag gcr.io/SEU_ID_PROJETO/run-lab
   ```
4. Faça o deploy no Cloud Run:
   ```powershell
   gcloud run deploy run-lab --image gcr.io/SEU_ID_PROJETO/run-lab --platform managed --region us-central1 --allow-unauthenticated
   ```

Substitua `SEU_ID_PROJETO` pelo ID do seu projeto no GCP.
