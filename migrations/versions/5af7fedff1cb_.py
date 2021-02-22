"""empty message

Revision ID: 5af7fedff1cb
Revises: 7cd99a4cddb7
Create Date: 2021-01-27 18:02:23.056090

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5af7fedff1cb'
down_revision = '7cd99a4cddb7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('habitat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('pet_in_habitat_id', sa.String(length=80), nullable=True),
    sa.Column('info', sa.String(length=250), nullable=True),
    sa.Column('habitat_location', sa.String(length=100), nullable=True),
    sa.Column('habitat_supplies', sa.String(length=100), nullable=True),
    sa.Column('habitat_equipment', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('habitat')
    # ### end Alembic commands ###