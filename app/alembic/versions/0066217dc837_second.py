"""Second

Revision ID: 0066217dc837
Revises: c8c0c8032fd2
Create Date: 2023-10-17 05:13:18.800335

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '0066217dc837'
down_revision: Union[str, None] = 'c8c0c8032fd2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('question_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('question', 'question_id')
    # ### end Alembic commands ###
