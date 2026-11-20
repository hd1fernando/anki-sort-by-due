# Sort Decks by Column

Complemento para o Anki que permite ordenar os baralhos na tela inicial clicando no cabeçalho de uma coluna. Funciona com **Baralho**, **Novo**, **Aprender** e **Revisar**, em qualquer idioma, pois a coluna é identificada pela posição, não pelo texto.

## Instalação

1. Baixe o arquivo `.ankiaddon` na aba [Releases](https://github.com/hd1fernando/anki-sort-by-due/releases).
2. Abra o arquivo baixado (duplo clique) ou use **Ferramentas → Complementos → Instalar do arquivo...**.
3. Reinicie o Anki.

## Uso

Clique no cabeçalho da coluna desejada:

- **1º clique:** ordem crescente (`▲`);
- **clique na mesma coluna:** inverte para decrescente (`▼`);
- **clique em outra coluna:** volta à ordem crescente.

Baralhos filhos acompanham o baralho pai, preservando a hierarquia. A última coluna e direção são reaplicadas quando a tela é atualizada (se `remember_last_sort` estiver ativo).

A ordenação é apenas visual: ela não altera a ordem real de estudo nem os dados da coleção.

## Compatibilidade

- Anki Desktop 2.1.50 ou superior, incluindo as versões 25.x e 26.x.
- Testado no Anki 26.09.4.

## Configurações

Acesse **Ferramentas → Complementos → Sort Decks by Column → Editar...**:

| Opção | Padrão | Descrição |
| --- | --- | --- |
| `enabled` | `true` | Ativa ou desativa o complemento. |
| `show_indicator` | `true` | Exibe `▲`/`▼` no cabeçalho usado. |
| `remember_last_sort` | `true` | Reaplica a última ordenação após cada renderização. |

## Desenvolvimento

```bash
python3 scripts/build.py
```

O comando gera `dist/sort_by_due-1.0.0.ankiaddon` com o conteúdo da pasta `addon/` na raiz do arquivo. Para testar localmente, extraia o conteúdo da pasta `addon/` em `addons21/sort_by_due/` e reinicie o Anki.

## Licença

MIT — veja [LICENSE](LICENSE).
