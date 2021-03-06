import os
IPFS_URL = {
    'url': 'ipfs.singularitynet.io',
    'port': '80',
    'protocol': 'http'
}
NETWORKS = {
    999: {
        'name': 'TEST',
        'ws_provider': 'wss://kovan.infura.io/ws',
        'http_provider': 'https://kovan.infura.io',
        'db': {'DB_HOST': '127.0.0.1',
               'DB_USER': 'unittest_root',
               'DB_PASSWORD': 'unittest_pwd',
               'DB_NAME': 'unittestdb',
               'DB_PORT': 3306
               }
    }
}
MPE_EVTS = ['ChannelOpen', 'ChannelClaim', 'ChannelSenderClaim', 'ChannelExtend', 'ChannelAddFunds']
REG_EVTS = ['OrganizationCreated', 'OrganizationModified', 'OrganizationDeleted', 'ServiceCreated',
            'ServiceMetadataModified', 'ServiceTagsModified', 'ServiceDeleted']
COMMON_CNTRCT_PATH = '../node_modules/singularitynet-platform-contracts'
REG_CNTRCT_PATH = COMMON_CNTRCT_PATH + '/abi/Registry.json'
MPE_CNTRCT_PATH = COMMON_CNTRCT_PATH + '/abi/MultiPartyEscrow.json'
REG_ADDR_PATH = COMMON_CNTRCT_PATH + '/networks/Registry.json'
MPE_ADDR_PATH = COMMON_CNTRCT_PATH + '/networks/MultiPartyEscrow.json'
SLACK_HOOK = {
    'hostname' : '',
    'port': 443,
    'path': '',
    'method': 'POST',
    'headers': {
        'Content-Type': 'application/json'
    }
}
EVNTS_LIMIT = "100"
SRVC_STATUS_GRPC_TIMEOUT = 10
