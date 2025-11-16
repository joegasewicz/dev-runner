# Dev Runner

### Examples

```python
from dev_runner.dev_runner import DevRunner
from dev_runner.tasks import MyPyTask

dr = DevRunner(
    path="examples",
    tasks=[
        MyPyTask(path="examples"),
    ])

if __name__ == "__main__":
    dr.watch()

```