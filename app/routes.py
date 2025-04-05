from flask import Blueprint, request, jsonify
from app.models import db, Usuario

bp = Blueprint('api', __name__)

# Rota principal
@bp.route('/')
def home():
    return "Olá mundo! A API está funcionando."

# Rota para listar usuários
@bp.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([u.to_dict() for u in usuarios])

# Rota para adicionar usuários
@bp.route('/usuarios', methods=['POST'])
def adicionar_usuario():
    dados = request.get_json()
    novo = Usuario(nome=dados['nome'], email=dados['email'])
    db.session.add(novo)
    db.session.commit()

    return jsonify(novo.to_dict()), 201

# PUT - Atualizar usuário existente
@bp.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    dados = request.get_json()
    usuario = Usuario.query.get(id)

    if usuario is None:
        return jsonify({'erro': 'Usuário não encontrado'}), 404

    usuario.nome = dados.get('nome', usuario.nome)
    usuario.email = dados.get('email', usuario.email)
    db.session.commit()

    return jsonify(usuario.to_dict())

# DELETE - Remover usuário
@bp.route('/usuarios/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    usuario = Usuario.query.get(id)

    if usuario is None:
        return jsonify({'erro': 'Usuário não encontrado'}), 404

    db.session.delete(usuario)
    db.session.commit()

    return jsonify({'mensagem': f'Usuário {id} removido com sucesso'})