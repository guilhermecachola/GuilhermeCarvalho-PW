# Making Of - Diário de Bordo do Portfólio
Este documento detalha o processo de conceção, modelação e desenvolvimento da aplicação de Portfólio, registando a evolução do projeto e as decisões técnicas tomadas.

## 1. Modelação de Dados (DER)

### 1.1. Versão Inicial (v1)
A primeira abordagem focou-se nas entidades básicas: `Licenciatura`, `UnidadeCurricular`, `Docente` e `Projeto`.
- **Fotografia do DER:** ![DER Versão 1](media/makingof/der_v1.png)
- **Apontamentos:** Inicialmente, não tínhamos considerado a necessidade de distinguir entre projetos académicos e projetos pessoais ou TFCs.

### 1.2. Evolução (v2 - Integração com API Lusófona)
Após explorar as APIs da Lusófona, o modelo foi expandido para incluir campos técnicos detalhados e a entidade `TFC`.
- **Fotografia do DER:** ![DER Versão Final](media/makingof/der_vfinal.png)
- **Apontamentos:** Adição de campos como `ects`, `objetivos` e `conteudos` para alinhar com os dados oficiais.

---

## 2. Justificação das Decisões de Modelação

### Entidade: Licenciatura
1.  **Justificação 1:** Inclusão do campo `apresentacao` e `objetivos` para permitir que o portfólio funcione como um guia curricular completo e não apenas uma lista de nomes.
2.  **Justificação 2:** Relacionamento `1-para-N` com `UnidadeCurricular`, pois uma disciplina pertence obrigatoriamente a um plano de estudos específico.

### Entidade: UnidadeCurricular (UC)
1.  **Justificação 1:** Criação do campo `codigo` (ReadableCode da API) como chave de sincronização para evitar a criação de duplicados ao importar dados externos.
2.  **Justificação 2:** Separação dos campos `objetivos` e `conteudos` para manter a estrutura fiel à ficha de unidade curricular (FUC) oficial.

### Entidade: Projeto
1.  **Justificação 1:** Relacionamento `Muitos-para-Muitos` com `Tecnologia`, permitindo filtrar projetos por linguagens de programação ou frameworks (ex: todos os projetos feitos em Python).
2.  **Justificação 2:** Campo `link_github` obrigatório para promover a transparência do código e facilitar a avaliação por parte de recrutadores.

### Entidade: TFC (Trabalho de Fim de Curso)
1.  **Justificação 1:** Entidade separada de `Projeto` devido à sua natureza crítica (exige `orientadores` e `rating` específico).
2.  **Justificação 2:** Atributo `ano` para permitir a organização cronológica de projetos de final de curso no portfólio.

---

## 3. Diário de Bordo: Erros e Correções

| Data | Erro Identificado | Causa | Correção / Solução |
| :--- | :--- | :--- | :--- |
| 10/04/2026 | `ModuleNotFoundError: No module named 'config'` | Execução de scripts fora da raiz do projeto. | Adição do `sys.path.append` no script para localizar o `settings.py`. |
| 11/04/2026 | `NameError: name 'requests' is not defined` | Falta de importação da biblioteca no script de automação. | Adição de `import requests` no topo do ficheiro. |
| 12/04/2026 | `ConnectTimeoutError` na API Lusófona | Bloqueio de rede ou latência no servidor da universidade. | Implementação de `timeout=30` e criação de ficheiro JSON local para simular os dados. |
| 13/04/2026 | Dados do Admin sem formatação | Ausência de configuração no `admin.py`. | Uso de `list_display` e `list_filter` para tornar a gestão de dados profissional. |

---

## 4. Reflexão Crítica
O processo de modelação revelou-se dinâmico. A maior dificuldade foi garantir que a base de dados fosse suficientemente flexível para aceitar tanto dados manuais (projetos próprios) como dados automáticos (API). A decisão de usar `update_or_create` nos scripts de importação foi vital para manter a integridade dos dados sem apagar o progresso manual.
