from functools import wraps
import time

def retry(max_tries):
    def decorator(func):

        @wraps(func)
        async def wrapper(*args,**kwargs):
            for attempt in range(max_tries):
                try:
                    return await func(*args,**kwargs)
                except Exception as e:
                    if attempt == max_tries -1:
                        raise e

        return wrapper
    
    return decorator

def log_execution(func):

    @wraps(func)
    async def wrapper(*args,**kwargs):
        print(f"Starting {func.__name__}")

        try:
            result=await func(*args,**kwargs)
            print(f"Completed {func.__name__}")
            return result
        except Exception as e:
            print(f"Failed {func.__name__}")
            raise(e)
        
    return wrapper

def timer(func):
    
    @wraps(func)
    async def wrapper(*args,**kwargs):
        
        start=time.time()
        result=await func(*args,**kwargs)
        end=time.time()

        print(f"{func.__name__} took {end-start:.2f} seconds ")

        return result
    
    return wrapper