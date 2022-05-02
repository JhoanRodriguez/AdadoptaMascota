"""1.0.0.0 created fk for initial tables

Revision ID: 4f83f3abce8f
Revises: 8d671979b946
Create Date: 2022-04-29 21:03:00.275106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "4f83f3abce8f"
down_revision = "8d671979b946"
branch_labels = None
depends_on = None


def upgrade():
    op.create_foreign_key(
        "fk_users_company",
        "users",
        "company",
        ["company_id"],
        ["id"],
        ondelete="CASCADE",
        source_schema="ama",
        referent_schema="ama",
    )

    op.create_foreign_key(
        "fk_users_users",
        "users",
        "users",
        ["modified_by"],
        ["id"],
        ondelete="CASCADE",
        source_schema="ama",
        referent_schema="ama",
    )

    op.create_foreign_key(
        "fk_company_users_created_by",
        "company",
        "users",
        ["created_by"],
        ["id"],
        ondelete="CASCADE",
        source_schema="ama",
        referent_schema="ama",
    )

    op.create_foreign_key(
        "fk_company_users_modified_by",
        "company",
        "users",
        ["modified_by"],
        ["id"],
        ondelete="CASCADE",
        source_schema="ama",
        referent_schema="ama",
    )

    op.create_foreign_key(
        "fk_pets_users_responsable",
        "pets",
        "users",
        ["responsable"],
        ["id"],
        ondelete="CASCADE",
        source_schema="ama",
        referent_schema="ama",
    )

    op.create_foreign_key(
        "fk_pets_users_created_by",
        "pets",
        "users",
        ["created_by"],
        ["id"],
        ondelete="CASCADE",
        source_schema="ama",
        referent_schema="ama",
    )

    op.create_foreign_key(
        "fk_pets_users_modified_by",
        "pets",
        "users",
        ["modified_by"],
        ["id"],
        ondelete="CASCADE",
        source_schema="ama",
        referent_schema="ama",
    )

    op.create_foreign_key(
        "fk_vaccines_users_created_by",
        "vaccines",
        "users",
        ["created_by"],
        ["id"],
        ondelete="CASCADE",
        source_schema="ama",
        referent_schema="ama",
    )

    op.create_foreign_key(
        "fk_vaccines_users_modified_by",
        "vaccines",
        "users",
        ["modified_by"],
        ["id"],
        ondelete="CASCADE",
        source_schema="ama",
        referent_schema="ama",
    )

    op.create_foreign_key(
        "fk_vaccines_applied_vaccines_vaccine_id",
        "vaccines_applied",
        "vaccines",
        ["vaccine_id"],
        ["id"],
        ondelete="CASCADE",
        source_schema="ama",
        referent_schema="ama",
    )

    op.create_foreign_key(
        "fk_vaccines_applied_pets_pets_id",
        "vaccines_applied",
        "pets",
        ["pet_id"],
        ["id"],
        ondelete="CASCADE",
        source_schema="ama",
        referent_schema="ama",
    )


def downgrade():
    op.drop_constraint(
        "fk_company_users_modified_by", "company", schema="ama", type_="foreignkey"
    )
    op.drop_constraint(
        "fk_company_users_created_by", "company", schema="ama", type_="foreignkey"
    )
    op.drop_constraint("fk_users_users", "users", schema="ama", type_="foreignkey")
    op.drop_constraint("fk_users_company", "users", schema="ama", type_="foreignkey")
    op.drop_constraint(
        "fk_pets_users_responsable", "pets", schema="ama", type_="foreignkey"
    )
    op.drop_constraint(
        "fk_pets_users_created_by", "pets", schema="ama", type_="foreignkey"
    )
    op.drop_constraint(
        "fk_pets_users_modified_by", "pets", schema="ama", type_="foreignkey"
    )
    op.drop_constraint(
        "fk_vaccines_users_created_by", "vaccines", schema="ama", type_="foreignkey"
    )
    op.drop_constraint(
        "fk_vaccines_users_modified_by", "vaccines", schema="ama", type_="foreignkey"
    )
    op.drop_constraint(
        "fk_vaccines_applied_vaccines_vaccine_id",
        "vaccines_applied",
        schema="ama",
        type_="foreignkey",
    )
    op.drop_constraint(
        "fk_vaccines_applied_pets_pets_id",
        "vaccines_applied",
        schema="ama",
        type_="foreignkey",
    )
