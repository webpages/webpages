

def User(request):
    """
    Restore user session based on active Session.

    Add `request.user` as LazyUser to fetch used data
    from database only when we access to `request.user`
    first time.
    """
    pass
