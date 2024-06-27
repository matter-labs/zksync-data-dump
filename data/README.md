# ZKsyn Dataset

The ZKsyn dataset provides comprehensive data on blocks, transactions, transaction receipts, transaction logs, and L2 to L1 logs from ZKSync blockchain. It spans from February 14th, 2023, to March 24th, 2024, capturing raw ZKSync data.

This dataset provides a rich source of data for analyzing the ZKSync network and its transaction dynamics.

## Data Description

The dataset is stored in Parquet format, organized into multiple subfiles:

- **Blocks:** 298 files
- **Transactions:** 298 files
- **Transaction receipts:** 298 files
- **Logs:** 298 files
- **L2 to L1 logs:** 298 files

These files are structured to facilitate processing on local machines, such as laptops. Python scripts are provided for data download, along with [Jupyter notebooks](https://github.com/matter-labs/zksync-data-dump/tree/main/notebooks) for quick exploration and analysis. The dataset aims to support in-depth analysis of the ZKSync network and its transactions.

## Usage Recommendations

For loading and processing the data, we recommend using the [Polars](https://github.com/pola-rs/polars) library. Example code snippets are available in the provided in [./notebooks](https://github.com/matter-labs/zksync-data-dump/tree/main/notebooks).

## Dataset Statistics

- **Transactions:** 327,174,035
- **Blocks:** 29,710,983
  - Block range: 1 (February 14th, 2023, 14:22:22) to 29,710,983 (March 24th, 2024, 00:00:00)
- **Logs:**
  - Unique topics_0 (proxy for event name): 14,388
  - Total events triggered: 2,044,221,151
  - Unique contracts called: 981,892
- **Transfer events:**
  - Total transfer events: 1,479,714,503
  - Filtered transfer events that do not account for ZKsync fees processing: 704,720,525
- **Unique wallet addresses:** 7,322,502


## Blocks

Blocks are sequential units of data within a blockchain, each identified by a unique hash. They contain transaction information, metadata such as timestamps and the hash of the previous block (`parentHash`), which links them in a chain back to the genesis block (block number 0). This chain of blocks forms the blockchain. Blocks ensure transaction security, network consensus, and efficient data storage and processing within blockchain networks.

We list the attributes of the blocks in the ZKsyn dataset below:

| Attribute         | Type          | Description                                                                                           |
|-------------------|---------------|-------------------------------------------------------------------------------------------------------|
| hash              | str           | Unique identifier for the block.                                                                      |
| parentHash        | str           | Unique identifier of the parent block.                                                                |
| sha3Uncles        | str           | SHA-3 hash of the uncles' block headers. In ZKsyn it is set to `0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347` since there are no uncle blocks.                                                             |
| miner             | str           | Address of the miner who mined the block. This is set as Null address (`0x0`) in all ZKsync blocks since it does not have miners or block validators.                                                            |
| stateRoot         | str           | Root hash of the state trie. Set to Null address (`0x0`).                                                                         |
| transactionsRoot  | str           | Root hash of the transaction trie.  Set to Null address (`0x0`).                                                                   |
| receiptsRoot      | str           | Root hash of the receipts trie.  Set to Null address (`0x0`).                                                                        |
| number            | i64           | Block number or height.                                                                               |
| l1BatchNumber     | str           | L1 batch number, related to the sequence of batches submitted to Layer 1 in zkRollup systems.       |
| gasUsed           | i64           | Total amount of gas used by all transactions in the block.                                            |
| gasLimit          | i64           | Maximum amount of gas that can be used by all transactions in the block.   Set to 4,294,967,296 (2^32) units of gas.                       |
| baseFeePerGas     | i64           | Base fee, in Wei (10^-18 ETH), per unit of gas.                                                                             |
| extraData         | str           | Extra data included by the miner in the block. Set to `"0x"` since there are no miner.                                                       |
| logsBloom         | str           | Bloom filter for the logs of the block. Set to `0x0...0`.                                                              |
| timestamp         | i64           | Unix timestamp of when the block was collated.                                                           |
| l1BatchTimestamp  | str           |L1 batch timestamp (in HEX format) associated with the block.                                            |
| difficulty        | i64           | Difficulty target for mining the block.  Set to 0 since there is not mining.                                                             |
| totalDifficulty   | i64           | Cumulative difficulty of the blockchain up to and including this block.    Set to 0 since there is not mining.                                |
| sealFields        | list[null]    | Seal fields containing proof-of-work or proof-of-stake information.   List containng null a since value.                                |
| uncles            | list[null]    | Uncle blocks that were mined but not included in the main chain.   List with Null value since there is not mining.                                   |
| size              | i64           | Size of the block in bytes.  Set to 0.                                                                         |
| mixHash           | str           | Hash used in the mining process to prove that enough computational work has been performed.  Set to `0x0...0` since there is not mining.         |
| nonce             | str           | Value used in the mining process to find a valid block hash.    Set to `0x0000000000000000` since there is not mining.                                     |


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
