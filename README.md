# Simulacoes-Educativas-Ransomware-e-Keylogger
Este repositório contém apenas simulações educativas e documentação. Nenhum código malicioso real está incluído. Eu executei todos os testes apenas em máquinas virtuais isoladas e com backups. Qualquer uso fora de ambiente autorizado é ilegal e antiético.

O que eu implementei
====================
Eu desenvolvi simuladores seguros para demonstrar conceitos de ransomware e keylogger:
- Simulador de cifragem que opera apenas em arquivos de teste na pasta sandbox/ usando cryptography (Fernet).
- Processador de amostras de teclado que analisa samples/keystrokes.txt em vez de capturar teclas em tempo real.
- Documentação com instrucoes de execucao segura e reflexoes sobre mitigacao.

Conteudo do repositorio
=======================
- scripts/encrypt_demo.py  : simulador de cifragem
- scripts/process_keystrokes.py : processamento de amostras simuladas
- docs/defesa.md : medidas de mitigacao e recomendacoes

Como reproduzir com seguranca
============================
1. Crie uma VM isolada e faça snapshot antes de qualquer teste.
2. Coloque arquivos de teste em sandbox/ com extensao .test.
3. Para cifrar: python3 scripts/encrypt_demo.py --mode encrypt
4. Para decifrar: python3 scripts/encrypt_demo.py --mode decrypt
5. Para analisar entradas simuladas: python3 scripts/process_keystrokes.py samples/keystrokes.txt

Boas praticas e seguranca
=========================
- Nunca executar testes em sistemas de producao.
- Nao publicar chaves, senhas ou logs sensiveis.
- Revogar ou alterar qualquer credencial criada para testes antes de publicar.

Contato e referencias
=====================
Documentacao e bibliotecas de referencia:
- Python official docs
- Cryptography (Fernet)
- pynput (uso estudado, nao publicado)
- smtplib (referencia teorica)
