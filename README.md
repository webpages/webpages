WebPages - python web framework
===

Hello.

This project is based on good ideas from **Ruby on Rails** and **Django** web frameworks. Also I wish to add asynchronous code execution like in **Tornado** and **Node.js**. I tried to simplify project structure to make project as easy as it possible. I believe that you find it useful.


Documentation
---

Read full project [documentation](docs/). You can help us to improve our docs!


Our goals:
---

 * **automatic routers**. We DON'T have `urls.py` url mapping *(like we do in Django)*. Instead the web framework search controllers and actions based on convention `controller_name/action_name/...` *(`/blog/view/123/` call `view` action of `Blog` controller with `123` argument)*
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


Roadmap
---

- [x] Create facebook group to have feedback from developers
- [ ] Run web server on top of webOb or Werkzeug
- [ ] Describe plans splitted by milestones in issues
- [ ] Use Django ORM and Django Templates to speed-up development


**Follow us on [facebook](https://www.facebook.com/WebPagesFramework)**

*****

My old visiton *(see below)*
-----

Below is my original visiton of this project. Above - is my new vision of this web framework.

### Foreword

I was thinking about how to teach my nephew to create web applications. The boy were 14 years old, and his hasn't experience in programming yet.

My goal was to tell about how to write web applications on python. But I was found that I need to tell a lot of basic information about:
 - *hirst of all* help to install **Ubuntu Linux** to his PC
 - basics
  - what is **python** language (this is not hard)
  - what is **django** and how to create new empty project
  - what is **html, css, java srcipt**
 - how to **run project**
  - how to change **setings.py**
  - what is **regular expressions** (to build urls.py)
  - how to enable admin app and show admin site
 - how to **create new app**
  - describe **models**
  - design **urls.py**
  - add new app to **INSTALLED_APPS** in settings.py
  - create new controller in **views.py**
  - create required **templates**


### Idea

I think, that **urls.py not need** for us. We can design urls automatically internally, based on defined Pages.

The **Page** - is a representation of real web page, that show something and handle user request. For example, this can be a list of products, and user can filter result to show the same page, but with filtered results.

    class Page(object):
      def get(self):
        # filter results, based on GET request variables
        return "page content"
      
      def post(self):
        # handle user request to modify something and redirect to result page
        # where we can show appropriate message

We can modify page behaviour with subclassing one Page to build another with similar things. For example, we can create general page behaviour and use it in multiple pages that subclass this one.

Page can be build from parts. This parts are standart set of classes, designed to solve some tasks:
 - show list of something
 - show details about something
 - show comments/ratings to something


### Project diagrams

*(this is old diagram for my old idea, and I will delete this soon)*

![Project diagram](https://raw.github.com/1st/webpages/master/rapidpy_framework_diagram.png "Project diagram")
