from bitcoinlib.transactions import Transaction
import json

def json_to_raw_transaction():
        # 从JSON数据中重建交易对象
        transaction = Transaction()
        transaction.locktime = 0

        # 处理输入
        transaction.add_input(prev_txid="2ac0daff49a4ff82a35a4864797f99f23c396b0529c5ba1e04b3d7b97521feba",output_n=0,unlocking_script=b'473044022013d212c22f0b46bb33106d148493b9a9723adb2c3dd3a3ebe3a9c9e3b95d8cb00220461661710202fbab550f973068af45c294667fc4dc526627a7463eb23ab39e9b01410479be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8')
        transaction.add_output(value=6990000,lock_script=b'76a91401b81d5fa1e55e069e3cc2db9c19e2e80358f30688ac')

        print(transaction.as_json())

        # 返回原始交易的十六进制表示
        return transaction.raw_hex()
        # 处理异常，这里简单地打印错误信息，你可以根据需要进行其他处理

def json_to_raw_transactioni_1(json_tx):
    try:
        # 从JSON数据中重建交易对象
        transaction = Transaction()
        
        tx_dict = json.loads(json_tx) 
        transaction.locktime = tx_dict.get("locktime",0)
        for vin in tx_dict.get("vin", []):
            transaction.add_input(prev_txid=vin.get("txid"),output_n=vin.get("vout",0),unlocking_script=bytes.fromhex(vin["scriptSig"].get("hex","")))

        for vout in tx_dict.get("vout", []):
            transaction.add_output(value=vout.get("value",0)*100000000,lock_script=bytes.fromhex(vout["scriptPubKey"].get("hex","")))

        print(transaction.as_json())
        # 返回原始交易的十六进制表示
        return transaction.raw_hex(), None
        # 处理异常，这里简单地打印错误信息，你可以根据需要进行其他处理
    except Exception as e:
        return None, f"Error in raw_transaction_to_json: {e}"

#raw_transaction_hex = json_to_raw_transaction()
#
#if raw_transaction_hex:
#    print(f"Raw Transaction: {raw_transaction_hex}")
#else:
#    print("Failed to convert JSON to raw transaction.")
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
j,e = json_to_raw_transactioni_1(in_json)
print(j)
print(e)
