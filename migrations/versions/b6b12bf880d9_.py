"""empty message

Revision ID: b6b12bf880d9
Revises: 
Create Date: 2023-03-14 07:26:44.788866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6b12bf880d9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('property',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('no_of_bedrooms', sa.Integer(), nullable=True),
    sa.Column('no_of_bathrooms', sa.Integer(), nullable=True),
    sa.Column('location', sa.String(length=100), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(length=20), nullable=True),
    sa.Column('description', sa.String(length=1000), nullable=True),
    sa.Column('photo', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('location'),
    sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('property')
    # ### end Alembic commands ###
