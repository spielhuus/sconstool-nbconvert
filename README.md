# SCons nbconvert tool

## Basics

This tool can be used to convert jupyter pages with nbconvert.

## Install

Installing it, requires you to copy (or, even better: checkout) the contents of the
package's ``nbconvert`` folder to

- ``/path_to_your_project/site_scons/site_tools/nbconvert``", if you need the `nbconvert` Tool in one project only, or
- ``/user/share/scons/site_scons/site_tools/nbconvert``, for a system-wide installation under your current login.

For more infos about this, please refer to 

* the SCons User's Guide, sect. "Where to put your custom Builders and Tools" and

## Activate the tool

Create a build environment with the nbconvert builder

```python
env = Environment(tools=['nbconvert'], 
        NBCONVERT_ENVIRONMENT_VARS={'flags': ['execute', 'no-input'],
                  'to': 'html',
                  'log-level': 'CRITICAL', 
                  'ExecutePreprocessor.kernel_name': 'python3',
                  'HTMLExporter.exclude_anchor_links': True,
                  'template': 'classic'})
```

## Configuration

the `NBCONVERT_ENVIRONMENT_VARS` must contain a list of flags
allowed flags are `[execute] [allow-errors] [inplace] [clear-output] [no-prompt] [no-input] [show-input]`

It can also contain a list of build options.
For a list of options visit the [nbconvert documentation](https://nbconvert.readthedocs.io/)

```python
env.nbconvert('rendered_templ.html', os.path.join('test.ipynb'))
```

## Templates

There is a template folder in this repository. It can be used to convert the notebooks to hugo 
pages. It will allow metadata in the jupyter notebook for the `FrontMatter` creation. Jupyterlab 
is needed to edit this data. The `FrontMatter` section can be added before the jupyter metadata 
starting with `kernelspec`.

```json
{
    "FrontMatter": {
        "author": "spielhuus",
        "category": "article",
        "date": "2021-01-10",
        "tag": "grundlage",
        "title": "cmos",
        "draft": True
    },
    
    "kernelspec": {
        ...
    },
    "language_info": {
        ...
    }
}
```