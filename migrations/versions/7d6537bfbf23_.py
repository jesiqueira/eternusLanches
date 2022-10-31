"""empty message

Revision ID: 7d6537bfbf23
Revises: 
Create Date: 2022-10-30 21:26:09.623758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d6537bfbf23'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Acessos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipo', sa.String(length=15), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('tipo')
    )
    op.create_table('Enderecos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rua', sa.String(length=40), nullable=False),
    sa.Column('numero', sa.Integer(), nullable=False),
    sa.Column('cidade', sa.String(length=40), nullable=False),
    sa.Column('bairro', sa.String(length=40), nullable=False),
    sa.Column('cep', sa.String(length=14), nullable=False),
    sa.Column('principal', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Lanches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=40), nullable=True),
    sa.Column('valor', sa.Float(), nullable=False),
    sa.Column('ingrediente', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nome')
    )
    op.create_table('Mesas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('numero', sa.Integer(), nullable=False),
    sa.Column('livre', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('numero')
    )
    op.create_table('Telefones',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('numero', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('numero')
    )
    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=40), nullable=False),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('nome'),
    sa.UniqueConstraint('password')
    )
    op.create_table('Pedidos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dataHora', sa.DateTime(), nullable=False),
    sa.Column('codPedido', sa.String(length=15), nullable=False),
    sa.Column('idMesa', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['idMesa'], ['Mesas.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('codPedido')
    )
    op.create_table('acessoUsers',
    sa.Column('idUsers', sa.Integer(), nullable=True),
    sa.Column('idAcesso', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['idAcesso'], ['Acessos.id'], ),
    sa.ForeignKeyConstraint(['idUsers'], ['Users.id'], )
    )
    op.create_table('enderecoUsers',
    sa.Column('idUsers', sa.Integer(), nullable=True),
    sa.Column('idEndereco', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['idEndereco'], ['Enderecos.id'], ),
    sa.ForeignKeyConstraint(['idUsers'], ['Users.id'], )
    )
    op.create_table('Entregas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('taxaEntrega', sa.Float(), nullable=True),
    sa.Column('idPedido', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['idPedido'], ['Pedidos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pedidoLanches',
    sa.Column('idLanche', sa.Integer(), nullable=True),
    sa.Column('idPedido', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['idLanche'], ['Lanches.id'], ),
    sa.ForeignKeyConstraint(['idPedido'], ['Pedidos.id'], )
    )
    op.create_table('pedidoUsers',
    sa.Column('idPedido', sa.Integer(), nullable=True),
    sa.Column('idUsers', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['idPedido'], ['Pedidos.id'], ),
    sa.ForeignKeyConstraint(['idUsers'], ['Users.id'], )
    )
    op.create_table('entregaUsers',
    sa.Column('idEntrega', sa.Integer(), nullable=True),
    sa.Column('idUsers', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['idEntrega'], ['Entregas.id'], ),
    sa.ForeignKeyConstraint(['idUsers'], ['Users.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('entregaUsers')
    op.drop_table('pedidoUsers')
    op.drop_table('pedidoLanches')
    op.drop_table('Entregas')
    op.drop_table('enderecoUsers')
    op.drop_table('acessoUsers')
    op.drop_table('Pedidos')
    op.drop_table('Users')
    op.drop_table('Telefones')
    op.drop_table('Mesas')
    op.drop_table('Lanches')
    op.drop_table('Enderecos')
    op.drop_table('Acessos')
    # ### end Alembic commands ###