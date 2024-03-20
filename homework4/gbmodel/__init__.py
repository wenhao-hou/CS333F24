# gbmodel/__init__.py

model_backend = 'sqlite3'  # Default to 'sqlite3', but can be changed to 'pylist'

if model_backend == 'sqlite3':
    from .model_sqlite3 import SQLiteModel as Model
elif model_backend == 'pylist':
    from .model import PyListModel as Model
  # Ensure this file & class exist
else:
    raise ValueError("No appropriate database backend configured.")

appmodel = Model('entries.db') if model_backend == 'sqlite3' else Model()

def get_model():
    """
    Returns the model instance for the application.
    """
    return appmodel
