# TELEGRAM BOT
A execução da aplicação resulta em um chatbot do Telegram.
Após executar o programa principal, basta acessar a url [FastAPI_URL](https://t.me/ScoreitorBot)

## Comandos
A interação do usuário com o chatbot se dá por meio de comandos e respostas de mensagens com passagem de valores para dados.

### /start
O comando `/start` inicia o chatbot, o qual responde com um menu de opções com os comandos seguintes:

### /create
Executa o comando para inserir um novo usuário:
1. O chatbot envia uma mensagem solicitando que seja digitado o nome do novo usuário;
2. A aplicação armazena a resposta do usuário com o valor 'nome';
3. O chatbot envia uma mensagem solicitando que seja digitada a data de nascimento do novo usuário;
4. A aplicação armazena a resposta do usuário com o valor 'data_nascimento';
5. O chatbot envia uma mensagem solicitando que seja digitado o score do novo usuário;
6. 4. A aplicação armazena a resposta do usuário com o valor 'score';
7. Após todos os valores terem sido passados para a aplicação, os valores são enviados para validação:
    * Caso os valores sejam válidos, o novo usuário é registrado na base de dados e o chatbot envia uma mensagem informando "Usuário cadastrado com sucesso!"
    * Caso algum dos valores seja inválido, o novo usuário não é registrado na base de dados e o chatbot envia uma mensagem informando "Dados inválidos, tente novamente." retornando o chat para o item 1.

### /read
Executa o comando para filtrar os usuários por score:
1. O chatbot envia uma mensagem perguntando se deseja informar um valor para o score:
    * Caso a resposta seja 's':
        * O chatbot envia uma mensagem solicitando um valor para o score;
        * Jump para o intem 2.
    * Caso a resposta seja 'n':
        * O chatbot enviar mensagens com os 50 usuários com maiores scores na base de dados.
2. Após receber a resposta como valor para score:
    * Caso tenham usuários na base de dados com valores para score maiores do que o informado:
        * O chatbot envia mensagens com todos os usuários com score maior do que o digitado.
    Caso não exista usuário com score maior do que o digitado:
        * O chatbot envia uma mensagem informando que não há usuários com score maior que o informado.

## /update
Executa o comando para alterar os dados de um usuário:
1. O chatbot envia uma mensagem solicitando o ID do usuário que deseja alterar;
2. Após receber o ID, o chatbot envia uma mensagem com os dados atuais do usuário com ID digitado;
    * Caso o ID digitado não corresponda há nenhum usuário na base de dados:
        * O chatbot envia uma mensagem informando "Usuário com ID (id) não encontrado.".
3. O chatbot envia uma mensagem solicitando um novo nome para o usuário;
4. Após receber a resposta, a aplicação salva o novo nome na base de dados do usuário;
5. O chatbot envia uma mensagem solicitando uma nova data de nascimento para o usuário;
6. Após receber a resposta, a aplicação salva a nova data de nascimentona base de dados do usuário;
7. O chatbot envia uma mensagem solicitando um novo score para o usuário;
8. Após receber a resposta, a aplicação salva o novo score na base de dados do usuário;
9. O chatbot envia uma mensagem informando "Usuário editado com sucesso!".


## /delete
Executa o comando para excluir os dados de um usuário:
1. O chatbot envia uma mensagem solicitando o ID do usuário que deseja excluir;
2. Após receber o ID, o chatbot envia uma mensagem com os dados atuais do usuário com ID digitado;
    * Caso o ID digitado não corresponda há nenhum usuário na base de dados:
        * O chatbot envia uma mensagem informando "Usuário com ID {id} não encontrado.".
3. O chatbot envia uma mensagem solicitando confirmar a exclusão com "sim" ou cancelar a exclusão com "não":
    * Caso a resposta seja "sim" os dados do usuário são excluídos da base de dados e o chatbot envia uma mensagem informando "Usuário com ID {id} excluído com sucesso.";
    * Caso a resposta seja "não" os dados do usuário são mantidos na base de dados e o chatbot envia uma mensagem informando "Operação cancelada."