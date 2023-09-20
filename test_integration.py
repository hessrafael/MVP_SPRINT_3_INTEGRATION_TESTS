import json
import requests


class Med1:
    id = None

class Med2:
    id = None

class Sala1:
    id = None

class Sala2:
    id = None

class Paciente1:
    id = None

class Proc1:
    id = None

class Proc2:
    id = None

class Presc1:
    id = None

class Presc2:
    id = None

class Presc3:
    id = None

class Presc4:
    id = None


def create_medicament_1():
    print('criando med1')
    response = requests.post('http://127.0.0.1:5001/medicamento',data={
        "apresentacao": "comprimido",
        "dosagem": 500,
        "unidade_dosagem": "mg",
        "quantidade": 16,
        "marca": "Neosa",
        "principio_ativo": "Dipirona"
    })
    assert response.status_code == 200
    response_data = response.json()
    Med1.id = response_data["id"]

def create_medicament_2():
    print('criando med2')
    response = requests.post('http://127.0.0.1:5001/medicamento',data={
        "apresentacao": "comprimido",
        "dosagem": 500,
        "unidade_dosagem": "mg",
        "quantidade": 20,
        "marca": "Tylenaasol",
        "principio_ativo": "Paracetamol"
    })
    assert response.status_code == 200
    response_data = response.json()
    Med2.id = response_data["id"]

def create_sala_1():
    print('criando Sala1')
    response = requests.post('http://127.0.0.1:5002/sala',data={
        "numero": 1
    })
    assert response.status_code == 200
    response_data = response.json()
    Sala1.id = response_data["id"]

def create_sala_2():
    print('criando Sala2')
    response = requests.post('http://127.0.0.1:5002/sala',data={
        "numero": 2
    })
    assert response.status_code == 200
    response_data = response.json()
    Sala2.id = response_data["id"]

def create_paciente_1():
    print('criando Paciente1')
    response = requests.post('http://127.0.0.1:5000/paciente',data={
        "cep": "90470230",
        "data_nascimento": "31/05/1996",
        "nome": "João Neto",
        "queixa_principal":"Cefaleia",
        "sexo":"M"
    })
    assert response.status_code == 200
    response_data = response.json()
    Paciente1.id = response_data["id"]

def create_proc_1_passado():
    print('criando Procedimento1, no passado')
    response = requests.post('http://127.0.0.1:5002/procedimento',data={
        "description": "xablau",
        "start_time":"15/01/1900 10:00",
        "end_time":"15/01/1900 10:30",
        "room_id":Sala1.id,
        "paciente_id":Paciente1.id
    })
    assert response.status_code == 200
    response_data = response.json()
    Proc1.id = response_data["id"]

def create_proc_2_futuro():
    print('criando Procedimento2, no futuro')
    response = requests.post('http://127.0.0.1:5002/procedimento',data={
        "description": "futuro xablau",
        "start_time":"30/12/2900 10:00",
        "end_time":"30/12/2900 10:30",
        "room_id":Sala1.id,
        "paciente_id":Paciente1.id
    })
    assert response.status_code == 200
    response_data = response.json()
    Proc2.id = response_data["id"]

def create_proc_1_passado_presc_1():
    print('criando Prescricao1, para Proc Passado')
    response = requests.post('http://127.0.0.1:5002/prescricao',data={
        "medicament_id": Med1.id,
        "proceeding_id":Proc1.id,
        "quantity":5
    })
    assert response.status_code == 200
    response_data = response.json()

def create_proc_1_passado_presc_2():
    print('criando Prescricao2, para Proc Passado')
    response = requests.post('http://127.0.0.1:5002/prescricao',data={
        "medicament_id": Med2.id,
        "proceeding_id":Proc1.id,
        "quantity":3
    })
    assert response.status_code == 200
    response_data = response.json()

def create_proc_2_futuro_presc_1():
    print('criando Prescricao2, para Proc Futuro')
    response = requests.post('http://127.0.0.1:5002/prescricao',data={
        "medicament_id": Med1.id,
        "proceeding_id":Proc2.id,
        "quantity":2
    })
    assert response.status_code == 200
    response_data = response.json()

def create_proc_2_futuro_presc_2():
    print('criando Prescricao2, para Proc Futuro')
    response = requests.post('http://127.0.0.1:5002/prescricao',data={
        "medicament_id": Med2.id,
        "proceeding_id":Proc2.id,
        "quantity":4
    })
    assert response.status_code == 200
    response_data = response.json()

