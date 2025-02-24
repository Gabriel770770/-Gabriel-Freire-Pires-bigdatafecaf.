# -Gabriel-Freire-Pires-bigdatafecaf.

# Pipeline de Dados com IoT e PostgreSQL

Este projeto tem como objetivo criar um pipeline de dados que processa leituras de temperatura de dispositivos IoT e armazena essas informações em um banco de dados PostgreSQL. O script Python lê um arquivo CSV contendo as leituras de temperatura e insere os dados em uma tabela no banco de dados.

## Pré-requisitos

Antes de executar o projeto, certifique-se de que você possui os seguintes requisitos instalados:

- **Python 3.8 ou superior**
- **PostgreSQL** (local ou remoto)
- **Bibliotecas Python**: `pandas`, `sqlalchemy`

## Configuração do Ambiente

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```

2. **Crie um ambiente virtual** (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install pandas sqlalchemy
   ```

4. **Configure o banco de dados PostgreSQL**:
   - Crie um banco de dados chamado `database`.
   - Certifique-se de que o PostgreSQL está acessível no endereço `192.168.1.47` na porta `5432`.
   - Crie um usuário com as credenciais fornecidas no script (`user` e `GaaBs7007.`).

5. **Prepare o arquivo CSV**:
   - Coloque o arquivo `temperature_readings.csv` na raiz do projeto. O arquivo deve conter as colunas necessárias para as leituras de temperatura.

## Executando o Script

Para processar o arquivo CSV e inserir os dados no banco de dados, execute o script Python:

```bash
python main.py
```

### O que o Script Faz?

1. **Conecta ao banco de dados PostgreSQL**:
   - Utiliza a biblioteca `sqlalchemy` para criar uma conexão com o banco de dados.

2. **Lê o arquivo CSV**:
   - O arquivo `temperature_readings.csv` é lido usando a biblioteca `pandas`.

3. **Insere os dados no banco de dados**:
   - Os dados são inseridos na tabela `temperature_readings` do banco de dados PostgreSQL. Se a tabela já existir, ela será substituída (`if_exists='replace'`).

## Estrutura do Projeto

```
nome-do-repositorio/
├── main.py                # Script principal para processar e inserir os dados
├── temperature_readings.csv  # Arquivo CSV com as leituras de temperatura
├── README.md              # Documentação do projeto
└── requirements.txt       # Lista de dependências (opcional)
```

## Contribuindo

Contribuições são bem-vindas! Siga os passos abaixo para contribuir:

1. **Faça um fork** do repositório.
2. **Crie uma branch** para sua feature ou correção:
   ```bash
   git checkout -b minha-feature
   ```
3. **Faça commit das suas alterações**:
   ```bash
   git commit -m "Adicionando nova funcionalidade"
   ```
4. **Envie as alterações**:
   ```bash
   git push origin minha-feature
   ```
5. **Abra um Pull Request** no repositório original.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

### Exemplo de `requirements.txt`

Se preferir, você pode criar um arquivo `requirements.txt` para listar as dependências do projeto:

```
pandas==1.5.3
sqlalchemy==1.4.46
```

Para instalar as dependências a partir do arquivo `requirements.txt`, execute:

```bash
pip install -r requirements.txt
```


### 1. **Média de Temperatura por Dispositivo**
```sql
CREATE VIEW avg_temp_por_dispositivo AS
SELECT 
    device_id, 
    AVG(temperature) AS avg_temp
FROM 
    temperature_readings
GROUP BY 
    device_id;
```

#### **Propósito**:
- Esta view calcula a **temperatura média** registrada por cada dispositivo IoT.
- Ela agrupa as leituras de temperatura pelo `device_id` e calcula a média das temperaturas para cada dispositivo.

#### **Utilização**:
- Identificar dispositivos que estão registrando temperaturas médias mais altas ou mais baixas.
- Monitorar o desempenho dos dispositivos ao longo do tempo.
- Detectar anomalias ou problemas em dispositivos específicos (por exemplo, se a temperatura média de um dispositivo estiver fora do esperado).

#### **Exemplo de Insight**:
- Se um dispositivo estiver com uma temperatura média significativamente mais alta que os outros, pode indicar um problema de hardware ou sobrecarga.

---

### 2. **Contagem de Leituras por Hora do Dia**
```sql
CREATE VIEW leituras_por_hora AS
SELECT 
    EXTRACT(HOUR FROM noted_date) AS hora, 
    COUNT(*) AS contagem
FROM 
    temperature_readings
GROUP BY 
    EXTRACT(HOUR FROM noted_date)
ORDER BY 
    hora;
```

