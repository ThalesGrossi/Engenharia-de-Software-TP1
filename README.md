# Engenharia-de-Software-TP1
Trabálho Prático 1 da disciplina de Engenharia de Software da UFMG

## Descrição do projeto

O objetivo do sistema é criar um fórum simples de perguntas e respostas para situações de vida universitária, onde usuários podem postar novas perguntas e respostas para dúvidas em relação a alguma universidade ou curso em particular, e outros usuários podem responder essas perguntas. Essas perguntas e respostas são rankeadas no site de acordo com votos dos usuários sobre a qualidade das perguntas e respostas.

## Integrantes
 - Luiz Augusto Facury de Souza - 2018072484
 - Silvio Natã Rocha Porto - 2018020603
 - Thales Pantuzo Grossi - 2014129660
 - Tiago Rezende Valadares - 2016027562

## Features
 - Postar perguntas
 - Postar respostas
 - Votar na qualidade de uma pergunta ou resposta
 - Se cadastrar como usário

## Tecnologias
 - front: React.js
 - back: Django
 - BD: MySQL

## Histórias de Usuário
 - Como usuário normal, gostaria de postar pergunta no fórum
 
   - Projetar e testar interface web [Silvio]
   - Implementar interface web [Tiago]
   - Criar e testar rota para cada tópico [Thales]
   
 - Como usuário normal, gostaria de postar resposta no fórum
 
   - Projetar e testar interface web [Luiz]
   - Implementar interface web [Silvio]
   - Criar e testar rota para cada tópico [Tiago]
   - Criar e testar rota para associar resposta a um comentário [Thales]
   
 - Como usuário normal, gostaria de me cadastrar na plataforma e fazer login
 
   - Projetar e testar interface web [Luiz]
   - Implementar interface web [Silvio]
   - Criar e testar validação e senha [Tiago]
   - Criar e testar recuperação e mudança de senha [Luiz]
   
 - Como usuário normal, gostaria de votar na qualidade da resposta
 
   - Projetar e testar interface web [Thales]
   - Implementar interface web [Luiz]
   - Criar e testar contador de votos para cada pergunta e resposta [Tiago]
   - Criar classificador das perguntas e respostas [Luiz]
   
 - Como usuário normal, gostaria de apagar e editar meu próprio post
 
   - Projetar e testar interface web [Thales]
   - Implementar interface web [Thales]
   - Criar e testar rota para deletar post [Tiago]
   - Criar e testar rota para editar post [Silvio]
   
 - Como moderador, gostaria de deletar posts de outros usuários
 
   - Implementar usuário especial moderador com botão de deletar condicional [Thales]
   
 - Como usuário, gostaria de buscar um post por palavra-chave em pergunta ou resposta 
   - Projetar e testar interface web [Silvio]
   - Implementar interface web [Silvio]
   - Criar e testar filtro de busca [Tiago]
   - Criar e testar rota de busca [Luiz]
