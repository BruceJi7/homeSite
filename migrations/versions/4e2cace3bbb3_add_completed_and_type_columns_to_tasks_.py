"""Add completed and type columns to tasks model

Revision ID: 4e2cace3bbb3
Revises: a90b88f588c2
Create Date: 2020-05-08 12:23:45.970178

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e2cace3bbb3'
down_revision = 'a90b88f588c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('taskType', sa.String(length=64), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'taskType')
    # ### end Alembic commands ###
