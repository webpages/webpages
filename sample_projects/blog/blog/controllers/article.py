from webpages import Controller


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
