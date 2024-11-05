# Furious API
FastAPI extensions

What we want for FastAPI? 
- for sure
    - SQLAlchemy setup
    - mongo setup
    - manage.py shell like tool
    - notebooks
    - celery setup
    - migrations
    - management commands 
    - logging
- additionally
    - mongo setup


This leads us to a need for CLI:
- furious run app
- furious run celery
- furious shell
- furious notebook [nb]
- furious migrate // probably not needed because alembic can do the same
- furious mkdocker

This also leads us to code interface:

```python
from furious import AppDatabase

```

