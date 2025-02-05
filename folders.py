import os

for i in range(1,9):
    os.mkdir(f"TPC{i}")
    os.chdir(f"./TPC{i}")
    with open("README.md", "w") as readme:
        readme.write(f"""# TPC{i}

## Metadata

| Title | Date | AuthorId | AuthorName | UcSigla | UcNome |
|:-----:|:----:|:--------:|:----------:|:-------:|:------:|
| TPC{i} | | PG55920 | Afonso Silva | SPLN | Scripting no Processamento de Linguagem Natural |

## Resumo

-
-
-

## Resultados

""")
    os.chdir("..")
