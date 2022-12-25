"""add content column to post table

Revision ID: c5af0fef7a8e
Revises: ff83d06fe376
Create Date: 2022-12-24 16:30:54.925087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5af0fef7a8e'
down_revision = 'ff83d06fe376'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
