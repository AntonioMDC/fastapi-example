"""add user table

Revision ID: 648843c47655
Revises: c5af0fef7a8e
Create Date: 2022-12-24 16:35:35.760103

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '648843c47655'
down_revision = 'c5af0fef7a8e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users', 
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'),
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
