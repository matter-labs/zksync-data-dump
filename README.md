# ZKsync Data

Welcome to the ZKsync Data repository! This project provides an open dataset of the [ZKsync Era](https://zksync.io) blockchain network, curated by the [Research Team](https://matter-labs.io/research) at [Matter Labs](https://matter-labs.io). Our dataset offers a comprehensive view of the ZKsync Era blockchain, enabling researchers, developers, and enthusiasts to analyze and understand its transaction dynamics.

You can access the dataset through our data portal at [https://data.zksync.dev](https://data.zksync.dev). For further details, refer to the [Dataset Description](#dataset-description) section or the data folder at [./data/](./data/).

For an in-depth explanation of our work, read our paper available on ArXiv at [https://arxiv.org/abs/2407.18699](https://arxiv.org/abs/2407.18699) or download it directly from [paper-data-strategy-for-zksync.pdf](paper-data-strategy-for-zksync.pdf).

If you find this dataset useful, please cite our paper as described in the [License](#license) section.

## Overview

The ZKsync Dataset offers detailed information on the ZKsync blockchain, including blocks, transactions, transaction receipts, transaction logs, and L2 to L1 logs. The data spans from February 14th, 2023, to March 24th, 2024, capturing the raw data of the ZKsync network to support in-depth analysis of its transaction dynamics.

### Dataset Description

The dataset is organized into multiple subfiles in Parquet format, structured to facilitate processing on local machines. Below are the contents and their respective file counts:

- **Blocks:** 298 files
- **Transactions:** 298 files
- **Transaction receipts:** 298 files
- **Logs:** 298 files
- **L2 to L1 logs:** 298 files

### Dataset Statistics

You can download the full dataset from our data portal at [https://data.zksync.dev](https://data.zksync.dev). The dataset description and schema are available in the [./data/](./data/) directory. Jupyter notebooks for quick exploration and analysis are provided in the [./notebooks/](./notebooks/) directory. For loading and processing the data, we recommend using the [Polars](https://github.com/pola-rs/polars) library.

We descibe the dataset statistics below:


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
- Paper is avaialble at [paper-data-strategy-for-zksync.pdf](paper-data-strategy-for-zksync.pdf)
- Paper is available on ArXiv at [https://arxiv.org/abs/2407.18699](https://arxiv.org/abs/2407.18699)
  

## Ask a Question

- For reporting bugs, please use the [zksync-data-dump/issues](https://github.com/matter-labs/zksync-data-dump/issues) page.

## License

If you find this work useful, please consider citing our academic paper:

```
@misc{silva2024publicdatasetzksyncrollup,
      title={A Public Dataset For the ZKsync Rollup}, 
      author={Maria In{\^e}s Silva and Johnnatan Messias and Benjamin Livshits},
      year={2024},
      eprint={2407.18699},
      archivePrefix={arXiv},
      primaryClass={cs.CR},
      url={https://arxiv.org/abs/2407.18699}, 
}
```
