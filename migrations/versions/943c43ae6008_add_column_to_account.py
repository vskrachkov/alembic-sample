"""add column to account

Revision ID: 943c43ae6008
Revises: 65e7b8bc449b
Create Date: 2020-08-15 12:37:19.453541

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '943c43ae6008'
down_revision = '65e7b8bc449b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('account', sa.Column('last_transaction_date', sa.DateTime))


def downgrade():
    op.drop_column('account', 'last_transaction_date')
