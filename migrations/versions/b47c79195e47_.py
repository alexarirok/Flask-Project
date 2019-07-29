"""empty message

Revision ID: b47c79195e47
Revises: 8c2ec4d38e0a
Create Date: 2019-07-29 17:46:14.435052

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b47c79195e47'
down_revision = '8c2ec4d38e0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('parcel_name', sa.String(length=100), nullable=True),
    sa.Column('parcel_number', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('parcel_number')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('item')
    # ### end Alembic commands ###