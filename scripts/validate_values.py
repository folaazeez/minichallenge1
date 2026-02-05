import yaml
import sys

def fail(msg:str,code:int=1)->None:
    print(f"ERROR: {msg}")
    sys.exit(code)

yaml_file = sys.argv[1] if len(sys.argv) > 1 else "values.yaml"

try:
    with open(yaml_file,"r") as f:
        values = yaml.safe_load(f) or {}
except FileNotFoundError:
    fail("values.yaml not found")
except yaml.YAMLError as e:
    fail(f"Invalid YAML: {e}")
        
#never assume the key exists
replicas  = values.get("replicaCount",1)
env = values.get("environment")

if not isinstance(replicas,int):
    fail("replicaCount must be an integer")

if not env:
    fail("environment is missing")

if env == "prod" and replicas < 3:
        print("ERROR: prod requires at least 3 replicas")                                     
        sys.exit(1)
    
print ("File validated successfully ✅")
sys.exit(0)
