from boto_idempotent.client import create_client

"""
Configure the singleton client instance.
Typical stuff here related to timeouts, heartbeats, etc
Client will be resource-specific; we'll use metaclasses to fill in the body with resource-specific attributes
"""
client = create_client('ec2')

"""
Acquire a resource. The resource is what was configured in create_client(...).
The returned resource has been idempotently acquired; the meaning of 'idempotent' is resource-specific but implies that
the sole owner of that resource until a call to release() (which is implicit when resource is acquired in a with
statement) or otherwise released in an exceptional manner (e.g. lock expiration).
"""
with client.acquire() as resource:
    """
    """
    pass
