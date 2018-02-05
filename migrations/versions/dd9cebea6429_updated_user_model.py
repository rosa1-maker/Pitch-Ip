"""Updated User model

Revision ID: dd9cebea6429
Revises: b57817ab4378
Create Date: 2018-02-05 10:29:58.579842

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd9cebea6429'
down_revision = 'b57817ab4378'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('posted', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'posted')
    # ### end Alembic commands ###