#### **Propósito**:
- Esta view conta quantas leituras de temperatura foram feitas em **cada hora do dia**.
- Ela extrai a hora (`HOUR`) da coluna `noted_date` e agrupa as leituras por hora, contando o número de registros em cada grupo.

#### **Utilização**:
- Identificar os **horários de pico** de leituras de temperatura.
- Entender padrões de uso dos dispositivos IoT ao longo do dia.
- Planejar a capacidade de armazenamento e processamento com base na carga de dados.

#### **Exemplo de Insight**:
- Se houver um pico de leituras entre 14h e 16h, pode indicar que os dispositivos estão mais ativos nesse período (por exemplo, devido a maior atividade humana ou ambiental).

---

### 3. **Temperaturas Máximas e Mínimas por Dia**
```sql
CREATE VIEW temp_max_min_por_dia AS
SELECT 
    DATE(noted_date) AS data, 
    MAX(temperature) AS temp_max, 
    MIN(temperature) AS temp_min
FROM 
    temperature_readings
GROUP BY 
    DATE(noted_date)
ORDER BY 
    data;
```

#### **Propósito**:
- Esta view calcula as **temperaturas máximas e mínimas** registradas em **cada dia**.
- Ela agrupa as leituras por dia (usando a função `DATE`) e calcula os valores máximo e mínimo de temperatura para cada dia.

#### **Utilização**:
- Monitorar **variações extremas de temperatura** ao longo dos dias.
- Identificar dias com temperaturas anormalmente altas ou baixas.
- Analisar tendências climáticas ou padrões sazonais.

#### **Exemplo de Insight**:
- Se a temperatura máxima de um dia for muito superior à média histórica, pode indicar um evento climático incomum ou um problema no sistema de medição.

---

### Resumo das Views

| View                     | Propósito                                                                 | Utilização Principal                                                                 |
|--------------------------|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| `avg_temp_por_dispositivo` | Calcular a temperatura média por dispositivo.                             | Monitorar desempenho e detectar anomalias em dispositivos específicos.              |
| `leituras_por_hora`       | Contar o número de leituras por hora do dia.                              | Identificar horários de pico e padrões de uso dos dispositivos.                     |
| `temp_max_min_por_dia`    | Calcular as temperaturas máximas e mínimas por dia.                       | Monitorar variações extremas de temperatura e identificar tendências climáticas.    |

---

### Como Utilizar as Views no Dashboard

Essas views podem ser utilizadas no **dashboard Streamlit** para gerar visualizações interativas. Por exemplo:

1. **Média de Temperatura por Dispositivo**:
   - Gráfico de barras mostrando a temperatura média de cada dispositivo.
   - Identificar dispositivos com temperaturas fora do esperado.

2. **Leituras por Hora do Dia**:
   - Gráfico de linha mostrando a contagem de leituras ao longo do dia.
   - Identificar horários de pico de atividade.

3. **Temperaturas Máximas e Mínimas por Dia**:
   - Gráfico de linha mostrando as temperaturas máximas e mínimas ao longo dos dias.
   - Identificar dias com variações extremas de temperatura.

---

### Exemplo de Código no Streamlit

```python
import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# Conexão com o banco de dados
engine = create_engine('postgresql://user:password@localhost:5432/database')

# Função para carregar dados de uma view
def load_data(view_name):
    return pd.read_sql(f"SELECT * FROM {view_name}", engine)

# Título do dashboard
st.title('Dashboard de Temperaturas IoT')

# Gráfico 1: Média de temperatura por dispositivo
st.header('Média de Temperatura por Dispositivo')
df_avg_temp = load_data('avg_temp_por_dispositivo')
fig1 = px.bar(df_avg_temp, x='device_id', y='avg_temp')
st.plotly_chart(fig1)

# Gráfico 2: Contagem de leituras por hora
st.header('Leituras por Hora do Dia')
df_leituras_hora = load_data('leituras_por_hora')
fig2 = px.line(df_leituras_hora, x='hora', y='contagem')
st.plotly_chart(fig2)

# Gráfico 3: Temperaturas máximas e mínimas por dia
st.header('Temperaturas Máximas e Mínimas por Dia')
df_temp_max_min = load_data('temp_max_min_por_dia')
fig3 = px.line(df_temp_max_min, x='data', y=['temp_max', 'temp_min'])
st.plotly_chart(fig3)
```

---

Essas views fornecem insights valiosos sobre os dados de temperatura, permitindo uma análise mais profunda e visualizações mais ricas no dashboard.
No processo de desenvolvimento deste projeto, vários conceitos e habilidades foram aprendidos e reforçados. Abaixo está um resumo do que foi aprendido:

