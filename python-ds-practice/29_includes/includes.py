def includes(collection, sought, start=None):
    if isinstance(collection, dict):
        return sought in collection.values()
    return sought in collection[start:] if start else sought in collection