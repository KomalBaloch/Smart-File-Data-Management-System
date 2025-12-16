from datetime import datetime

# Logger decorator
def logger(func):
    """Decorator to log function calls"""
    def wrapper(*args, **kwargs):
        print(f"[LOG] {func.__name__} called at {datetime.now()}")
        return func(*args, **kwargs)
    return wrapper
