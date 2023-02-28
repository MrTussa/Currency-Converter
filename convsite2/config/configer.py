from dataclasses import dataclass
from environs import Env

env = Env()
env.read_env(override=True)

@dataclass
class MainConfig:
    DBNAME: str
    ADMINS: list[int]

CONFIGER = MainConfig(
    DBNAME = env.str('DBNAME'),
    ADMINS = list(map(int, env.list('ADMINS')))
)