from datetime import timedelta

__all__ = ['create_client', 'RetryStrategies', 'RetryStrategy']


class RetryStrategies:
    pass


class RetryStrategy:
    pass


def create_client(resource, *,
                  # typical botocore arguments
                  profile: str = None, region: str = None,
                  # global idempotency arguments
                  timeout: timedelta = None, retry_strategy: RetryStrategy = None, heartbeat_interval: timedelta = None,
                  # action-specific idempotency arguments
                  acquire_timeout: timedelta = None, acquire_retry_strategy: RetryStrategy = None):
    pass


class IdempotencyClient:
    def acquire(self, *, timeout=None, retry_strategy=None):
        pass
