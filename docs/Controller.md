Controllers in WebPages framework
===

Controller responsible for business logic of application.


Request
---

When user requests web page - we search appropriate controller and run his action (class method). If user requests page `/blog/create` than we find `controllers/blog.py` and call `Blog.create(request)` method. Where `request = Request()` with all filled data from user request.

We have some magic to simplify development. When user make `GET/POST/PUT/DELETE` request than we try to find requested action that ends with request method type. For example, when you open page `/blog/create` we call `Blog.create()` action. When user send form with `method="POST"` to the same page than we try to call `Blog.create_post()` action. If this action doesn't exists - we call `Blog.create()` action instead. This add freedom to simplify code and divide it to small parts that responsible for one action with given input.