def get_med_quantity(id):
    print('Verificando qtdade do Medicamento')
    response = requests.get(f'http://127.0.0.1:5001/medicamento?id={id.id}')
    assert response.status_code == 200
    response_data = response.json()
    return response_data["quantidade"]

def delete_paciente_1():
    print('Deletando o paciente 1')
    response = requests.delete(f'http://127.0.0.1:5000/delete_paciente',data={
        "id":Paciente1.id
    })
    assert response.status_code == 200
    response_data = response.json()

def get_procedimentos_paciente_1():
    response = requests.get(f'http://127.0.0.1:5002/procedimentos_paciente?id={Paciente1.id}')
    assert response.status_code == 200
    response_data = response.json()
    return response_data

def get_prescricoes_medicamento_1():
    print('Recuperando prescricoes associadas ao Medicamento1')
    response = requests.get(f'http://127.0.0.1:5002/prescricao_medicamento?id={Med1.id}')
    assert response.status_code == 200
    response_data = response.json()
    return response_data

def delete_medicamento_1():
    print('Deletando Medicamento1')
    response = requests.delete(f'http://127.0.0.1:5001/delete_medicamento',data={
        "id":Med1.id
    })
    assert response.status_code == 200
    response_data = response.json()
    return response_data

def test_create_medicament():
    response = requests.post('http://127.0.0.1:5001/medicamento',data={
        "apresentacao": "comprimido",
        "dosagem": 500,
        "unidade_dosagem": "mg",
        "quantidade": 16,
        "marca": "Neosa",
        "principio_ativo": "Dipirona"
    })
    assert response.status_code == 200

print('---------------------------INICIO DO TESTE-------------------------------------')

create_medicament_1()
create_medicament_2()

create_sala_1()
create_sala_2()

create_paciente_1()

create_proc_1_passado()
create_proc_2_futuro()

val = get_med_quantity(Med1)
assert val == 16
print(f'qtdade med1 = {val}')
val = get_med_quantity(Med2)
assert val == 20
print(f'qtdade med2 = {val}')

create_proc_1_passado_presc_1()

val = get_med_quantity(Med1)
assert val == 11
print(f'qtdade med1 = {val}')
val = get_med_quantity(Med2)
assert val == 20
print(f'qtdade med2 = {val}')

create_proc_1_passado_presc_2()

val = get_med_quantity(Med1)
assert val == 11
print(f'qtdade med1 = {val}')
val = get_med_quantity(Med2)
assert val == 17
print(f'qtdade med2 = {val}')

create_proc_2_futuro_presc_1()

val = get_med_quantity(Med1)
assert val == 9
print(f'qtdade med1 = {val}')
val = get_med_quantity(Med2)
assert val == 17
print(f'qtdade med2 = {val}')

create_proc_2_futuro_presc_2()

val = get_med_quantity(Med1)
assert val == 9
print(f'qtdade med1 = {val}')
val = get_med_quantity(Med2)
assert val == 13
print(f'qtdade med2 = {val}')

ans = get_procedimentos_paciente_1()
assert len(ans["procedimentos"]) == 2
print(f'\n Procedimentos antes da delecao do paciente: {ans}')


delete_paciente_1()

ans = get_procedimentos_paciente_1()
assert len(ans["procedimentos"]) == 1
print(f'\n Procedimentos apos delecao do paciente: {ans}')

val = get_med_quantity(Med1)
assert val == 11
print(f'qtdade med1 = {val}')
val = get_med_quantity(Med2)
assert val == 17
print(f'qtdade med2 = {val}')


print('---Testando Deleção de Medicamento e deleção das prescricoes do futuro associadas')
create_paciente_1()
create_proc_2_futuro()
create_proc_2_futuro_presc_1()

val = get_med_quantity(Med1)
assert val == 9
print(f'qtdade med1 = {val}')
val = get_med_quantity(Med2)
assert val == 17
print(f'qtdade med2 = {val}')

ans = get_prescricoes_medicamento_1()
assert len(ans["prescricoes"]) == 2
print(f'\n Prescricoes antes delecao do medicamento: {ans}')


ans = delete_medicamento_1()
assert ans["quantidade"] == 11

ans = get_prescricoes_medicamento_1()
assert len(ans["prescricoes"]) == 1
print(f'\n Prescricoes apos delecao do medicamento: {ans}')

print('---------------------------FIM DO TESTE-------------------------------------')