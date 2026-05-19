import os

def contar_arquivos_em_train(diretorio_raiz):
    resultados = []

    # percorre todas as pastas dentro de Train
    for pasta in os.listdir(diretorio_raiz):
        caminho_pasta = os.path.join(diretorio_raiz, pasta)

        # garante que é uma pasta (classe)
        if os.path.isdir(caminho_pasta):
            arquivos = [
                f for f in os.listdir(caminho_pasta)
                if os.path.isfile(os.path.join(caminho_pasta, f))
            ]

            resultados.append({
                'classe': pasta,
                'quantidade': len(arquivos)
            })

    return resultados


# uso
resultado = contar_arquivos_em_train('Train')

# imprime bonito
for r in resultado:
    print(f"Classe {r['classe']}: {r['quantidade']} imagens")