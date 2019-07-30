"""empty message

Revision ID: 7a336e26d0b1
Revises: b47c79195e47
Create Date: 2019-07-30 11:15:04.320630

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a336e26d0b1'
down_revision = 'b47c79195e47'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('parcel_name', sa.String(length=100), nullable=True),
    sa.Column('parcel_number', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('parcel_number')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=40), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.drop_table('item')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(length=60), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key')
    )
    op.create_table('item',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('parcel_name', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('parcel_number', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='item_pkey'),
    sa.UniqueConstraint('parcel_number', name='item_parcel_number_key')
    )
    op.drop_table('users')
    op.drop_table('items')
    # ### end Alembic commands ###
