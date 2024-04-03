def list_check(lst):
    for item in lst:
  
        if not isinstance(item, list):
            return False
    
    
    return True