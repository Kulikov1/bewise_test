"""First migration

Revision ID: c8c0c8032fd2
Revises: 
Create Date: 2023-10-17 02:03:01.556766

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'c8c0c8032fd2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('question_text', sa.String(length=200), nullable=False),
    sa.Column('answer_text', sa.String(length=200), nullable=False),
    sa.Column('created_at', sa.String(length=200), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('question')
    # ### end Alembic commands ###
