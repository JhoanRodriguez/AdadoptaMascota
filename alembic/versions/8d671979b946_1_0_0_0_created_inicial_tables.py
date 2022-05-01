"""1.0.0.0 created inicial tables

Revision ID: 8d671979b946
Revises: 7c3fe4c63f39
Create Date: 2022-04-29 18:22:38.245270

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8d671979b946"
down_revision = "7c3fe4c63f39"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("name", sa.String(20), nullable=False),
        sa.Column("last_name", sa.String(20), nullable=False),
        sa.Column("password", sa.String(120), nullable=False),
        sa.Column("email", sa.String(50), nullable=False),
        sa.Column("cellphone", sa.String(20), nullable=False),
        sa.Column("city", sa.String(50), nullable=False),
        sa.Column("country", sa.String(50), nullable=False),
        sa.Column(
            "company_id",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "created_on", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column(
            "modified_on", sa.DateTime(), server_default=sa.text("now()"), nullable=True
        ),
        sa.Column(
            "modified_by",
            sa.Integer(),
            nullable=True,
        ),
        schema="ama",
    )

    op.create_table(
        "company",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("nit", sa.String(15), nullable=False),
        sa.Column("email", sa.String(50), nullable=False),
        sa.Column("cellphone", sa.String(20), nullable=True),
        sa.Column("city", sa.String(50), nullable=False),
        sa.Column("country", sa.String(50), nullable=False),
        sa.Column("address", sa.String(50), nullable=False),
        sa.Column(
            "created_on", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column(
            "created_by",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "modified_on", sa.DateTime(), server_default=sa.text("now()"), nullable=True
        ),
        sa.Column(
            "modified_by",
            sa.Integer(),
            nullable=True,
        ),
        schema="ama",
    )

    op.create_table(
        "pets",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("age", sa.Integer(), nullable=False),
        sa.Column(
            "size",
            sa.Enum(
                "Pequeno",
                "Mediano",
                "Grande",
                name="petsizeenum",
            ),
            nullable=False,
        ),
        sa.Column(
            "kind",
            sa.Enum(
                "Gato",
                "Perro",
                name="petkindenum",
            ),
            nullable=False,
        ),
        sa.Column(
            "sex",
            sa.Enum(
                "Macho",
                "Hembra",
                name="petsexenum",
            ),
            nullable=False,
        ),
        sa.Column("sterilized", sa.Boolean, nullable=False, default=False),
        sa.Column("description", sa.String(280), nullable=False),
        sa.Column("picture", sa.String(250), nullable=False),
        sa.Column("responsable", sa.Integer(), nullable=False),
        sa.Column("adopted", sa.Boolean, nullable=False, default=False),
        sa.Column(
            "created_on", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column(
            "created_by",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "modified_on", sa.DateTime(), server_default=sa.text("now()"), nullable=True
        ),
        sa.Column(
            "modified_by",
            sa.Integer(),
            nullable=True,
        ),
        schema="ama",
    )

    op.create_table(
        "vaccines",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column(
            "created_on", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column(
            "created_by",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "modified_on", sa.DateTime(), server_default=sa.text("now()"), nullable=True
        ),
        sa.Column(
            "modified_by",
            sa.Integer(),
            nullable=True,
        ),
        schema="ama",
    )

    op.create_table(
        "vaccines_applied",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("vaccine_id", sa.Integer(), nullable=False),
        sa.Column("pet_id", sa.Integer(), nullable=False),
        sa.Column(
            "applied_on", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column("applied_at", sa.String(50), nullable=False),
        sa.Column("proof", sa.String(250), nullable=False),
        schema="ama",
    )

    op.execute(
        sa.text(
            """
            INSERT INTO ama.users (
                name, 
                last_name, 
                password, 
                email, 
                cellphone, 
                city, 
                country, 
                company_id
            ) VALUES (
                'Adopta',
                'Mascota',
                'pbkdf2:sha256:260000$K5HwtJT8VkuD6zPr$84933e379048aca90f223175c41392d607caa37cb79abf1847c18e38f4f2a975',
                'info@adoptamascota.com',
                '0000000000',
                'Barranquilla',
                'Colombia',
                '1'
            );
            """
        )
    )

    op.execute(
        sa.text(
            """
            INSERT INTO ama.company (
                name,
                nit,
                email,
                city,
                country,
                address,
                created_by
            ) VALUES (
                'Adopta Mascota',
                '000000000-0',
                'info@adoptamascota.com',
                'Barranquilla',
                'Colombia',
                'Cra 74 #88 - 82',
                '1'
            )
            """
        )
    )


def downgrade():
    op.drop_table("vaccines_applied", schema="ama")
    op.drop_table("vaccines", schema="ama")
    op.drop_table("pets", schema="ama")
    sa.Enum(name="petsizeenum").drop(op.get_bind(), checkfirst=False)
    sa.Enum(name="petkindenum").drop(op.get_bind(), checkfirst=False)
    sa.Enum(name="petsexenum").drop(op.get_bind(), checkfirst=False)
    op.drop_table("company", schema="ama")
    op.drop_table("users", schema="ama")
