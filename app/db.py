import sqlalchemy as sa

metadata = sa.MetaData(
    naming_convention={
        "pk": "pk_%(table_name)s",
        "ix": "ix_%(table_name)s__%(column_0_N_name)s",
        "uq": "uq_%(table_name)s__%(column_0_N_name)s",
        "ck": "ch_%(table_name)s__%(constraint_name)s",
        "fk": "fk_%(table_name)s__%(column_0_name)s_%(referred_table_name)s",
    }
)

user = sa.Table(
    "user",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("name", sa.String(50)),
    sa.Column("fullname", sa.String(50)),
    sa.Column("nickname", sa.String(12), unique=True),
    sa.Column("age", sa.Integer()),
    sa.UniqueConstraint("name", "fullname"),
)

account = sa.Table(
    "account",
    metadata,
    sa.Column("id", sa.Integer(), primary_key=True),
    sa.Column("user_id", sa.Integer(), sa.ForeignKey("user.id")),
    sa.Column("description", sa.Unicode(200), index=True),
)

account_balance = sa.Table(
    "account_balance",
    metadata,
    sa.Column("id", sa.BigInteger(), primary_key=True),
    sa.Column("balance", sa.Numeric(), nullable=False),
    sa.CheckConstraint("balance > 0", name='balance_is_positive'),
    sa.ForeignKeyConstraint(("id",), ("account.id",)),
)
