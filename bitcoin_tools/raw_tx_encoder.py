from bitcoinlib.transactions import Transaction
import json

def json_to_raw_transaction(json_tx):
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
