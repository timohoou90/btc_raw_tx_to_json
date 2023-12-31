from bitcoin_tools import raw_tx_decoder, raw_tx_encoder

# 示例用法
raw_transaction_hex = "0100000001bafe2175b9d7b3041ebac529056b393cf2997f7964485aa382ffa449ffdac02a000000008a473044022013d212c22f0b46bb33106d148493b9a9723adb2c3dd3a3ebe3a9c9e3b95d8cb00220461661710202fbab550f973068af45c294667fc4dc526627a7463eb23ab39e9b01410479be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8ffffffff01b0a86a00000000001976a91401b81d5fa1e55e069e3cc2db9c19e2e80358f30688ac00000000"
decoded_transaction_json, err = raw_tx_decoder.raw_transaction_to_json(raw_transaction_hex)
print(decoded_transaction_json)

in_json = '''{
    "txid": "52309405287e737cf412fc42883d65a392ab950869fae80b2a5f1e33326aca46",
    "hash": "52309405287e737cf412fc42883d65a392ab950869fae80b2a5f1e33326aca46",
    "version": 1,
    "size": 223,
    "vsize": 223,
    "weight": 892,
    "locktime": 0,
    "vin": [
        {
            "txid": "2ac0daff49a4ff82a35a4864797f99f23c396b0529c5ba1e04b3d7b97521feba",
            "vout": 0,
            "scriptSig": {
                "asm": "3044022013d212c22f0b46bb33106d148493b9a9723adb2c3dd3a3ebe3a9c9e3b95d8cb00220461661710202fbab550f973068af45c294667fc4dc526627a7463eb23ab39e9b[ALL] 0479be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8",
                "hex": "473044022013d212c22f0b46bb33106d148493b9a9723adb2c3dd3a3ebe3a9c9e3b95d8cb00220461661710202fbab550f973068af45c294667fc4dc526627a7463eb23ab39e9b01410479be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8"
            },
            "sequence": 4294967295
        }
    ],
    "vout": [
        {
            "value": 0.0699,
            "n": 0,
            "scriptPubKey": {
                "asm": "OP_DUP OP_HASH160 01b81d5fa1e55e069e3cc2db9c19e2e80358f306 OP_EQUALVERIFY OP_CHECKSIG",
                "desc": "addr(1A6Ei5cRfDJ8jjhwxfzLJph8B9ZEthR9Z)#z60wy0ua",
                "hex": "76a91401b81d5fa1e55e069e3cc2db9c19e2e80358f30688ac",
                "address": "1A6Ei5cRfDJ8jjhwxfzLJph8B9ZEthR9Z",
                "type": "pubkeyhash"
            }
        }
    ]
}'''
j,e = raw_tx_encoder.json_to_raw_transaction(in_json)
print(j)
print(e)
