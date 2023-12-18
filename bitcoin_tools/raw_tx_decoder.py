from bitcoinlib.transactions import Transaction

def raw_transaction_to_json(raw_transaction_hex):
    # 解析原始交易十六进制字符串
    try:
        raw_transaction_bytes = bytes.fromhex(raw_transaction_hex)
        transaction = Transaction.parse(raw_transaction_bytes)

        # 构建JSON格式的交易数据

        return transaction.as_json(), None
    except Exception as e:
        return None, f"Error in raw_transaction_to_json: {e}"
