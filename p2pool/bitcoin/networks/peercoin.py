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
            (yield helper.check_block_header(bitcoind, '0000000032fe677166d54963b62a4677d8957e87c508eaa4fd7eb1c880cd27e3')) and # genesis block
            (yield helper.check_block_header(bitcoind, '000000000000bca54d9ac17881f94193fd6a270c1bb21c3bf0b37f588a40dbd7')) and # chk block
            (yield helper.check_block_header(bitcoind, 'd39d1481a7eecba48932ea5913be58ad3894c7ee6d5a8ba8abeb772c66a6696e')) and # chk block
            (yield helper.check_block_header(bitcoind, '27fd5e1de16a4270eb8c68dee2754a64da6312c7c3a0e99a7e6776246be1ee3f')) and # 99999 block
            (yield bitcoind.rpc_getblockchaininfo())['chain'] == 'main'
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
