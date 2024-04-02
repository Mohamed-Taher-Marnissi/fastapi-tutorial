"""create posts table

Revision ID: 5ded923fd7f8
Revises: 
Create Date: 2024-04-01 19:00:20.622329

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5ded923fd7f8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# handle the changes
def upgrade() -> None:
    op.create_table('posts' , sa.Column('id', sa.Integer(), nullable = False , primary_key = True)
        , sa.Column('title', sa.String(), nullable=False))
    pass

# handle the rolling back
def downgrade() -> None:
    op.drop_table('posts')
    pass
