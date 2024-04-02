"""add user table

Revision ID: 8abad67caaf2
Revises: f5ad4e72ec5f
Create Date: 2024-04-02 02:00:52.359338

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key= True, nullable=False)
#     email = Column(String, nullable=False, unique = True)
#     password = Column(String, nullable=False)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

# revision identifiers, used by Alembic.
revision: str = '8abad67caaf2'
down_revision: Union[str, None] = 'f5ad4e72ec5f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users' , sa.Column('id' , sa.Integer(), nullable= False),
            sa.Column('email', sa.String(), nullable = False),
            sa.Column('password', sa.String(), nullable= False),
            sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),
            sa.PrimaryKeyConstraint('id'),
            sa.UniqueConstraint('email')
            )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
