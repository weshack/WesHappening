import logging,sys
sys.path.insert(0, '/srv/weshack/WesHappening/')
logging.basicConfig(stream=sys.stderr)
from weshappening import app as application
application.secret_key = 'this is a secret key for awafaweofawoefaewifiowef'
