user = {
    'name': 'Carlos',
    'age': '32',
    'email': 'carlos@email.com'
}

if 'telefone' not in user:
    user['telefone'] = 'sem número'

valuecpf = user.get('cpf','Sem CPF cadastrado')
print(valuecpf)