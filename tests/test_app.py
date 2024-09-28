from http import HTTPStatus


def test_create_user(client):
    response = client.post(
        '/users',  # UserSchema
        json={
            'username': 'testFeitosa',
            'email': 'testfeit@mail.com',
            'password': 'fake@1234',
        },
    )

    # Voltando os status code correto?
    assert response.status_code == HTTPStatus.CREATED
    # Validar UserPublic
    assert response.json() == {
        'id': 1,
        'username': 'testFeitosa',
        'email': 'testfeit@mail.com',
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'testFeitosa',
                'email': 'testfeit@mail.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'Alice',
            'email': 'alic@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'Alice',
        'email': 'alic@example.com',
        'id': 1,
    }

    # Tenta atualizar um usuário que não existe
    response = client.put(
        '/users/99',  # ID que não existe
        json={
            'username': 'Bob',
            'email': 'bob@example.com',
            'password': 'password',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client):
    # Existem Usuário
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted'}
    # Não existem usuário
    response = client.delete('/users/99')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
