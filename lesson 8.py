"""
import logging


logging.basicConfig(level=logging.ERROR, filename="error.log", format="%(asctime)s - %(levelname)s - %(message)s")

def divide(a,b):
    try:
        result = a/b
        return result
    except ZeroDivisionError as e:
        logging.error(f"Division by zero error: {e}")

divide(10,0)
"""



"""
>>> 2+2
5
"""
if __name__ == "__Less_8__":
    import doctest
    doctest.testmod()





