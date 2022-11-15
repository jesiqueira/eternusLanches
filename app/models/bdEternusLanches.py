from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin


entregaUsers = db.Table(
    'entregaUsers',
    db.Column('idEntrega', db.Integer, db.ForeignKey('Entregas.id')),
    db.Column('idUsers', db.Integer, db.ForeignKey('Users.id'))
)

pedidoUsers = db.Table(
    'pedidoUsers',
    db.Column('idPedido', db.Integer, db.ForeignKey('Pedidos.id')),
    db.Column('idUsers', db.Integer, db.ForeignKey('Users.id'))
)

enderecoUsers = db.Table(
    'enderecoUsers',
    db.Column('idUsers', db.Integer, db.ForeignKey('Users.id')),
    db.Column('idEndereco', db.Integer, db.ForeignKey('Enderecos.id'))
)

acessoUsers = db.Table(
    'acessoUsers',
    db.Column('idUsers', db.Integer, db.ForeignKey('Users.id')),
    db.Column('idAcesso', db.Integer, db.ForeignKey('Acessos.id'))
)

pedidoLanches = db.Table(
    'pedidoLanches',
    db.Column('idLanche', db.Integer, db.ForeignKey('Lanches.id')),
    db.Column('idPedido', db.Integer, db.ForeignKey('Pedidos.id'))
)

pedidoPorcoes = db.Table(
    'pedidoPorcoes',
    db.Column('idPorcao', db.Integer, db.ForeignKey('Porcoes.id')),
    db.Column('idPedido', db.Integer, db.ForeignKey('Pedidos.id'))
)

pedidoBebidas = db.Table(
    'pedidoBebidas',
    db.Column('idBebida', db.Integer, db.ForeignKey('Bebidas.id')),
    db.Column('idPedido', db.Integer, db.ForeignKey('Pedidos.id'))
)


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Lanches(db.Model):
    __tablename__ = 'Lanches'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), unique=True, nullable=True)
    valor = db.Column(db.Float, nullable=False)
    ingrediente = db.Column(db.String(150), nullable=False)
    img = db.Column(db.String(20), nullable=False, default='default.jpg')

    def __init__(self, nome='', valor=0.00, ingrediente='....', img='') -> None:
        self.nome = nome
        self.valor = valor
        self.ingrediente = ingrediente
        self.img = img

    def __repr__(self) -> str:
        return f"Lanches('{self.nome}', '{self.valor}', '{self.ingrediente}', '{self.img}')"


class Porcoes(db.Model):
    __tablename__ = 'Porcoes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), unique=True, nullable=True)
    valor = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.String(150), nullable=False)
    img = db.Column(db.String(20), nullable=False, default='default.jpg')

    def __init__(self, nome='', valor=0.00, descricao='....', img='') -> None:
        self.nome = nome
        self.valor = valor
        self.descricao = descricao
        self.img = img

    def __repr__(self) -> str:
        return f"Lanches('{self.nome}', '{self.valor}', '{self.descricao}', '{self.img}')"


class Bebidas(db.Model):
    __tablename__ = 'Bebidas'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), unique=True, nullable=True)
    valor = db.Column(db.Float, nullable=False)
    alcoolica = db.Column(db.Boolean, nullable=False)
    img = db.Column(db.String(20), nullable=False, default='default.jpg')

    def __init__(self, nome='', valor=0.00, alcoolica=False, img='') -> None:
        self.nome = nome
        self.valor = valor
        self.alcoolica = alcoolica
        self.img = img

    def __repr__(self) -> str:
        return f"Lanches('{self.nome}', '{self.valor}', '{self.alcoolica}', '{self.img}')"


class Mesas(db.Model):
    __tablename__ = 'Mesas'
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, unique=True, nullable=False)
    livre = db.Column(db.Boolean, nullable=False, default=True)

    pedidos = db.relationship('Pedidos', backref='mesas', lazy=True)

    def __init__(self, numero=0, livre=True) -> None:
        self.numero = numero
        self.livre = livre

    def __repr__(self) -> str:
        return f"Mesas('{self.numero}', '{self.livre}')"


class Pedidos(db.Model):
    __tablename__ = 'Pedidos'
    id = db.Column(db.Integer, primary_key=True)
    dataHora = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    codPedido = db.Column(db.String(15), nullable=False, unique=True)
    idMesa = db.Column(db.Integer, db.ForeignKey('Mesas.id'), nullable=False)

    entrega = db.relationship('Entregas', backref='pedidos', lazy=True)
    user = db.relationship('Users', secondary=pedidoUsers, backref='pedidos')
    lanche = db.relationship(
        'Lanches', secondary=pedidoLanches, backref='pedidos')
    porcao = db.relationship(
        'Porcoes', secondary=pedidoPorcoes, backref='pedidos')
    bebida = db.relationship(
        'Bebidas', secondary=pedidoBebidas, backref='pedidos')

    def __init__(self, dataHora=datetime.utcnow, codPedido='ET0123456789', idMesa=0) -> None:
        self.dataHora = dataHora
        self.codPedido = codPedido
        self.idMesa = idMesa

    def __repr__(self) -> str:
        return f"Pedidos('{self.dataHora}', '{self.codPedido}')"


class Entregas(db.Model):
    __tablename__ = 'Entregas'
    id = db.Column(db.Integer, primary_key=True)
    taxaEntrega = db.Column(db.Float)
    idPedido = db.Column(db.Integer, db.ForeignKey(
        'Pedidos.id'), nullable=False)
    user = db.relationship('Users', secondary=entregaUsers, backref='entregas')

    def __init__(self, taxaEntrega=0.00, idPedido=0, user=[]) -> None:
        self.taxaEntrega = taxaEntrega
        self.idPedido = idPedido
        self.user = user

    def __repr__(self) -> str:
        return f"Entregas('{self.taxaEntrega}')"


class Users(db.Model, UserMixin):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(60), unique=True, nullable=False)

    endereco = db.relationship(
        'Enderecos', secondary=enderecoUsers, backref='users')
    acesso = db.relationship('Acessos', secondary=acessoUsers, backref='users')

    def __init__(self, nome='', email='', password='', endereco=[], acesso=[]) -> None:
        self.nome = nome
        self.email = email
        self.password = password
        self.endereco = endereco
        self.acesso = acesso

    def __repr__(self) -> str:
        return f"Users('{self.nome}', '{self.email}')"


class Telefones(db.Model):
    __tablename__ = 'Telefones'
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, nullable=False, unique=True)

    def __init__(self, numero=0) -> None:
        self.numero = numero

    def __repr__(self) -> str:
        return f"Telefone('{self.numero}')"


class Acessos(db.Model):
    __tablename__ = 'Acessos'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(15), nullable=False, unique=True)

    def __init__(self, tipo='') -> None:
        self.tipo = tipo

    def __repr__(self) -> str:
        return f"Acessos('{self.tipo}')"


class Enderecos(db.Model):
    __tablename__ = 'Enderecos'
    id = db.Column(db.Integer, primary_key=True)
    rua = db.Column(db.String(40), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    cidade = db.Column(db.String(40), nullable=False)
    bairro = db.Column(db.String(40), nullable=False)
    cep = db.Column(db.String(14), nullable=False)
    principal = db.Column(db.Boolean, nullable=False)

    def __init__(self, rua='', numero=0, cidade='', bairro='', cep='', principal=True) -> None:
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
        self.bairro = bairro
        self.cep = cep
        self.principal = principal

    def __repr__(self) -> str:
        return f"Endereco('{self.rua}', '{self.numero}', '{self.cidade}', '{self.bairro}', '{self.cep}', '{self.principal}')"
