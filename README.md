WebPages - incredibly ***new*** python web framework
=======

***
*I think, that most of web frameworks was inspired by Ruby on Rails approach. I like RoR, Django, Cake PHP - these are good projects. But I have a new idea how to do web programming more easy.*
***


Foreword
--------

I was thinking about how to teach my nephew to create web applications. The boy were 14 years old, and his hasn't experience in programming yet.

My goal was to tell about how to write web applications on python. But I was found that I need to tell a lot of basic information about:
 - *hirst of all* - help to install Ubuntu Linux to his PC
 - *basic concepts of python* language (this is not hard)
 - *what is django* and how to create new empty project
 - how to *change setings.py and run project*
  - what is *regular expressions* (to build urls.py)
  - how to *enable admin app* and show admin site
 - how to *create new app*
  - describe *models*
  - design *urls.py*
  - add new app to *INSTALLED_APPS* in settings.py
  - create new controller in *views.py*
  - create required *templates*
 - what is *html, css, java srcipt*


Idea
--------

I think, that **urls.py not need** for us. We can design urls automatically internally, based on defined Pages.

The **Page** - is a representation of real web page, that show something and handle user request. For example, this can be a list of products, and user can filter result to show the same page, but with filtered results.

    class Page(object):
      def get(self):
        # filter results, based on GET request variables
        return "page content"
      
      def post(self):
        # handle user request to modify something and redirect to result page
        # where we can show appropriate message

We can modify page behaviour with subclassing one Page to build another, with similar things. For example, we can create general page behaviour and use it in multiple pages that subclass this one.


Project diagrams
--------

*(this is onl diagram for my old idea, and I will delete this soon)*

![Project diagram](https://raw.github.com/1st/webpages/master/rapidpy_framework_diagram.png "Project diagram")
