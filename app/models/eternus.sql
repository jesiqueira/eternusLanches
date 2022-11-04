-- SELECT * FROM Acessos
-- SELECT * FROM Users
SELECT Users.nome, Acessos.tipo FROM Users JOIN acessoUsers on acessoUsers.idUsers = Users.id JOIN Acessos ON Acessos.id=acessoUsers.idAcesso