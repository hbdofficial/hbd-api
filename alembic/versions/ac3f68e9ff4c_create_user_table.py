"""create user table

Revision ID: ac3f68e9ff4c
Revises: 
Create Date: 2024-04-01 17:48:30.486429

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'ac3f68e9ff4c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("username", sa.String, primary_key=True),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("hashed_password",sa.String, nullable=False),
        sa.Column("email",sa.String, nullable=True),
        sa.Column("gender",sa.String, nullable=True),
        sa.Column("birthday",sa.Date),
        sa.Column("profile_pic",sa.String, nullable=True)
    )


def downgrade() -> None:
    pass
