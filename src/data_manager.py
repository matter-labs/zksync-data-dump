import polars as pl


class DataManager:
    def __init__(self, path_data):
        self.path_data = path_data
        self.contract_deployed_event_hash = "0x290afdae231a3fc0bbae8b1af63698b0a1d79b21ad17df0342dfb952fe74f8e5"
        self.transfer_event_hash = "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"

    def get_total_number_of_deployed_contracts(self, block_max, block_min=1):
        # Get total number of unique contracts deployed on zkSync until the block number max
        q = (
            pl.scan_parquet(self.path_data['logs'])
            .filter(
                pl.col('topics_0').str.to_lowercase().eq(
                    self.contract_deployed_event_hash)
                &
                pl.col("blockNumber").is_between(block_min, block_max)
            )
            .select(pl.format("0x{}", pl.col('topics_3').str.slice(-40)).alias('contract_address'))
        )
        return q.collect(streaming=True)['contract_address'].unique()

    def get_total_number_of_transactions(self, block_min, block_max):

        q = (
            pl.scan_parquet(self.path_data['transactions'])
            .filter(pl.col("blockNumber").is_between(block_min, block_max))
            .select(pl.len())
        )
        return q.collect(streaming=True).rows()[0][0]

    def get_events(self, topic_0, block_min, block_max, contract_addresses={}):
        txs = pl.scan_parquet(self.path_data['logs'])
        if len(contract_addresses) > 0:
            txs = txs.filter(
                pl.col('address').str.to_lowercase().is_in(contract_addresses))
        txs = (
            txs.filter(
                pl.col('topics_0').eq(topic_0)
                & pl.col('blockNumber').is_between(block_min, block_max)
            )
            .select([
                pl.col('blockNumber'),
                pl.col('transactionHash'),
                pl.col('transactionIndex'),
                pl.col('logIndex'),
                pl.col('address').str.to_lowercase().alias('contract_address'),
                pl.format("0x{}", pl.col(
                    'topics_1').str.slice(-40)).alias('sender'),
                pl.format("0x{}", pl.col('topics_2').str.slice(-40)
                          ).alias('receiver'),
                pl.col('data').str.replace('0x', '0x0').alias('amount')]
            )
        )
        blocks = (
            pl.scan_parquet(self.path_data['blocks'])
            .filter(pl.col('number').is_between(block_min, block_max))
            .select(pl.col('number'), pl.from_epoch(pl.col('timestamp')))
        )
        q = (txs.join(blocks, left_on='blockNumber', right_on='number', how='left')
             )
        return q.collect(streaming=True)

    def get_number_of_contracts_per_day(self, block_min, block_max):
        # Number of contracts deployed on zkSync during the analyzed block range per day
        q_1 = (
            pl.scan_parquet(self.path_data['logs'])
            .filter(
                pl.col('topics_0').eq(self.contract_deployed_event_hash)
                & pl.col('blockNumber').is_between(block_min, block_max)
            )
            .select([pl.col('blockNumber'), pl.format("0x{}", pl.col('topics_3').str.slice(-40)
                                                      ).unique().alias('contract_address')])
        )
        q_2 = (pl.scan_parquet(self.path_data['blocks'])
               .filter(pl.col('number').is_between(block_min, block_max))
               .select(pl.col('number'), pl.from_epoch(pl.col('timestamp')).cast(pl.Date).alias('date'))
               )
        q = q_1.join(q_2, left_on='blockNumber', right_on='number', how='left')
        q = (q
             .group_by(pl.col('date'))
             .agg(pl.len())
             .sort(pl.col('date'))
             )
        return q.collect(streaming=True)

    def get_block_info(self, block_min, block_max):
        q = (
            pl.scan_parquet(self.path_data['blocks'])
            .filter(pl.col("number").is_between(block_min, block_max))
            .filter(pl.col('number') > 0)
            .select([pl.col('number').min().alias('min_number'),
                    pl.col('number').max().alias('max_number'),
                    pl.from_epoch(pl.col('timestamp').min()
                                  ).alias('min_timestamp'),
                    pl.from_epoch(pl.col('timestamp').max()).alias('max_timestamp')])
        )
        return q.collect(streaming=True)

    def get_total_number_of_blocks(self, block_min, block_max):
        q = (
            pl.scan_parquet(self.path_data['blocks'])
            .filter(pl.col("number").is_between(block_min, block_max))
            .select(pl.len())
        )
        return q.collect(streaming=True).rows()[0][0]

    def get_total_number_of_topics(self):
        q = (
            pl.scan_parquet(self.path_data['logs'])
            .group_by(pl.col('topics_0'))
            .agg(pl.len())
            .sort(pl.col('len'), descending=True)
        )
        return q.collect(streaming=True)

    def get_total_number_of_contract_calls(self):
        q = (
            pl.scan_parquet(self.path_data['logs'])
            .group_by(pl.col('address').str.to_lowercase())
            .agg(pl.len())
            .sort(pl.col('len'), descending=True)
        )
        return q.collect(streaming=True)

    def get_number_of_transfers_events_filtered(self, block_min, block_max):
        q = (
            pl.scan_parquet(self.path_data['logs'])
            .filter(
                pl.col('topics_0').eq(self.transfer_event_hash)
                & pl.col('blockNumber').is_between(block_min, block_max)
                & ~(
                    pl.col('address').str.to_lowercase().eq(
                        '0x000000000000000000000000000000000000800a')
                    & (
                        pl.col('topics_1').eq(
                            '0x0000000000000000000000000000000000000000000000000000000000008001')
                        | pl.col('topics_2').eq('0x0000000000000000000000000000000000000000000000000000000000008001')
                    )
                )
                # & pl.col('topics_1').ne(pl.col('topics_2'))
            )
            .group_by(pl.col('address').str.to_lowercase())
            .agg(pl.len())
            .sort(pl.col('len'), descending=True)
        )
        return q.collect(streaming=True)

    def get_number_of_transfers_events(self, block_min, block_max):
        q = (
            pl.scan_parquet(self.path_data['logs'])
            .filter(
                pl.col('topics_0').eq(self.transfer_event_hash)
                & pl.col('blockNumber').is_between(block_min, block_max)
            )
            .group_by(pl.col('address').str.to_lowercase())
            .agg(pl.len())
            .sort(pl.col('len'), descending=True)
        )
        return q.collect(streaming=True)

    def get_number_of_unique_addresses(self, block_min, block_max):
        q = (pl.scan_parquet(self.path_data['transactions'])
             .filter(pl.col('blockNumber').is_between(block_min, block_max))
             .select(pl.concat([pl.col('from').unique(), pl.col('to').unique()]).n_unique().alias('unique_addresses'))
             )
        return q.collect(streaming=True)['unique_addresses'][0]

    def get_transactions_per_day_dist(self, block_min, block_max):
        q_1 = (pl.scan_parquet(self.path_data['transactions'])
               .filter(pl.col('blockNumber').is_between(block_min, block_max))
               .select('blockNumber')
               )
        q_2 = (pl.scan_parquet(self.path_data['blocks'])
               .filter(pl.col('number').is_between(block_min, block_max))
               .select(pl.col('number'), pl.from_epoch(pl.col('timestamp')).cast(pl.Date).alias('date'))
               )
        q = q_1.join(q_2, left_on='blockNumber', right_on='number', how='left')
        q = (q
             .group_by(pl.col('date'))
             .agg(pl.len())
             .sort(pl.col('date'))
             )
        return q.collect(streaming=True)

    def get_number_of_daily_active_users(self, block_min, block_max):
        # Get the daily number of active users
        txs = (
            pl.scan_parquet(self.path_data['transactions'])
            .filter(pl.col('blockNumber').is_between(block_min, block_max))
            .select(
                [
                    pl.col('blockNumber').alias('block_number'),
                    pl.col('from').str.to_lowercase().alias('issuer'),
                ],
            )
        )

        blocks = (pl.scan_parquet(self.path_data['blocks']).select(pl.col('number').alias(
            'block_number'), pl.col('timestamp')))

        q = txs.join(blocks, left_on='block_number',
                     right_on='block_number', how='left')
        q = q.with_columns(pl.from_epoch(
            pl.col('timestamp')).cast(pl.Date).alias('date'))

        q = (q.group_by('date')
             .agg(pl.col('issuer').n_unique().alias('unique_issuers_per_day'))
             .sort('date'))

        return q.collect(streaming=True)
