# Microatividade 6: Funções com Argumentos

# Definindo uma função chamada loginUsuario que recebe um parâmetro chamado perfil
def loginUsuario(perfil):
    # Verificando se o valor do parâmetro perfil é igual a 'admin' (considerando maiúsculas e minúsculas)
    if perfil.lower() == 'admin':
        print("Bem-vindo, Administrador")
    else:
        print("Bem-vindo, Usuário")

# Chamando a função com diferentes valores
loginUsuario('Admin')
loginUsuario('admin')
loginUsuario('User')
loginUsuario('usuário')
