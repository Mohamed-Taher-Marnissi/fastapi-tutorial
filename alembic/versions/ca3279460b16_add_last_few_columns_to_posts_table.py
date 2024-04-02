"""add last few columns to posts table

Revision ID: ca3279460b16
Revises: 2d906250a1a6
Create Date: 2024-04-02 17:32:56.571702

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ca3279460b16'
down_revision: Union[str, None] = '2d906250a1a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# class Post(Base):
#     __tablename__ = "posts"

#     id = Column(Integer, primary_key = True, nullable=False)
#     title = Column(String, nullable = False)
#     content = Column(String, nullable = False)
#     published = Column(Boolean, server_default ='TRUE' , nullable= False)
#     created_at = Column(TIMESTAMP(timezone=True) ,nullable=False, server_default=text('now()'))
#     owner_id = Column(Integer , ForeignKey("users.id", ondelete="CASCADE"), nullable= False)
#     owner  = relationship("User")

def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), server_default='TRUE', nullable=False),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)        
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
