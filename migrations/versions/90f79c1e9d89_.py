"""empty message

Revision ID: 90f79c1e9d89
Revises: 7a336e26d0b1
Create Date: 2019-07-30 14:26:00.074882

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90f79c1e9d89'
down_revision = '7a336e26d0b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('parcel_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('items', 'parcel_id')
    # ### end Alembic commands ###
