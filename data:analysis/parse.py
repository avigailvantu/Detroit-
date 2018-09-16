import json
import pdb

nb1 = json.loads(open('./detroit_open_demolitions.ipynb').read())
nb2 = json.loads(open('./python_crash_course.ipynb').read())

nb1["cells"] = nb1["cells"][0:1] + nb2["cells"] + nb1["cells"][2:]

print json.dumps(nb1, indent=4, separators=(',', ': '))
