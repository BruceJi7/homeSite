"""Add shipping db model

Revision ID: 51b1fe6ff1dc
Revises: 
Create Date: 2020-05-03 15:44:25.450017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51b1fe6ff1dc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('parcelInfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('trackingNumber', sa.String(length=64), nullable=True),
    sa.Column('company', sa.String(length=64), nullable=True),
    sa.Column('delivered', sa.Boolean(), nullable=True),
    sa.Column('status', sa.String(length=64), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('location', sa.String(length=64), nullable=True),
    sa.Column('extraNotes', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('parcelInfo')
    # ### end Alembic commands ###
