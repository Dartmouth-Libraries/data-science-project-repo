# Project package

As your project grows, you will notice that you find yourself using the same code in different places, e.g., defining the same variables to point to your data folder, or using the same helper functions to clean up some strings. This can be greatly simplified by collecting this code in a lightweight Python package, that you can install into your project folder and then use just like any other package installed through PyPi.

So instead of repeating `data_dir = "../data/"` in every notebook, you define it only once in the package and then import that variable like so:

```python
from projectname.config import data_dir
```

The same is true for any functions you use repeatedly, e.g.:

```python
from projectname.utils import my_popular_function
```

Having only a single point of definition is extremely helpful, since if you later on find a bug in your that function or want to change how it works, you can just do it in one place and don't need to worry about missing some copy in a notebook somewhere.

You can install your custom package with `pip` from the root folder of the project repo:

```bash
pip install --editable ./projectname
```
Mind the `./`, which tells `pip` to not go online to find this package but use the local folder of this name. You should provide the flag `--editable` to avoid having to re-install the package everytime you make a change to its source code.