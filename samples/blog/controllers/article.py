from webpages import Controller
from ..models.article import Article as ArticleModel


class Article(Controller):

    def index(self, request):
        return self.list(request)

    def list(self, request):
        return self.render('article/list')

    def view(self, request):
        return self.render('article/view')

    def create(self, request):
        form = ArticleModel.get_article_form()
        return self.render('article/create', {'form': form})

    def create_post(self, request):
        form = ArticleModel.get_article_form(request.data)
        if form.valid():
            obj = form.save()
            return self.redirect('/article/view/' + obj.id)
        return self.render('article/create', {'form': form})

    def edit(self, request):
        form = ArticleModel.get_article_form()
        return self.render('article/edit', {'form': form})

    def delete(self, request):
        return self.render('article/delete')

    def not_found(self, request):
        raise Exception('Not found')
