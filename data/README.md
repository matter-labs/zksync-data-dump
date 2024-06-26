

## Blocks
| Attribute         | Type          | Description                                                                                           |
|-------------------|---------------|-------------------------------------------------------------------------------------------------------|
| hash              | str           | Unique identifier for the block.                                                                      |
| parentHash        | str           | Unique identifier of the parent block.                                                                |
| sha3Uncles        | str           | SHA-3 hash of the uncles' block headers.                                                              |
| miner             | str           | Address of the miner who mined the block.                                                             |
| stateRoot         | str           | Root hash of the state trie.                                                                          |
| transactionsRoot  | str           | Root hash of the transaction trie.                                                                    |
| receiptsRoot      | str           | Root hash of the receipts trie.                                                                       |
| number            | i64           | Block number or height.                                                                               |
| l1BatchNumber     | str           | L1 batch number, related to the sequence of batches submitted to Layer 1 in zkRollup systems.         |
| gasUsed           | i64           | Total amount of gas used by all transactions in the block.                                            |
| gasLimit          | i64           | Maximum amount of gas that can be used by all transactions in the block.                              |
| baseFeePerGas     | i64           | Base fee per unit of gas.                                                                             |
| extraData         | str           | Extra data included by the miner in the block.                                                        |
| logsBloom         | str           | Bloom filter for the logs of the block.                                                               |
| timestamp         | i64           | Unix timestamp of when the block was mined.                                                           |
| l1BatchTimestamp  | str           | Timestamp of the L1 batch, related to the zkRollup system.                                            |
| difficulty        | i64           | Difficulty target for mining the block.                                                               |
| totalDifficulty   | i64           | Cumulative difficulty of the blockchain up to and including this block.                               |
| sealFields        | list[null]    | Seal fields containing proof-of-work or proof-of-stake information.                                   |
| uncles            | list[null]    | Uncle blocks that were mined but not included in the main chain.                                      |
| size              | i64           | Size of the block in bytes.                                                                           |
| mixHash           | str           | Hash used in the mining process to prove that enough computational work has been performed.           |
| nonce             | str           | Value used in the mining process to find a valid block hash.                                          |


## Transactions
| Attribute                | Type  | Description                                                                 |
|--------------------------|-------|-----------------------------------------------------------------------------|
| blockHash                | str   | Unique identifier of the block containing the transaction.                  |
| blockNumber              | i64   | Block number or height containing the transaction.                          |
| chainId                  | i64   | Identifier of the blockchain network.                                       |
| from                     | str   | Address of the sender of the transaction.                                   |
| gas                      | i64   | Amount of gas provided for the transaction.                                 |
| gasPrice                 | i64   | Price per unit of gas the sender is willing to pay.                         |
| hash                     | str   | Unique identifier for the transaction.                                      |
| input                    | str   | Data sent along with the transaction.                                       |
| l1BatchNumber            | str   | L1 batch number related to the transaction in zkRollup systems.             |
| l1BatchTxIndex           | str   | Index of the transaction in the L1 batch.                                   |
| maxFeePerGas             | i64   | Maximum fee per unit of gas.                                                |
| maxPriorityFeePerGas     | i64   | Maximum priority fee per unit of gas.                                       |
| nonce                    | i64   | Number of transactions sent by the sender prior to this one.                |
| r                        | str   | First part of the ECDSA signature.                                          |
| s                        | str   | Second part of the ECDSA signature.                                         |
| to                       | str   | Address of the receiver of the transaction.                                 |
| transactionIndex         | i64   | Index of the transaction within the block.                                  |
| type                     | i64   | Type of transaction.                                                        |
| v                        | f64   | Recovery id of the ECDSA signature.                                         |
| value                    | str   | Amount of cryptocurrency being transferred in the transaction.              |


## Transaction receipts
| Attribute              | Type  | Description                                                                   |
|------------------------|-------|-------------------------------------------------------------------------------|
| blockHash              | str   | Unique identifier of the block containing the transaction.                    |
| blockNumber            | i64   | Block number or height containing the transaction.                            |
| contractAddress        | str   | Address of the contract created by the transaction, if applicable.            |
| cumulativeGasUsed      | i64   | Total amount of gas used when the transaction was executed in the block.      |
| effectiveGasPrice      | i64   | Actual price per unit of gas paid.                                            |
| from                   | str   | Address of the sender of the transaction.                                     |
| gasUsed                | i64   | Amount of gas used by the transaction.                                        |
| l1BatchNumber          | str   | L1 batch number related to the transaction in zkRollup systems.               |
| l1BatchTxIndex         | str   | Index of the transaction in the L1 batch.                                     |
| logsBloom              | str   | Bloom filter for the logs of the transaction.                                 |
| root                   | str   | State root after the transaction is executed.                                 |
| status                 | i64   | Status of the transaction (1 for success, 0 for failure).                     |
| to                     | str   | Address of the receiver of the transaction.                                   |
| transactionHash        | str   | Unique identifier for the transaction.                                        |
| transactionIndex       | i64   | Index of the transaction within the block.                                    |
| type                   | i64   | Type of transaction.                                                          |

## Transaction logs
| Attribute             | Type  | Description                                                      |
|-----------------------|-------|------------------------------------------------------------------|
| address               | str   | Address of the contract that generated the log.                  |
| blockHash             | str   | Unique identifier of the block containing the transaction.       |
| blockNumber           | i64   | Block number or height containing the transaction.               |
| data                  | str   | Data contained in the log.                                       |
| l1BatchNumber         | str   | L1 batch number related to the log in zkRollup systems.          |
| logIndex              | i64   | Index of the log within the block.                               |
| logType               | null  | Type of log.                                                     |
| removed               | bool  | Indicates whether the log was removed (true) or not (false).     |
| transactionHash       | str   | Unique identifier for the transaction.                           |
| transactionIndex      | i64   | Index of the transaction within the block.                       |
| transactionLogIndex   | str   | Index of the log within the transaction.                         |
| topics_0              | str   | First topic of the log.                                          |
| topics_1              | str   | Second topic of the log.                                         |
| topics_2              | str   | Third topic of the log.                                          |
| topics_3              | str   | Fourth topic of the log.                                         |


## L2 to L1 logs
| Attribute             | Type  | Description                                                         |
|-----------------------|-------|---------------------------------------------------------------------|
| blockHash             | str   | Unique identifier of the block containing the log.                  |
| blockNumber           | str   | Block number or height containing the log.                          |
| isService             | bool  | Indicates whether the log is a service log (true) or not (false).   |
| key                   | str   | Key associated with the log.                                        |
| l1BatchNumber         | str   | L1 batch number related to the log in zkRollup systems.             |
| logIndex              | str   | Index of the log within the block.                                  |
| sender                | str   | Address of the sender of the log.                                   |
| shardId               | str   | Identifier of the shard where the log was generated.                |
| transactionHash       | str   | Unique identifier for the transaction associated with the log.      |
| transactionIndex      | str   | Index of the transaction within the block.                          |
| transactionLogIndex   | str   | Index of the log within the transaction.                            |
| txIndexInL1Batch      | str   | Index of the transaction within the L1 batch.                       |
| value                 | str   | Value associated with the log.                                      |

