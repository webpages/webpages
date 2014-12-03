from webpages import Controller
from ..models.blog import Blog as BlogModel


class Blog(Controller):

    def index(self, request):
        return self.render('blog/index')

    def view_list(self, request):
        return self.render('blog/view_list')

    def view_one(self, request):
        return self.render('blog/view_one')

    def create(self, request):
        form = BlogModel.get_blog_form()
        return self.render('blog/create', {'form': form})

    def edit(self, request):
        form = BlogModel.get_blog_form()
        return self.render('blog/edit', {'form': form})

    def delete(self, request):
        return self.render('blog/delete')
