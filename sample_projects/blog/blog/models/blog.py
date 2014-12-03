from webpages import orm


class Blog(orm.Model):
    name = orm.fields.CharField(max_length=200)
