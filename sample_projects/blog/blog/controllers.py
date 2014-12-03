from webpages import Controller


class Blog(Controller):

    def index(self):
        return self.render('blog/index')

    def view_list(self):
        return self.render('blog/view_list')

    def view_one(self):
        return self.render('blog/view_one')

    def create(self):
        return self.render('blog/create')

    def delete(self):
        return self.render('blog/delete')

    def edit(self):
        return self.render('blog/edit')


class Article(Controller):

    def index(self):
        return self.render('article/index')

    def view_list(self):
        return self.render('article/view_list')

    def view_one(self):
        return self.render('article/view_one')

    def create(self):
        return self.render('article/create')

    def delete(self):
        return self.render('article/delete')

    def edit(self):
        return self.render('article/edit')
