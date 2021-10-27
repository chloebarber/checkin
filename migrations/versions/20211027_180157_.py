"""empty message

Revision ID: 15634a41e24a
Revises: ffdc0a98111c
Create Date: 2021-10-27 18:01:57.816741

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15634a41e24a'
down_revision = 'ffdc0a98111c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('user_type', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'user_type')
    # ### end Alembic commands ###
