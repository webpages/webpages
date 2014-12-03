from webpages import orm


class Blog(orm.Model):
    name = orm.fields.CharField(max_length=200)


class Article(orm.Model):
    title = orm.fields.CharField(max_length=200)
    text = orm.fields.CharField(max_length=10000)
    blog = orm.fields.ReferenceField(model=Blog)
