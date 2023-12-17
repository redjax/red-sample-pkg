from dynaconf import Dynaconf

settings = Dynaconf(
    root_path="config",
    envvar_prefix="APP",
    environments=True,
    settings_files=["settings.toml", ".secrets.toml"],
)

database_settings = Dynaconf(
    root_path="config/db",
    environments=True,
    envvar_prefix="DB",
    settings_files=["settings.toml", ".secrets.toml"],
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
