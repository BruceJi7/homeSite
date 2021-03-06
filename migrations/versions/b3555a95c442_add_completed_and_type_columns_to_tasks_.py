"""Add completed and type columns to tasks model

Revision ID: b3555a95c442
Revises: 409bfa0789ad
Create Date: 2020-05-08 12:30:20.850662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3555a95c442'
down_revision = '409bfa0789ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('isSingleUse', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'isSingleUse')
    # ### end Alembic commands ###
