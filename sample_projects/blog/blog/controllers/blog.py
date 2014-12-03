from webpages import Controller


class Blog(Controller):

    def index(self, request):
        return self.render('blog/index')

    def view_list(self, request):
        return self.render('blog/view_list')

    def view_one(self, request):
        return self.render('blog/view_one')

    def create(self, request):
        return self.render('blog/create')

    def delete(self, request):
        return self.render('blog/delete')

    def edit(self, request):
        return self.render('blog/edit')
