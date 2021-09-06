"""add active to Store

Revision ID: edb1b4bfbd99
Revises: 4d6945689969
Create Date: 2021-07-13 14:34:16.120795

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'edb1b4bfbd99'
down_revision = '4d6945689969'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('store', sa.Column('active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('store', 'active')
    # ### end Alembic commands ###