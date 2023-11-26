# FASTAPI
A execução da aplicação resulta em uma aplicação no browser.
Após executar o programa principal, basta acessar a url [FastAPI_URL](http://127.0.0.1:8000/docs#)

## Create
### create_user:
Executa o copando para inserir um novo usuário:
1. Clicar no botão "Try it out";
2. Alterar os valores padrão do _dict_;
3. Clicar no botão "Execute";
4. Validação de dados:
> * Caso os dados sejam válidos, a mensagem de "Usuário criado com sucesso!" será exibida no campo "Responses" e os dados do novo usuário serão armazenados no banco de dados.
> * Caso algum dos dados seja inválido, o campo "Response" irá apresentar uma mensagem com o(s) dado(s) inválido(s) e o novo usuário não será registrado no banco de dados.
### add_users:
Executa o copando para inserir vários usuários:
1. Clicar no botão "Try it out";
2. Alterar os valores padrão da _list_ inserindo vários _dict_ com os dados dos novos usuários;
3. Clicar no botão "Execute";
4. Validação de dados:
4.1 Caso os dados sejam válidos, a mensagem de "Usuários adicionados com sucesso!" será exibida no campo "Responses" e os dados dos novos usuários serão armazenados no banco de dados.
4.2 Caso algum dos dados seja inválido, o campo "Response" irá apresentar uma mensagem com o(s) dado(s) inválido(s) e os novos usuários não serão registrados no banco de dados.

## Read
### get_users_by_score:
Executa o comando para filtrar usuários pelo score:
1. Clicar no botão "Try it out";
2. Escolha do score para filtro:
2.1 Caso seja dado um valor no campo X, o filtro será baseado nesse valor;
2.2 Caso não seja dado nenhum valor para X, o filtro apresentará os 50 usuários com maiores scores;
3. Clicar no botão "Execute";
4. No campo "Response" irá aparecer o resultado com base no critério do item 2.

## Update
### edit_user:
Executa o comando para alterar os dados de um usuário:
1. Clicar no botão "Try it out";
2. Alterar os valores padrão do _dict_:
2.1 Necessário preencher corretamente o número do ID do usuário a ser editado.
3. Clicar no botão "Execute";
4. Validação de dados:
4.1 Caso os dados sejam válidos, a mensagem de "Usuário com ID {id} editado com sucesso!" será exibida no campo "Responses" e os dados do usuário serão alterados no banco de dados.
4.2 Caso algum dos dados seja inválido, o campo "Response" irá apresentar uma mensagem com o(s) dado(s) inválido(s) e o usuário não será alterado no banco de dados.

## Delete
### delete_user:
Executa o comando para excluir os dados de um usuário:
1. Clicar no botão "Try it out";
2. Alterar o ID no _dict_:
3. Clicar no botão "Execute";
4. O browser irá apresentar uma tela de "loading" enquanto uma pergunta será feita no terminal para confirmar ou cancelar a exclusão do usuário:
4.1 Caso digitar "s" no terminal, o usuário será excluído e a mensagem de "Usuário com ID {id} excluído com sucesso!" será apresentada no campo "Response" do browser.
4.2 Caso digitar "n" no terminal, a operação de exclusão será cancelada e uma mensagem de "Operação de exclusão cancelada." será apresentada no campo "Response" do browser.