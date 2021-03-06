"""empty message

Revision ID: 558cea325d32
Revises: 
Create Date: 2018-07-15 16:17:32.494687

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '558cea325d32'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('encrypted_password', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'encrypted_password')
    # ### end Alembic commands ###
