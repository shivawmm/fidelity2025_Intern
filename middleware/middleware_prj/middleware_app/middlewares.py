def middleware(get_response):
    print("First time initailized")
    def my_function(request):
        print("process before request")
        res = get_response(request)
        print("after request process")
        return res
    return my_function

