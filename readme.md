# Requirements

I want to
* develop Python code in a TDD fashion
* automatically run unit tests on change of any source or test code.

This turns out to not be as simple as it sounds.  
I don't currently care about anything else (like deploying or publishing this code).

# Success
1. Install [conda](https://conda.io/docs/user-guide/install/index.html).
1. `git clone` and `cd` into this project
1. Modify `environment.yml` with appropriate env name. 
1. Run `conda env create`
1. Run `make test` to automatically run tests in [looponfailing mode](https://docs.pytest.org/en/3.0.0/xdist.html#running-tests-in-looponfailing-mode) and wait for changes.

## Test Discovery

According to [pytest's test discovery rules](https://docs.pytest.org/en/latest/goodpractices.html#conventions-for-python-test-discovery), tests have to
* be in a file named `test_*.py` or `*_test.py`
* either
  * be in a method named `test_*`
  * be in a [TestCase](https://docs.python.org/3/library/unittest.html#unittest.TestCase)

Note that there is some limited coupling to `pytest` in the way the tests are written. For example, running the builtin command `python -m unittest` in the project root will run all the tests written as [TestCases](https://docs.python.org/3/library/unittest.html#unittest.TestCase) but not those written as `test_*` methods.

## Setting Up A New Github Repo

After cloning this repo we need to get rid of the commit history. Having set up some new github repo "REPO_NAME", let's make a shiny new git history:

    rm -rf .git
    git init
    git remote add origin git@github.com:USER_NAME/REPO_NAME.git

# Compromises

Bridges will be crossed as necessary.

This project
* is something I'd like to evolve into an [auto-generator](http://yeoman.io/authoring/) for a Python project
* doesn't use `requirements.txt` because I use [conda](https://conda.io/docs/user-guide/tasks/manage-environments.html) as my default package manager
* is more than likely **not** [publishable to PyPi](https://packaging.python.org/tutorials/distributing-packages/#setup-py), due to
  * `__init__.py` in the tests folder, which I've read is [not recommended](https://stackoverflow.com/questions/29153922/pytest-and-why-avoid-init-file) -- but it **must** be there as of now!
  * missing a `setup.py` file
  * probably breaks a bunch of other rules for publishing packages.

# Future

As my requirements and knowledge of Python expand I will improve upon this project to further streamline my Pythonic process.