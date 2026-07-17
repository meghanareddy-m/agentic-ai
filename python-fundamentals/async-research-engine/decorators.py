def retry(max_tries):
    def decorator(func):
        async def wrapper(*args,**kwargs):
            for attempt in range(max_tries):
                try:
                    return await func(*args,**kwargs)
                except Exception as e:
                    if attempt == max_tries -1:
                        raise e

        return wrapper
    
    return decorator