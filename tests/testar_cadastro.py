from services.cadastrar import cadastrarUsuario

resultado = cadastrarUsuario(
    "test@gmail.com",
    "123456",
    "Wadisson"
)

print(resultado)