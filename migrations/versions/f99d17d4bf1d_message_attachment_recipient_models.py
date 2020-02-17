"""Message, Attachment, Recipient Models

Revision ID: f99d17d4bf1d
Revises: 1f0ef92767aa
Create Date: 2020-02-16 22:11:04.325470

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f99d17d4bf1d'
down_revision = '1f0ef92767aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('attachment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message_id', sa.String(length=32), nullable=True),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['message_id'], ['message.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('attachment')
    # ### end Alembic commands ###
