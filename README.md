# ZKsync Data

`The repository is still under development and will be finalized soon.`

This repository contains an open data set of the [ZKsync](https://zksync.io/) blockchain network, provided by the [Research Team](https://matter-labs.io/research/) at [Matter Labs](https://matter-labs.io/). The data set aims to offer comprehensive insights into the ZKsync blockchain, enabling researchers, developers, and enthusiasts to analyze and understand the network's transaction dynamics.

## Overview

The ZKsync Data Set offers detailed information on the ZKsync blockchain, including blocks, transactions, transaction receipts, transaction logs, and L2 to L1 logs. The data spans from February 14th, 2023, to March 24th, 2024, capturing the raw data of the ZKsync network to support in-depth analysis of its transaction dynamics.

### Data Set Description

The data set is organized into multiple subfiles in Parquet format, structured to facilitate processing on local machines. Below are the contents and their respective file counts:

- **Blocks:** 298 files
- **Transactions:** 298 files
- **Transaction receipts:** 298 files
- **Logs:** 298 files
- **L2 to L1 logs:** 298 files

### Data Set Statistics

- **Transactions:** 327,174,035
- **Blocks:** 29,710,983
  - Block range: 1 (February 14th, 2023, 14:22:22) to 29,710,983 (March 24th, 2024, 00:00:00)
- **Logs:**
  - Unique topics_0 (proxy for event name): 14,388
  - Total events triggered: 2,044,221,151
  - Unique contracts called: 981,892
- **Transfer events:**
  - Total transfer events: 1,479,714,503
  - Filtered transfer events excluding ZKsync fees: 704,720,525
- **Unique wallet addresses:** 7,322,502

You can download the full data set from our data portal at [https://data.zksync.dev](https://data.zksync.dev). The data set description and schema are available in the [./data/](https://github.com/matter-labs/zksync-data-dump/tree/main/data) directory. Jupyter notebooks for quick exploration and analysis are provided in the [./notebooks/](https://github.com/matter-labs/zksync-data-dump/tree/main/notebooks) directory. For loading and processing the data, we recommend using the [Polars](https://github.com/pola-rs/polars) library.

### Data Attributes

#### Blocks
Blocks are sequential units of data containing lists of transactions and metadata such as timestamps and hashes. They ensure transaction security, network consensus, and efficient data storage. Attributes include `hash`, `parentHash`, `miner`, `number`, `timestamp`, among others.

#### Transactions
Transactions involve transferring assets, recording data, or executing smart contracts. Attributes include `blockHash`, `blockNumber`, `from`, `to`, `value`, `gas`, `gasPrice`, `nonce`, `hash`, etc.

#### Transaction Receipts
Receipts provide a summary of the transaction outcome, detailing gas used, status, and logs. Attributes include `transactionHash`, `blockNumber`, `from`, `to`, `gasUsed`, `status`, etc.

#### Transaction Logs
Logs are records of events during transaction execution, crucial for auditing and monitoring activities. Attributes include `address`, `blockHash`, `blockNumber`, `data`, `topics_0` through `topics_3`, etc.

#### L2 to L1 Logs
These logs facilitate communication between ZKsync Layer 2 and Ethereum Layer 1, ensuring transaction security through ZK proofs. Attributes include `blockHash`, `blockNumber`, `sender`, `transactionHash`, `value`, etc.

## What's New

- Initial version of the code and analysis

## Ask a Question

- For reporting bugs, please use the [zksync-data-dump/issues](https://github.com/matter-labs/zksync-data-dump/issues) page.

If you find this repository useful, please consider citing our academic paper:

```
To be announced soon. In the meantime, please consider referring to this GitHub repository.
```

For more detailed information on the data set and its attributes, please refer to the [./data/README.md](https://github.com/matter-labs/zksync-data-dump/tree/main/data) file.
