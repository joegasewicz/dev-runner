# Dev Runner
Watches for file changes & runs tasks against your Python code.

### Quickstart

```python
from bobtail import BobTail
from bobtail_logger import BobtailLogger
from dev_runner import DevRunner, MyPyTask, DevServerTask

from tests.routes import HomeRoute


routes = [
    (HomeRoute(), "/")
]

if __name__ == "__main__":
    bobtail = BobTail(routes=routes)
    bobtail.use(BobtailLogger())
    dr = DevRunner(
        path=".",
        tasks=[
            MyPyTask(path="routes", mypy_file="mypy.ini"),
            DevServerTask(wsgi_app=bobtail),
        ]
    )
    dr.watch()
```

### Tasks
- **Mypy** ✅
- **SimpleHttpServer** ✅
- **Pylint** *TODO*
- **Pytest** *TODO*
- **ISort** *TODO*
- **Flake8** *TODO*
- **Bandit** *TODO*
- **Sphinx** *TODO*
- **Custom Task** *TODO*


