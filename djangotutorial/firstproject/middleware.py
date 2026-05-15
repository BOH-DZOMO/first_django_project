import time

class LoadTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.perf_counter()
        response = self.get_response(request)
        end_time = time.perf_counter()
        load_time =  end_time - start_time
        print (f"page loaded in {load_time:-.4f} seconds")
        return response
    

