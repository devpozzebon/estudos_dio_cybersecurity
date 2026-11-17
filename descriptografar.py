from cryptography.fernet import Fernet
import os


def carregar_chave():
    with open("chave.key", "rb") as chave_file:
        return chave_file.read()


def descriptografar_arquivo(arquivo, chave):
    f = Fernet(chave)

    with open(arquivo, "rb") as file:
        dados = file.read()

    try:
        dados_descriptografados = f.decrypt(dados)
    except Exception as e:
        print(f"[!] Falha ao descriptografar {arquivo}: {e}")
        return

    with open(arquivo, "wb") as file:
        file.write(dados_descriptografados)


def encontrar_arquivos(diretorio):
    lista = []
    script_atual = os.path.abspath(__file__)

    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)

            # Não processa o próprio script
            if os.path.abspath(caminho) == script_atual:
                continue

            # Não processa a chave nem o próprio ransomware.py
            if nome == "ransomware.py" or nome.endswith(".key"):
                continue

            lista.append(caminho)

    return lista


def main():
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")

    for arquivo in arquivos:
        descriptografar_arquivo(arquivo, chave)

    print("Arquivos restaurados com sucesso")


if __name__ == "__main__":
    main()