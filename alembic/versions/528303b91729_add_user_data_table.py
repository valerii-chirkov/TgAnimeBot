"""Add user_data table

Revision ID: 528303b91729
Revises: 
Create Date: 2023-08-29 20:22:41.905508

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '528303b91729'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_data',
                    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
                    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('date_joined', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'),
                              autoincrement=False, nullable=False),
                    sa.PrimaryKeyConstraint('id', name='user_data_pkey')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_data')
    # ### end Alembic commands ###
