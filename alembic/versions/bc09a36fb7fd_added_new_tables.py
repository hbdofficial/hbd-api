"""added new tables

Revision ID: bc09a36fb7fd
Revises: 
Create Date: 2024-04-30 18:08:33.860437

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bc09a36fb7fd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('gender', sa.String(), nullable=True),
    sa.Column('birthday', sa.DateTime(), nullable=False),
    sa.Column('profile_pic', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('username')
    )
    op.create_table('card',
    sa.Column('card_no', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('holder_name', sa.String(), nullable=False),
    sa.Column('expiry_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['username'], ['users.username'], ),
    sa.PrimaryKeyConstraint('card_no', 'username')
    )
    op.create_table('friends',
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('following_username', sa.String(), nullable=False),
    sa.Column('date_followed', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['following_username'], ['users.username'], ),
    sa.ForeignKeyConstraint(['username'], ['users.username'], ),
    sa.PrimaryKeyConstraint('username', 'following_username')
    )
    op.create_table('notification',
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('timestamp', sa.TIMESTAMP(), nullable=False),
    sa.Column('content', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['username'], ['users.username'], ),
    sa.PrimaryKeyConstraint('username', 'content')
    )
    op.create_table('wishes_table',
    sa.Column('story_id', sa.String(), nullable=False),
    sa.Column('wishes_to', sa.String(), nullable=True),
    sa.Column('wished_by', sa.String(), nullable=True),
    sa.Column('wished_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['wished_by'], ['users.username'], ),
    sa.ForeignKeyConstraint(['wishes_to'], ['users.username'], ),
    sa.PrimaryKeyConstraint('story_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wishes_table')
    op.drop_table('notification')
    op.drop_table('friends')
    op.drop_table('card')
    op.drop_table('users')
    # ### end Alembic commands ###