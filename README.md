# red-sample-pkg

⚠️ DON'T USE THIS PACKAGE ⚠️

This is an example package, used to test workflows/Github Actions, packaging techniques, publishing, & more.

It will not be maintained for stability, security, or usefulness.

# Notes

## Dynaconf

This app uses [`Dynaconf`](https://www.dynaconf.com/) for configuration. The package is built in a way to allow for environments (set an environment variable, `ENV_FOR_DYNACONF`, to control which settings group to use) and modular configurations.

### Using configuration .toml files

The main/root configuration is defined in [`config/settings.toml`](./src/config/settings.toml). These settings can be overridden with environment variables (prepended with `APP_`), or by copying `settings.toml` to `settings.local.toml`. Dynaconf will use `*.local.toml` files, if they exist.

**NOTE**: I have had issues with Dynaconf preferring settings defined in a `.local.toml` file, even when the same environment variables are declared. I am still researching if a `.local.toml` file in a Docker container, for example, is read before environment variables.

### Creating config modules

New settings modules (i.e. a `db_settings` or `logging_settings`) can be created by creating a new directory in [`config/`](./src/config). For example, to create a `db_settings` Dynaconf object:

- Create a directory `config/db`
- Create `config/db/settings.toml`
  - (Optional) create `config/db/.secrets.toml`
- (Optional) to use environments (`dev`, `prod`, etc), use this as the basis for the new `settings.toml` and `.secrets.toml` file:
  -
  ```
  ## settings.toml / .secrets.toml

  [default]

  [dev]

  [prod]

  ```
- Create some variables, i.e. `db_type`:
  -
  ```
  ## db/settings.toml

  [default]

  db_type = "postgres"

  [dev]

  db_type = "sqlite"

  [prod]

  ```
- In the Dynaconf [`config.py`](./src/config.py) file, create a new settings loader called `db_settings`
  -
  ```
  ## config.py

  ...

  database_settings = Dynaconf(
    ## Set the root path for Dynaconf to search for settings.toml file
    root_path="config/db",
    ## Use environments (default/dev/prod)
    environments=True,
    ## To override db_settings with env variables,
    #  prepend all env vars with "DB_", i.e. "DB_TYPE=mysql"
    envvar_prefix="DB",
    ## Settings file patterns to match. Will also match *.local.toml
    settings_files=["settings.toml", ".secrets.toml"],
  )
  ```
