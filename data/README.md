# ZKsync Data Set

The ZKsync data set provides comprehensive data on blocks, transactions, transaction receipts, transaction logs, and L2 to L1 logs from ZKsync blockchain. It spans from February 14th, 2023, to March 24th, 2024, capturing raw ZKsync data.

This data set provides a rich source of data for analyzing the ZKsync network and its transaction dynamics.

## Data Description

The data set is stored in Parquet format, organized into multiple subfiles:

- **Blocks:** 298 files
- **Transactions:** 298 files
- **Transaction receipts:** 298 files
- **Logs:** 298 files
- **L2 to L1 logs:** 298 files

These files are structured to facilitate processing on local machines, such as laptops. Python scripts are provided for data download, along with [Jupyter notebooks](https://github.com/matter-labs/zksync-data-dump/tree/main/notebooks) for quick exploration and analysis. The data set aims to support in-depth analysis of the ZKsync network and its transactions.

## Usage Recommendations

For loading and processing the data, we recommend using the [Polars](https://github.com/pola-rs/polars) library. Example code snippets are available in the provided in [./notebooks](https://github.com/matter-labs/zksync-data-dump/tree/main/notebooks).

## Data Set Statistics

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

Blocks are sequential units of data within a blockchain, each identified by a unique hash. They contain a list of transactions, metadata such as timestamps and the hash of the previous block (`parentHash`), which links them in a chain back to the genesis block (block number 0). This chain of blocks forms the blockchain. Blocks ensure transaction security, network consensus, and efficient data storage and processing within blockchain networks.

> **Note:** Blocks should be sorted by the `number` attribute to maintain the correct order of the blocks on the blockchain.

We list the attributes of the blocks data in the ZKsync data set below:

| Attribute         | Type          | Description                                                                                           |
|-------------------|---------------|-------------------------------------------------------------------------------------------------------|
| hash              | str           | Unique identifier for the block.                                                                      |
| parentHash        | str           | Unique identifier of the parent block.                                                                |
| sha3Uncles        | str           | SHA-3 hash of the uncles' block headers. On ZKsync it is set to `0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347` since there are no uncle blocks.                                                             |
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
| sealFields        | list[null]    | Seal fields containing proof-of-work or proof-of-stake information.   List containng null as value.                                |
| uncles            | list[null]    | Uncle blocks that were mined but not included in the main chain.   List with Null value since there is not mining.                                   |
| size              | i64           | Size of the block in bytes.  Set to 0.                                                                         |
| mixHash           | str           | Hash used in the mining process to prove that enough computational work has been performed.  Set to `0x0...0` since there is not mining.         |
| nonce             | str           | Value used in the mining process to find a valid block hash.    Set to `0x0000000000000000` since there is not mining.                                     |


## Transactions
Transactions are digital interactions that involve transferring assets, recording data, or executing smart contracts between parties on blockchains like those based on the Ethereum Virtual Machine (EVM). Each transaction is initiated by a user, authenticated through cryptographic signatures, and broadcasted to a decentralized network of nodes for validation. Once verified, transactions are grouped into blocks and added to the blockchain via a consensus mechanism, ensuring that they are secure, immutable, transparent, and free of intermediaries, forming the core of the blockchain system.

In rollups, such as ZKsync, transactions are aggregated and processed off the underlying blockchain (e.g., Ethereum, a Layer 1 blockchain) to enhance scalability and reduce costs. Rollups bundle multiple transactions into a single batch, which is then submitted to the underlying blockchain as one transaction. This method reduces the load on the underlying chain while ensuring transaction security and finality through cryptographic proofs, like Zero-Knowledge (ZK) proofs used by ZKsync, or validity checks. By processing transactions off-chain and periodically committing the results to the underlying chain, rollups improve throughput and efficiency without compromising the blockchain’s security and decentralization.

Transactions are identified by a unique transaction hash. When issuing a transaction, the user needs to specify parameters such as the recipient address (which can also be a smart contract and the functions the user wants to call), the amount of tokens to transfer, the gas price, and the gas limit. The gas price represents the fee the user is willing to pay per unit of gas, while the gas limit is the maximum amount of gas the user is willing to consume for the transaction, a mechanism introduced to prevent infinite loops or excessive resource consumption due to the [halting problem](https://en.wikipedia.org/wiki/Halting_problem). Another important parameter is the transaction receipt, which contains the status of the transaction (success or failure), and the amount of actual gas used. The specifics of transaction receipts are discussed in the next section.

> **Note:** Transactions should be sorted by the `blockNumber` and `transactionIndex` attributes to maintain the correct order of the transactions on the blockchain.

We list the attributes of the transactions data in the ZKsync data set below:


| Attribute                | Type  | Description                                                                 |
|--------------------------|-------|-----------------------------------------------------------------------------|
| blockHash                | str   | Unique identifier of the block containing the transaction.                  |
| blockNumber              | i64   | Block number or height containing the transaction.                          |
| chainId                  | i64   | Identifier of the blockchain network. Set to 324 that represents ZKsync chain.                                      |
| from                     | str   | Address of the sender of the transaction.                                   |
| gas                      | i64   | Amount of gas provided as `gasLimit` for the transaction.                                 |
| gasPrice                 | i64   | Price per unit of gas the sender is willing to pay.                         |
| hash                     | str   | Unique identifier for the transaction.                                      |
| input                    | str   | Data sent along with the transaction. In HEX code.                                      |
| l1BatchNumber            | str   | L1 batch number related to the transaction in zkRollup systems.             |
| l1BatchTxIndex           | str   | Index of the transaction in the L1 batch.                                   |
| maxFeePerGas             | i64   | Maximum fee, in Wei (10^-18 ETH), per unit of gas.                                                |
| maxPriorityFeePerGas     | i64   | Maximum priority fee, in Wei (10^-18 ETH), per unit of gas.                                       |
| nonce                    | i64   | Number of transactions sent by the sender prior to this one.                |
| r                        | str   | First part of the ECDSA signature.                                          |
| s                        | str   | Second part of the ECDSA signature.                                         |
| to                       | str   | Address of the receiver of the transaction.                                 |
| transactionIndex         | i64   | Index of the transaction within the block.                                  |
| type                     | i64   | Type of transaction divided into 5 categories: Legacy (0 or `0x0`), [EIP-2930](https://eips.ethereum.org/EIPS/eip-2930) (1 or `0x1`), [EIP-1559](https://eips.ethereum.org/EIPS/eip-1559) (2 or `0x2`), [EIP-712](https://eips.ethereum.org/EIPS/eip-712) (113 or `0x71`), and Priority (255 or `0xff`). See more details in the [ZKsync documentation](https://docs.zksync.io/zk-stack/concepts/transaction-lifecycle#transaction-types).                                                       |
| v                        | f64   | Recovery id of the ECDSA signature.                                         |
| value                    | str   | Amount of tokens (in Wei and in HEX format) that are transferred in the transaction to the receiptent address (`to`).|


## Transaction receipts

Transaction receipts provide a comprehensive summary of the outcome and effects of a transaction once it is processed and included in a block. They include key details such as the transaction hash, block number, and block hash to identify and verify the transaction, along with the sender (`from`) and recipient (`to`) addresses. The receipts also detail the actual gas used by the specific transaction, and, if applicable, the address of any newly created smart contract. Additional information includes logs for event logging (discussed in the next section), the transaction’s status (success or failure), and the effective gas price paid. These receipts are crucial for users and developers to understand, audit, and interact with transactions and smart contracts on the blockchain. For example, they provide essential elements for transaction analysis, monitoring, and verification of transaction fees spent by users.

> **Note:** Similarly to transactions, transaction receipt data should be sorted by the `blockNumber` and `transactionIndex` attributes to maintain the correct order of transactions on the blockchain.

We list the attributes of the transactions receipts data in the ZKsync data set below:


| Attribute              | Type  | Description                                                                   |
|------------------------|-------|-------------------------------------------------------------------------------|
| blockHash              | str   | Unique identifier of the block containing the transaction.                    |
| blockNumber            | i64   | Block number or height containing the transaction.                            |
| contractAddress        | str   | Address of the contract created by the transaction, if applicable.            |
| cumulativeGasUsed      | i64   | Total amount of gas used when the transaction was executed in the block. Set to 0 on ZKsync.      |
| effectiveGasPrice      | i64   | Actual price per unit of gas , in Wei (10^-18 ETH),paid.                                            |
| from                   | str   | Address of the sender of the transaction.                                     |
| gasUsed                | i64   | Amount of gas used by the transaction.                                        |
| l1BatchNumber          | str   | L1 batch number related to the transaction in zkRollup systems.               |
| l1BatchTxIndex         | str   | Index of the transaction in the L1 batch.                                     |
| logsBloom              | str   | Bloom filter for the logs of the transaction. Set to `0x0...0` on ZKsync.                                 |
| root                   | str   | State root after the transaction is executed.                                 |
| status                 | i64   | Status of the transaction (1 for success, 0 for failure).                     |
| to                     | str   | Address of the receiver of the transaction.                                   |
| transactionHash        | str   | Unique identifier for the transaction.                                        |
| transactionIndex       | i64   | Index of the transaction within the block.                                    |
| type                   | i64   | Type of transaction divided into 5 categories: Legacy (0 or `0x0`), [EIP-2930](https://eips.ethereum.org/EIPS/eip-2930) (1 or `0x1`), [EIP-1559](https://eips.ethereum.org/EIPS/eip-1559) (2 or `0x2`), [EIP-712](https://eips.ethereum.org/EIPS/eip-712) (113 or `0x71`), and Priority (255 or `0xff`). See more details in the [ZKsync documentation](https://docs.zksync.io/zk-stack/concepts/transaction-lifecycle#transaction-types).                                                          |



## Transaction Logs

In this section, we discuss the attributes of the transaction logs data in the ZKsync data set in details. Transaction logs are systematic records of events generated during the execution of transactions, particularly in interactions involving smart contracts. Each log entry comprises a log index, data, and topics, crucial for identifying and categorizing specific events such as token transfers, approvals, swaps, minting, and voting. These logs are emitted using the `emit` keyword within smart contract code and play a pivotal role in monitoring activities, triggering actions within decentralized applications, and enabling event-driven programming. For instance, decentralized exchanges (DEXs) emit events upon trade executions, enabling user interfaces to update displays with current trade information.

These logs are stored in transaction receipts, offering a gas-efficient method to capture transient event data without permanently altering the blockchain's state. They are indispensable for auditing, analytics, and ensuring seamless interaction between smart contracts and external systems. Among the vast array of data accessible on EVM-based blockchains, transaction logs stand out as crucial sources of information for researchers, developers, and users. They facilitate analyses of various token transfer patterns and support blockchain analysis research.

> **Note:** Transaction logs should be sorted by the `blockNumber`, `transactionIndex`, and `logIndex` attributes to maintain the correct order in which they are stored on the blockchain. This is particularly important when analyzing the different states of a blockchain before and after the execution of a transaction that triggers a smart contract function.

We list the attributes of the transactions logs data in the ZKsync data set below:

| Attribute             | Type  | Description                                                      |
|-----------------------|-------|------------------------------------------------------------------|
| address               | str   | Address of the contract that generated the log.                  |
| blockHash             | str   | Unique identifier of the block containing the transaction.       |
| blockNumber           | i64   | Block number or height containing the transaction.               |
| data                  | str   | Data contained in the log.  This can be used, for example, to extract the amont of tokens transferred from one users to the other.                                     |
| l1BatchNumber         | str   | L1 batch number related to the log in zkRollup systems.          |
| logIndex              | i64   | Index of the log within the block.                               |
| logType               | null  | Type of log.  Set to `null` on ZKsync                                                   |
| removed               | bool  | Indicates whether the log was removed (true) or not (false).     |
| transactionHash       | str   | Unique identifier for the transaction.                           |
| transactionIndex      | i64   | Index of the transaction within the block.                       |
| transactionLogIndex   | str   | Index of the log within the transaction. In hexadecimal (HEX) format.                        |
| topics_0              | str   | First topic of the log encoded in hexadecimal (HEX) format. This refers to the `name` of the event trigerred e.g., `Transfer`, `Approval`, `Swap`, etc.                                        |
| topics_1              | str   | Second topic of the log encoded in hexadecimal (HEX) format. Its function depends on the contract function implementation.                                          |
| topics_2              | str   | Third topic of the log encoded in hexadecimal (HEX) format.  Its function depends on the contract function implementation.                                                     |
| topics_3              | str   | Fourth topic of the log encoded in hexadecimal (HEX) format.  Its function depends on the contract function implementation.                                                    |


### Topics Attributes

The interpretation of the `topics` attributes (`topics_0`, `topics_1`, `topics_2`, and `topics_3`) depends on the implementation details of the invoked function within a smart contract. Typically, `topics_0` represents the event name like `Transfer`, `Approval`, and `Swap`, while subsequent topics represent indexed parameters of the event. The `data` attribute contains non-indexed event parameters. For example, in the context of a token transfer event, `topics_0` might signify the event name `Transfer`, `topics_1` and `topics_2` could respectively denote sender and receiver addresses, and `data` would typically represent the amount of tokens transferred. All these parameters are encoded in hexadecimal (HEX) format in our data set.

### Hashing and Signatures

`topics_0` corresponds to the hashed function signature using `keccak256`. This signature consists of the function name followed by its parameter types. For example, the signature of a typical `Transfer` event is `Transfer(address,address,uint256)`. After hashing it with `keccak256`, the result becomes `0xddf2 ... b3ef`, which is the `topics_0`. Below is a Python code snippet demonstrating how to verify if a given signature matches `topics_0`:

```python
import web3
def check_sig(sig, topics_0):
    return web3.Web3.keccak(text=sig).hex() == topics_0
```

### Event Mapping

We provide a mapping of the most frequently invoked events within the ZKsync data set in [./src/utils.py#events_dict](https://github.com/matter-labs/zksync-data-dump/blob/main/src/utils.py). This mapping facilitates the parsing of the majority of events in our data set. The mapping is structured as a dictionary where the topics_0 hex value serves as the key, and the corresponding value is a dictionary containing the parsed event name and its function signature. For instance, the Transfer event is represented as follows within the map:

```python
events_dict['0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'] = {
    'name': 'Transfer',
    'signature': 'Transfer(address,address,uint256)'
}
```


## L2 to L1 logs

These logs are messages emitted by the ZKsync Layer 2 (L2) network and sent to the Ethereum Layer 1 (L1) network. They play a crucial role in maintaining communication between the two layers and ensuring the security and integrity of transactions and data transfers.

In ZKsync, the L1 smart contract verifies these communications by checking the messages alongside the ZK proofs. The only "provable" part of the communication from L2 to L1 is the native L2 to L1 logs emitted by the virtual machine (VM). These logs can be generated using the `to_l1 opcode`. For details refer to the [ZKsync documentation](https://docs.zksync.io/zk-stack/concepts/l1_l2_communication).

We list the attributes of the L2 to L1 logs data in the ZKsync data set below:
| Attribute             | Type  | Description                                                         |
|-----------------------|-------|---------------------------------------------------------------------|
| blockHash             | str   | Unique identifier of the block containing the log.                  |
| blockNumber           | str   | Block number or height containing the log.                          |
| isService             | bool  | Indicates whether the log is a service log (`true`) or not (`false`).   |
| key                   | str   | Key associated with the log  that could be used to carry some data with the log.                                        |
| l1BatchNumber         | str   | L1 batch number related to the log.             |
| logIndex              | str   | Index of the log within the block.                                  |
| sender                | str   | It is the value of `this` in the frame where the L2→L1 log was emitted.                                   |
| shardId               | str   | It is the id of the shard the opcode was called. It is currently set to 0.                |
| transactionHash       | str   | Unique identifier for the transaction associated with the log.      |
| transactionIndex      | str   | Index of the transaction within the block.                          |
| transactionLogIndex   | str   | Index of the log within the transaction.                            |
| txIndexInL1Batch      | str   | Index of the transaction within the L1 batch.                       |
| value                 | str   | Value associated with the log that could be used to carry some data with the log.                                      |

