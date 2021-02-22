"""empty message

Revision ID: 08425ca8f506
Revises: 5af7fedff1cb
Create Date: 2021-01-28 16:15:45.291373

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08425ca8f506'
down_revision = '5af7fedff1cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('calendar',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('all_day', sa.String(length=120), nullable=True),
    sa.Column('habitat_id', sa.String(length=80), nullable=True),
    sa.Column('notes', sa.String(length=250), nullable=True),
    sa.Column('pets', sa.String(length=100), nullable=True),
    sa.Column('start_date', sa.String(length=100), nullable=False),
    sa.Column('end_date', sa.String(length=100), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('all_day')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('calendar')
    # ### end Alembic commands ###
