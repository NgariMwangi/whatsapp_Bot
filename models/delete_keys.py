import redis

# Create a Redis client
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# # List of keys to delete
# keys_to_delete = ["", "", "9876543211", "9876543210"]

# # Use the DEL command to delete the keys
# redis_client.delete(*keys_to_delete)
redis_client.flushall()