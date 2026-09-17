"""link students to users

Revision ID: 6e42048b088e
Revises: a697c0eb74ee
Create Date: 2026-09-16 09:11:55.610893

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6e42048b088e'
down_revision: Union[str, Sequence[str], None] = 'a697c0eb74ee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("students") as batch_op:
        batch_op.add_column(
            sa.Column("user_id", sa.Integer(), nullable=True)
        )

        batch_op.create_foreign_key(
            "fk_students_user_id_users",
            "users",
            ["user_id"],
            ["id"]
        )


def downgrade() -> None:
    with op.batch_alter_table("students") as batch_op:
        batch_op.drop_constraint(
            "fk_students_user_id_users",
            type_="foreignkey"
        )
        batch_op.drop_column("user_id")
