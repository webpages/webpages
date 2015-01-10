from webpages import Controller
from ..models.blog import Blog as BlogModel
from ..models.article import Article as ArticleModel


class Blog(Controller):

    def index(self, request):
        return self.list(request)

    def list(self, request):
        objects = BlogModel.first('name')
        return self.render('blog/list', {'objects': objects})

    def view(self, request):
        blog = BlogModel.get(slug=request.GET['slug'])
        objects = ArticleModel.filter(blog=blog).last('date_create')
        return self.render('blog/view', {'objects': objects})

    def create(self, request):
        form = BlogModel.get_blog_create_form(request)
        return self.render('blog/create', {'form': form})

    def edit(self, request):
        form = BlogModel.get_blog_edit_form(request)
        return self.render('blog/edit', {'form': form})

    def delete(self, request):
        form = BlogModel.get_blog_delete_form(request)
        return self.render('blog/delete', {'form': form})

    def not_found(self, request):
        raise Exception('Not found')
