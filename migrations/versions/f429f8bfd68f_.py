"""empty message

Revision ID: f429f8bfd68f
Revises: 
Create Date: 2020-09-27 21:00:06.518366

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f429f8bfd68f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('provinces',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_provinces_name'), 'provinces', ['name'], unique=True)
    op.create_table('reports',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('province', sa.String(length=64), nullable=True),
    sa.Column('district', sa.String(length=64), nullable=True),
    sa.Column('localbody', sa.String(length=64), nullable=True),
    sa.Column('customer_id', sa.String(length=64), nullable=True),
    sa.Column('latitude', sa.String(length=64), nullable=True),
    sa.Column('longitude', sa.String(length=64), nullable=True),
    sa.Column('ward', sa.String(length=64), nullable=True),
    sa.Column('status', sa.String(length=64), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_reports_province'), 'reports', ['province'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('districts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('province_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['province_id'], ['provinces.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_districts_name'), 'districts', ['name'], unique=True)
    op.create_table('localbodies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('type', sa.String(length=64), nullable=True),
    sa.Column('district_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['district_id'], ['districts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_localbodies_name'), 'localbodies', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_localbodies_name'), table_name='localbodies')
    op.drop_table('localbodies')
    op.drop_index(op.f('ix_districts_name'), table_name='districts')
    op.drop_table('districts')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_reports_province'), table_name='reports')
    op.drop_table('reports')
    op.drop_index(op.f('ix_provinces_name'), table_name='provinces')
    op.drop_table('provinces')
    # ### end Alembic commands ###