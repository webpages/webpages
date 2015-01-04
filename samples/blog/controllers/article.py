from webpages import Controller
from ..models.article import Article as ArticleModel


class Article(Controller):

    def index(self, request):
        return self.render('article/index')

    def view_list(self, request):
        return self.render('article/view_list')

    def view_one(self, request):
        return self.render('article/view_one')

    def create(self, request):
        form = ArticleModel.get_article_form()
        return self.render('article/create', {'form': form})

    def edit(self, request):
        form = ArticleModel.get_article_form()
        return self.render('article/edit', {'form': form})

    def delete(self, request):
        return self.render('article/delete')

    def not_found(self, request):
        raise Exception('Not found')
