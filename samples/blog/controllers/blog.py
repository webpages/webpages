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
        blog = BlogModel.get(slug=request.data['slug'])
        objects = ArticleModel.filter(blog=blog).last('date_create')
        return self.render('blog/view', {'objects': objects})

    def create(self, request):
        form = BlogModel.get_blog_create_form(request.data)
        return self.render('blog/create', {'form': form})

    def edit(self, request):
        form = BlogModel.get_blog_edit_form(request.data)
        return self.render('blog/edit', {'form': form})

    def delete(self, request):
        form = BlogModel.get_blog_delete_form(request.data)
        return self.render('blog/delete', {'form': form})

    def delete_post(self, request):
        obj = BlogModel.get(id=request.params[0])
        if request.user == obj.author:
            obj.delete()
        return self.render('blog/list')

    def not_found(self, request):
        raise Exception('Not found')
