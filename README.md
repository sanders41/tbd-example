# Data Triad CI/CD

This repository is for the Data Triad CI/CD example. In this example we will be using GitHub Actions, but there are also other options available such as [circleci](https://circleci.com/) and [Travis CI](https://travis-ci.com/).

The official github action for Python can be found [here](https://github.com/actions/setup-python), and the official github actions main repository for all actions is [here](https://github.com/actions). In addition to the official repository there are a lot of other pre-built actions available that can be used. [This](https://github.com/sdras/awesome-actions) "awesome list" has a lot of options, and many more can be found with a simple Google search.

## CI/CD Files

The files defining what is run for CI/CD are found in the [.github/workflows](https://github.com/sanders41/tbd-example/tree/main/.github/workflows) directory.

In these example files linting and testing (the CI part) are controlled by the linting.yaml and testing.yaml files and will be run automatically any time there is either a push to the main branch, or a pull request to the main branch is created. For the testing, tests will be run on Mac, Ubuntu Linux, and Windows, and each operating system will test with Python 3.7, 3.8, and 3.9.

![CI Running](https://raw.githubusercontent.com/sanders41/tbd-example/main/images/ci-running.png)

Deployment (the CD part) is controlled by the pypi_publish.yaml file and will happen automatically any time a new relase is created with a tag in the format of v\*.\*.\*. For example creating a release with a tag of v0.1.0 will trigger deployment.

![Create Release](https://raw.githubusercontent.com/sanders41/tbd-example/main/images/create-release.png)

![Tag Release](https://raw.githubusercontent.com/sanders41/tbd-example/main/images/tag.png)

## Adding Secrets

If you need to include passwords or other information that should not be viewable they can be included in the secrets section of the repository. To get there:

1. Click on setting

    ![Settings](https://raw.githubusercontent.com/sanders41/tbd-example/main/images/settings.png)

2. Click on secrets

    ![Secrets](https://raw.githubusercontent.com/sanders41/tbd-example/main/images/secrets.png)

3. Click on New Repository Secret

    ![New Repository Secret](https://raw.githubusercontent.com/sanders41/tbd-example/main/images/new-secret.png)

4. Give the secret a name and paste in the value to be used for the secret. The name you use for the secret becomes the variable name that will be used when you want to reference the secret in an action.

    ![Secret Information](https://raw.githubusercontent.com/sanders41/tbd-example/main/images/secret-info.png)

    ![Secret in YAML file](https://raw.githubusercontent.com/sanders41/tbd-example/main/images/secret-in-yaml.png)

## Dependency Management

This repositry uses [Poetry](https://python-poetry.org/) for dependency management and deployment. If instead you want use pip the work flow files can be updated for that. As an example, assuming you have a requirements.txt file, linting.yaml file would change to:

```yaml
name: Linting

on:
  push:
    branches:
    - main
  pull_request:
    branches:
    - main
jobs:
  linting:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    - name: Install Dependencies
      run: |
        python3 -m pip install -U pip
        python3 -m pip install -r requirements.txt
    - name: Isort check
      run: |
        python3 -m isort tbd_example tests --check-only
    - name: Black check
      run: |
        python3 -m black tbd_example tests --check
    - name: Lint with flake8
      run: |
        # stop the build if there are Python syntax errors or undefined names
        python3 -m flake8 tbd_example tests --count --select=E9,F63,F7,F82 --show-source --statistics
        # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
        python3 -m flake8 tbd_example tests --count --exit-zero --max-complexity=10 --max-line-length=100 --statistics
    - name: mypy check
      run: |
        python3 -m mypy tbd_example
```
