# Script para testes de integração

Este projeto visa a construção de um script para realizar o teste de integração entre os 3 microsserviços desenvolvidos na Sprint 3 da Pós de Eng. de Software da PUC-Rio

## Como executar

Tenha os 3 microsserviços rodando conforme as instruções de cada README

https://github.com/hessrafael/MVP_RAFAEL_HESS_PACIENTES
https://github.com/hessrafael/MVP_RAFAEL_HESS_MEDICAMENTOS
https://github.com/hessrafael/MVP_RAFAEL_HESS_PROCEDIMENTOS

**IMPORTANTE**: os testes são realizados no banco de dados de execução nomeado 'db.sqlite3'. Utilize um banco de dados virgem para os testes rodarem com sucesso. Caso não queira perder os seus dados, basta renomear o banco de dados 'db.sqlite3' para outro nome e então rodar os testes. Após a execução, é só apagar o 'db.sqlite3' criado durante o teste e alterar o nome do banco de produção de volta para 'db.sqlite3'

Uma vez os serviços de pé, basta ir na pasta raiz e executar:

```
$ python test_integration.py
```

O teste irá realizar uma série de 'asserts' e terá sido aprovado se não ocorrer nenhuma exceção se chegar na mensagem "-----FIM DO TESTE------".