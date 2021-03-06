"""empty message

Revision ID: 9e182f821d4a
Revises: 37828922af49
Create Date: 2017-11-09 16:13:19.627313

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e182f821d4a'
down_revision = '37828922af49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profile', sa.Column('min_rating', sa.Float(precision=2)))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('profile', 'min_rating')
    # ### end Alembic commands ###
