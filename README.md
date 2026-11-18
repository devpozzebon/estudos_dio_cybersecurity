# estudos_dio_cybersecurity
estudos de criptografia em um ambiente controlado

# Estudo de Criptografia: Simulação de Ransomware (Desafio DIO)

![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Cybersecurity](https://img.shields.io/badge/Area-Cybersecurity-red)

## AVISO LEGAL (DISCLAIMER)

**Este projeto foi desenvolvido EXCLUSIVAMENTE para fins educacionais.** 

O código aqui presente faz parte de um desafio prático do bootcamp de Cibersegurança da [DIO (Digital Innovation One)](https://www.dio.me/). O objetivo é compreender o funcionamento lógico de malwares do tipo Ransomware (criptografia de arquivos) e como criar a sua respectiva ferramenta de defesa (descriptografia).

**Este projeto NÃO deve ser utilizado para atividades maliciosas, ataques ou danos a sistemas de terceiros.** O autor não se responsabiliza por qualquer uso indevido deste material.

## Sobre o Projeto

Este repositório contém dois scripts em Python que demonstram a mecânica básica de um ataque de ransomware e sua subsequente recuperação de dados:

1. **`ransoware.py` (Simulação de Ataque):** Gera uma chave criptográfica simétrica e varre um diretório alvo (`test_files`), criptografando todos os arquivos encontrados (exceto o próprio script e a chave).
2. **`descriptografar.py` (Defesa/Recuperação):** Utiliza a chave gerada anteriormente para reverter o processo, restaurando os arquivos originais.

A biblioteca utilizada para a criptografia de ponta a ponta é a `cryptography`, através do módulo `Fernet` (que utiliza criptografia AES de 128 bits em modo CBC).

## Tecnologias e Ferramentas Utilizadas

* **Python 3** (Linguagem base do projeto)
* **Biblioteca `cryptography`** (Para as operações de criptografia e descriptografia)
* **Biblioteca `os`** (Para manipulação de diretórios e arquivos)
* **Git e GitHub** (Para versionamento e segurança do código)

## Como Executar o Projeto com Segurança

**IMPORTANTE:** Nunca execute scripts de criptografia em pastas reais do seu computador. Recomenda-se o uso de uma Máquina Virtual (VM) ou, no mínimo, de uma pasta isolada com arquivos fictícios.

**Nota:** Leia o [Relatório de Defesa e Reflexão](RELATORIO_DEFESA.md) completo.

### Pré-requisitos
1. Ter o Python instalado.
2. Instalar a biblioteca de criptografia. No terminal, execute:
   ```bash
   pip install cryptography
