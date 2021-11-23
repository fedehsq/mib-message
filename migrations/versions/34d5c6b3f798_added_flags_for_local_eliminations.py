"""added flags for local eliminations

Revision ID: 34d5c6b3f798
Revises: e2104ae205b0
Create Date: 2021-11-23 09:46:49.319403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34d5c6b3f798'
down_revision = 'e2104ae205b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Message', sa.Column('hidden_for_sender', sa.Boolean(), nullable=True))
    op.add_column('Message', sa.Column('hidden_for_receiver', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Message', 'hidden_for_receiver')
    op.drop_column('Message', 'hidden_for_sender')
    # ### end Alembic commands ###