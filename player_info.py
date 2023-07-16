from ei import get_first_contact
import os
import sys
import json
from datetime import datetime
from egg_utils import to_readable, to_rank

ei_user_id = os.getenv('EGGINC_ID')

if not ei_user_id:
    print("Env EGGINC_ID should be set")
    sys.exit(1)

r = get_first_contact(ei_user_id)

pe = int(r['backup']['game']['eggsOfProphecy'])
se = r['backup']['game']['soulEggsD']
prestiges = int(r['backup']['stats']['numPrestiges'])
eb = 100 * se * 1.5 * 1.1 ** pe
timestamp = datetime.utcnow().isoformat()

# Dump current stats
to_add = {
    'prestiges': prestiges,
    'se': se,
    'se_readable': to_readable(se),
    'eb': eb,
    'eb_readable': to_readable(eb),
    'pe': pe,
    'rank': to_rank(eb),
    'timestamp': timestamp,
}

print(json.dumps(to_add, indent=2))
