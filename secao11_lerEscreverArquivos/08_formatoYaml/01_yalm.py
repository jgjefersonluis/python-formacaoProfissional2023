from yaml.loader import Loader
import yaml
dtname = None
with open("config.yaml") as f:
  data = yaml.load(f,Loader=yaml.FullLoader)
  dtname = data['cloud']['provider']
print(dtname)
