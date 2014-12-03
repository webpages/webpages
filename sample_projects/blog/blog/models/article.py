from webpages import orm
from .blog import Blog


class Article(orm.Model):
    title = orm.fields.CharField(max_length=200)
    text = orm.fields.CharField(max_length=10000)
    date_create = orm.fields.DateField(set_now=True)
    blog = orm.fields.ReferenceField(model=Blog)

    @classmethod
    def get_article_form(cls):
        """
        We can define multiple forms to work with model(s).

        Sometimes we need only one form, but in some cases we need two or more
        forms to work with this model. And sometimes we need to edit two or more
        models via single form. For this purpose we need to create multiple methods
        in format "get_xxx_form()".
        """
        return cls.form(model=cls)
