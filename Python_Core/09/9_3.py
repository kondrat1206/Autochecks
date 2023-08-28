def caching_fibonacci():
    cache = {}  # Словник для зберігання кешованих значень

    def fibonacci(n):
        if n in cache:
            return cache[n]
        
        if n <= 1:
            result = n
        else:
            result = fibonacci(n - 1) + fibonacci(n - 2)
        
        cache[n] = result
        return result
    
    return fibonacci