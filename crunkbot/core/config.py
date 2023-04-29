import os
import typing as t
import yaml


class Config(dict):
    def __init__(self, root_path: str, defaults: t.Optional[dict] = None) -> None:
        super().__init__(defaults or {})
        self.root_path = root_path
        self.config: dict

    def from_env(self, var_name: str = "CBCONFIG") -> bool:
        env_var = os.environ.get(var_name)
        if not env_var:
            raise RuntimeError(
                f"The environment variable {var_name!r} is not set"
                " therefore configuration could not be loaded. Set"
                " this variable and ensure it points to a valid config"
                " file"
            )
        return self.load_config(env_var)

    def load_config(self, filename: str = "config.yaml") -> bool:
        filename = os.path.join(self.root_path, filename)
        try:
            with open(filename, "r") as config_file:
                conf = yaml.safe_load(config_file)
        except OSError as e:
            e.strerror = f"Unable to load configuration file ({e.strerror})"
            raise
        self.config = conf
        return True
    
    
        



    