---

### 1. **Manipulação de Dados com Pandas**
- **Leitura de arquivos CSV**: Aprendemos a carregar dados de um arquivo CSV usando a biblioteca `pandas`.
- **Transformação de dados**: Utilizamos o `pandas` para manipular e preparar os dados antes de inseri-los no banco de dados.
- **Inserção de dados no banco de dados**: Aprendemos a usar o método `to_sql` do `pandas` para inserir dados em uma tabela do PostgreSQL.

---

### 2. **Conexão com Banco de Dados PostgreSQL**
- **Configuração do banco de dados**: Aprendemos a configurar um banco de dados PostgreSQL e a criar uma conexão com ele usando a biblioteca `sqlalchemy`.
- **Execução de comandos SQL**: Utilizamos SQL diretamente no Python para criar views e consultar dados.
- **Gerenciamento de credenciais**: Entendemos a importância de proteger credenciais sensíveis (como usuário e senha do banco de dados) e como usar variáveis de ambiente para gerenciá-las.

---

### 3. **Criação de Views SQL**
- **Agregação de dados**: Aprendemos a usar funções de agregação como `AVG`, `MAX`, `MIN` e `COUNT` para resumir dados.
- **Manipulação de datas**: Utilizamos funções como `EXTRACT` e `DATE` para trabalhar com campos de data e hora.
- **Criação de views**: Entendemos como criar views no PostgreSQL para simplificar consultas e fornecer dados pré-processados para análise.

---

### 4. **Visualização de Dados com Streamlit e Plotly**
- **Criação de dashboards**: Aprendemos a usar o `Streamlit` para criar dashboards interativos.
- **Gráficos interativos**: Utilizamos a biblioteca `Plotly` para criar gráficos dinâmicos e visualmente atraentes.
- **Integração com banco de dados**: Aprendemos a conectar o dashboard ao banco de dados para exibir dados em tempo real.

---

### 5. **Versionamento de Código com Git e GitHub**
- **Comandos básicos do Git**: Aprendemos a usar comandos como `git init`, `git add`, `git commit`, `git push` e `git pull` para gerenciar o versionamento do código.
- **Colaboração no GitHub**: Entendemos como criar repositórios, fazer push de alterações e colaborar em projetos usando o GitHub.

---

### 6. **Deploy e Publicação de Projetos**
- **Preparação para deploy**: Aprendemos a configurar o ambiente e as dependências para publicar o projeto.
- **Uso de serviços como Render**: Entendemos como fazer o deploy de uma aplicação Streamlit usando serviços como o Render.

---

### 7. **Boas Práticas de Programação**
- **Organização do código**: Aprendemos a estruturar o projeto de forma clara e modular.
- **Documentação**: Entendemos a importância de documentar o código e o projeto (por exemplo, com um `README.md`).
- **Tratamento de erros**: Aprendemos a prever e lidar com possíveis erros, como falhas na conexão com o banco de dados.

---

### 8. **Análise de Dados e Insights**
- **Identificação de padrões**: Aprendemos a usar views SQL e visualizações para identificar padrões nos dados, como horários de pico e variações de temperatura.
- **Tomada de decisões com base em dados**: Entendemos como os dados processados podem ser usados para tomar decisões informadas, como detectar anomalias ou planejar a capacidade de armazenamento.

---

### 9. **Trabalho com Containers (Docker)**
- **Configuração de contêineres**: Aprendemos a configurar e executar um contêiner Docker para o PostgreSQL.
- **Isolamento de ambientes**: Entendemos a importância de usar Docker para garantir que o ambiente de desenvolvimento seja consistente e reproduzível.

---

### 10. **Habilidades de Resolução de Problemas**
- **Debugging**: Aprendemos a identificar e corrigir erros no código, como problemas de conexão com o banco de dados ou falhas na execução do script.
- **Pesquisa e aprendizado contínuo**: Desenvolvemos a habilidade de buscar soluções e aprender novas ferramentas e bibliotecas conforme necessário.

---

### Conclusão
Este projeto foi uma oportunidade valiosa para aplicar conceitos teóricos em um cenário prático. Através dele, aprendemos a integrar diferentes tecnologias (Python, PostgreSQL, Docker, Streamlit, etc.) para criar um pipeline de dados funcional e um dashboard interativo. Além disso, reforçamos habilidades essenciais como versionamento de código, documentação e análise de dados. Esses conhecimentos são fundamentais para projetos futuros na área de ciência de dados e engenharia de software.
