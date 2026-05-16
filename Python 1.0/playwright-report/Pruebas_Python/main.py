def google_search(query):
    """Simula una busqueda en goole"""
    if not query:
        raise ValueError("La consulta no puede ser vacia")
    results ={
        "python":["python.org", "tutorial python", "aprender python"],
        "java": ["java.com," "tutorial java", "Aprender java"],
        "javascrip": ["javascript.com", "tutorial javascript", "aprender javascript"],
    }
    return results.get(query.lower(),[])

print(google_search("python"))