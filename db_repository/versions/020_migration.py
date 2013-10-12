from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
items = Table('items', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name_item', String(length=100)),
    Column('description', String(length=500)),
    Column('date', DateTime),
    Column('item_status', String(length=10)),
    Column('user_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['items'].columns['item_status'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['items'].columns['item_status'].drop()
