# Static Site Generator

Um gerador de sites estáticos robusto desenvolvido em Python, projetado para converter arquivos Markdown em páginas HTML completas. Este projeto é parte fundamental da trilha de desenvolvimento backend da [Boot.dev](https://www.boot.dev/courses/build-static-site-generator-python).

## Tecnologias e Ferramentas

- **Linguagem:** [Python 3](https://www.python.org/)
- **Testes:** `Unittest` (Biblioteca nativa do Python)
- **Automação:** Scripts Bash (`.sh`) para CI/CD local
- **Processamento:** Expressões Regulares (Regex) para parsing de Markdown

## Funcionalidades Principais

- **Abstração de Nós (DOM-like):**
    - `HTMLNode`: Classe base para todos os elementos HTML.
    - `LeafNode`: Representa elementos finais sem filhos (ex: `<p>`, `<b>`, `<img>`).
    - `ParentNode`: Gerencia o aninhamento de elementos, permitindo estruturas complexas.
- **Processamento de Markdown Inline:**
    - Conversão automática de **Negrito**, *Itálico*, `Código`, Links e Imagens.
    - Extrator de links e imagens baseado em Regex de alta precisão.
- **Conversão de Árvore de Documento:** Sistema recursivo para transformar objetos Python em strings HTML prontas para o navegador.

## Metodologia de Desenvolvimento

O projeto foi construído com foco em **Qualidade de Software** e **Manutenibilidade**:

1.  **TDD (Test-Driven Development):** Cada funcionalidade de parsing e conversão foi precedida por testes unitários exaustivos (encontrados em `src/test_*.py`).
2.  **Desenvolvimento Incremental:** Seguindo a estrutura da Boot.dev, o progresso foi registrado commit a commit, referenciando capítulos (CH) e lições (L).
3.  **Clean Code:** Utilização de Enums (`TextType`), Casamento de Padrões (`match/case`) e princípios de POO para garantir um código legível e extensível.

## Estrutura do Repositório

```text
├── src/
│   ├── main.py                # Ponto de entrada da aplicação
│   ├── htmlnode.py            # Classes base para representação HTML
│   ├── textnode.py            # Representação de elementos Markdown
│   ├── splits_nodes.py        # Lógica de parsing de texto
│   ├── extract_markdown.py    # Utilitários de Regex
│   └── test_*.py              # Suíte completa de testes unitários
├── main.sh                    # Script de execução
└── test.sh                    # Script de execução de testes
```

## Como Utilizar

### Pré-requisitos
Certifique-se de ter o Python 3 instalado em sua máquina.

### Executando o Projeto
Para iniciar o gerador:
```bash
./main.sh
```

### Rodando os Testes
Para garantir a integridade do sistema:
```bash
./test.sh
```

---
*Desenvolvido por [Kaique S Silva](https://github.com/Kaique-S-Silva) como portfólio de engenharia de software.*
