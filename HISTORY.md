Project history
====


The initial idea for WebPages
----

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
