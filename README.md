WebPages - full-stack JS web framework
=====

Hello dear web developer!

I like the idea to use JavaScript on both sides - `front-end` and `back-end`. Yes, we can use `node.js` and frameworks like `backbone.js` and `express.js`. But JS syntax isn't what I like, especially spagetti-style with callbacks chain.

It's why appear this idea - create web framework that uses only `JavaScript`. But also I described a new syntax that can help to write more beautiful and understanble code. *(We continue discussing syntax)*


New syntax
-----

```python
# syntax mainly derived from Python languuage

# assign value
a, b, c = 1, 2, 3
a = n * 2
# syntax for lambda functions
func add(x, y): x + y
# define functions
func append(l, val):
    l.append(val)
    return true
```

```python
# callbacks chain (version 1: not flat)

func show_posts(request):
    try User.get(user_id=1) as user:
        if not user.is_active:
            raise Exception("Access denied")
        with Blog.getall(author=user) as posts:
            blog_posts = posts
    catch msg, code:
        raise Exception("User doesn't found")
    return render('posts.html', {'posts': blog_posts})

# converts to JS code
# ? ? ?
```

```python
# callbacks chain (version 2: flat list)

func show_posts(request):
    user = User.get(user_id=1)
    if not user.is_active:
        raise Exception("Access denied")
    posts = Blog.getall(author=user)
    return render('posts.html', {'posts': posts})

# converts to JS code (something like this)

function show_posts(request, response) {
    wait(function () {
      user = User.get(user_id=1)
    }).then(function (next, err) {
      if (! user.is_active) {
        throw "Access denied";
      }
    }).then(function (next, err) {
      posts = Blog.getall(author=user);
    }).then(function (next, err) {
      return render('posts.html', {'posts': posts});
    }).then(function (next, err) {
      response();
    });
}
```




Tasks and bugs
-----

Find list of tasks and bug reports in our [issues list](/webpages/webpages/issues). Also you can add your bug report or proposition.


Contact us
-----

Join to us on [Facebook](https://www.facebook.com/WebPagesFramework)
