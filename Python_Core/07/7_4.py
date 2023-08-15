def is_integer(s: str):
    s = s.strip()
    
    if len(s) == 0:
        return False
    if s.startswith('+') or s.startswith('-'):
        s = s[1:]  # Remove the leading "+" or "-"
    return s.isdigit()