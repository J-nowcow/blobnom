"""added practice

Revision ID: dae510910c91
Revises: 1b10836df245
Create Date: 2025-02-28 15:39:11.332228

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'dae510910c91'
down_revision: Union[str, None] = '1b10836df245'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('practice_sets',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('duration', sa.Integer(), nullable=False),
                    sa.Column('platform', postgresql.ENUM(name='platform', create_type=False), nullable=False),
                    sa.Column('penalty_type', sa.Enum('ICPC', name='penaltytype'), nullable=False),
                    sa.Column('problem_ids', sa.ARRAY(sa.Integer()), nullable=False),
                    sa.Column('created_member_id', sa.Integer(), nullable=True),
                    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
                    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
                    sa.ForeignKeyConstraint(['created_member_id'], ['members.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )

    op.create_table('practice_members',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('practice_set_id', sa.Integer(), nullable=True),
                    sa.Column('member_id', sa.Integer(), nullable=True),
                    sa.Column('room_id', sa.Integer(), nullable=True),
                    sa.Column('score', sa.Integer(), nullable=True),
                    sa.Column('penalty', sa.Integer(), nullable=True),
                    sa.Column('rank', sa.Integer(), nullable=True),
                    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
                    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
                    sa.ForeignKeyConstraint(['member_id'], ['members.id'], ),
                    sa.ForeignKeyConstraint(['practice_set_id'], ['practice_sets.id'], ),
                    sa.ForeignKeyConstraint(['room_id'], ['rooms.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )

    # Then add the column to rooms
    op.add_column('rooms', sa.Column('practice_session_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'rooms', 'practice_members', ['practice_session_id'], ['id'])


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'rooms', type_='foreignkey')
    op.drop_column('rooms', 'practice_session_id')
    op.drop_table('practice_sets')
    op.drop_table('practice_members')
    # ### end Alembic commands ###
