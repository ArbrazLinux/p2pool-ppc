import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'e5e9e8e6'.decode('hex')
P2P_PORT = 9901
ADDRESS_VERSION = 50
RPC_PORT = 9902
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'peercoin' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//210000
POW_FUNC = data.hash256
BLOCK_PERIOD = 600 # s
SYMBOL = 'PPC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Peercoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Peercoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.peercoin'), 'peercoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://chainz.cryptoid.info/ppc/block.dws'
ADDRESS_EXPLORER_URL_PREFIX = 'https://chainz.cryptoid.info/ppc/address.dws?'
TX_EXPLORER_URL_PREFIX = 'https://chainz.cryptoid.info/ppc/tx.dws?'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.001e7
