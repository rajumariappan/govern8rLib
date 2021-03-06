import test_data
from notary_client import NotaryClient, NotaryException

try:
    notary_client = NotaryClient('./notaryconfig.ini', 'foobar')
    message = notary_client.get_server_pubkey()
    print(message)
except NotaryException as e:
    print("Code %s " % e.error_code)
    print(e.message)
