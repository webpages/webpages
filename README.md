WebPages - python web framework
===

Hello.

This project is based on good ideas from **Ruby on Rails** and **Django** web frameworks. Also I wish to add asynchronous code execution like in **Tornado** and **Node.js**. I tried to simplify project structure to make project as easy as it possible. I believe that you find it useful.


Documentation
---

Read full project [documentation](docs/). You can help us to improve our docs!


Our goals:
---

 * **automatic routers**. We DON'T have `urls.py` url mapping *(like we do in Django)*. Instead the web framework search controllers and actions based on convention `controller_name/action_name/...` *(`/blog/view/123/` call `view` action of `Blog` controller with `123` argument)*. To disable application - rename it with leading underscore, like this `_blog`
 * **check broken urls**. We can run command `check urls` to detect broken urls and fix them manually. You don't need to support url mapping to do this extra job
 * we DON't have reusable applications *(like in Django)*. Only root folders `models`, `views` and `controllers` where you place all your code. You don't need to think about *"In what app I should place this new model?"*. Have an idea? - Code it!
 * **settings inheritance**. Project has own settings file and can redefine default settings for models and controllers. Settings file contains grouped configuraions per component *(NO global names like in Django)*
 * **generate project from command-line**. And each model/view/controller also sould be. To add new model - we use command-line to create appropriate model, view and controller with appropriate actions and templates for this new model (like in **Ruby on Rails**)
 * **easy migrations**. When we rename field or add new one - we do it in command-line and it save our changes to migration file
 * **data validation**. All data come to database only via forms (like in **Django**, but forms are part of Model). In total - the Model can return us the From that we requested *(`User.get_registration_from()` or `User.get_edit_profile_form()`)*
 * **middleware support**. Tou can add own middleware classes to do something before and after execution of each Controller's action
 * **[ORM](https://github.com/webpages/orm)**. For the first time we can use third-party ORM's *(Django ORM or SQLAlchemy). But we wish to create simplified syntax like this `User.first` or `User.all.filter((F.name='Tony' and F.age.in(10, 20, 30)) or F.roles.name='admins')`
 **template engine** with python-like syntax, without closing tags *(styled with indentation, like in `Slim` for Ruby)*


System requirements
---

 * to `return` something from function that contains `yield` keyword - we need to use **Python 3.3**


TODO
---

- [x] ~~Create facebook group to have feedback from developers~~
- [ ] [#1](../../issues/1) **Run web server on top of webOb or Werkzeug**
- [ ] Describe plans splitted by milestones in issues
- [ ] Use Django ORM and Django Templates to speed-up development

----

Follow us on [facebook](https://www.facebook.com/WebPagesFramework)
