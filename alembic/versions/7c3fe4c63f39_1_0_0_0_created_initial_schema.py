"""1.0.0.0 Created initial schema

Revision ID: 7c3fe4c63f39
Revises: 
Create Date: 2022-04-29 14:56:21.686092

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "7c3fe4c63f39"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute("CREATE SCHEMA IF NOT EXISTS ama;")


def downgrade():
    op.execute("DROP SCHEMA IF EXISTS ama CASCADE;")
