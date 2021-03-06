"""change user class

Revision ID: 547a2245508c
Revises: 
Create Date: 2020-03-07 00:16:37.765944

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '547a2245508c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(length=255), nullable=True),
    sa.Column('driver_name', sa.String(length=255), nullable=True),
    sa.Column('owner_name', sa.String(length=255), nullable=True),
    sa.Column('owner_email', sa.String(length=255), nullable=True),
    sa.Column('company_name', sa.String(length=255), nullable=True),
    sa.Column('eng_no', sa.String(length=255), nullable=True),
    sa.Column('reg_no', sa.String(length=255), nullable=True),
    sa.Column('mileage', sa.String(length=255), nullable=True),
    sa.Column('driver_no', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('pass_secure', sa.String(length=255), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('roles', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('pass_secure')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('details')
    # ### end Alembic commands ###
