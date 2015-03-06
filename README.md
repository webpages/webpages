WebPages - python web framework
===

Hello.

This project is based on good ideas from **Ruby on Rails** and **Django** web frameworks. Also I wish to add asynchronous code execution like in **Tornado** and **Node.js**. I tried to simplify project structure to make project as easy as it possible. I believe that you find it useful.


Documentation
---

Read full project [documentation](docs/). You can help us to improve our docs!


Key decisions
---

 * project contains set of MVC objects *(don't have reusable applications, like in Django)*
 * project has own settings file and can redefine default settings for models and controllers. Settings file contains grouped configuraions per component (instead of global names, like it's used in **Django**)
 * project can be generated from command-line
 * each MVC object can be generated from command-line. To add data model - we use command-line and it will create appropriate data model, controller with actions and templates for this new data model (like in **Ruby on Rails**)
 * data model migration is easy. When we rename field or add new - we do it in command-line and it save our changes to migration file
 * automatic routers. We don't need to control the urls that we use and pay attention to use unique naming without overlaping between multiple urls. Each controller has own prefix `controller_name/action_name/...` to handle user requests
 * all data come to database only via forms (like in **Django**, but forms is a part of model). It's important, because if we need to prevent save model with some field values, we need to use Forms in Django, and we can save this model without validation without use Form, but use Model instance instead
 * user-defined middleare classes are supported
 * [ORM](https://github.com/webpages/orm) *(it's our separate project)* is must have. But with simplified syntax like this `User.first` or `User.all.filter((F.name='Tony' and F.age.in(10, 20, 30)) or F.roles.name='admins')`
 * templates syntax is very similar to python, without closing tags (styled with indentation, like in **Slim for Ruby**)

System requirements
---

 * to `return` something from function that contains `yield` keyword - we need to use **Python 3.3**


Roadmap
---

- [x] Create facebook group to have feedback from developers
- [ ] Run web server on top of webOb or similar
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
