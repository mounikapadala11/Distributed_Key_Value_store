# Decentralized Key-Value Store

This project implements a decentralized key-value store using consistent hashing. The system is designed to distribute keys across multiple nodes, ensuring high availability and fault tolerance without a single point of failure. The project includes a FastAPI server to handle key-value operations and node management dynamically.

## Key Components

1. **ConsistentHashing**:
   - Manages the consistent hash ring and distributes keys across nodes.
   - Responsible for adding and removing nodes and finding the correct node for a given key.

2. **KeyValueStore**:
   - Implements basic CRUD operations for storing, retrieving, updating, and deleting key-value pairs.

3. **FastAPI Application**:
   - Provides endpoints for key-value operations and node management.
   - Allows dynamic addition of nodes and querying of the responsible node for a key.

4. **Client**:
   - Includes functions to interact with the FastAPI server for performing key-value operations and managing nodes.

## Class Diagram

![Class Diagram](path/to/class_diagram.png)

```plaintext
+--------------------+
| ConsistentHashing  |
+--------------------+
| - num_replicas     |
| - ring             |
| - nodes            |
+--------------------+
| + _hash(key)       |
| + add_node(node)   |
| + get_node(key)    |
+--------------------+

+--------------------+
| KeyValueStore      |
+--------------------+
| - store            |
+--------------------+
| + create(key, val) |
| + read(key)        |
| + update(key, val) |
| + delete(key)      |
+--------------------+

+--------------------+
| FastAPI App        |
+--------------------+
| - kv_store         |
| - hash_ring        |
+--------------------+
| + create(key, val) |
| + read(key)        |
| + update(key, val) |
| + delete(key)      |
| + add_node(node)   |
| + get_node(key)    |
+--------------------+

+--------------------+
| Client             |
+--------------------+
| + create_key(key, value) |
| + read_key(key)          |
| + update_key(key, value) |
| + delete_key(key)        |
| + add_node(node)         |
| + get_node(key)          |
+--------------------+

```


## Sequence Diagram

Client -> FastAPI App: create(key, value)
FastAPI App -> KeyValueStore: create(key, value)
KeyValueStore -> FastAPI App: success/failure
FastAPI App -> Client: response

Client -> FastAPI App: add_node(node)
FastAPI App -> ConsistentHashing: add_node(node)
ConsistentHashing -> FastAPI App: success
FastAPI App -> Client: response

Client -> FastAPI App: get_node(key)
FastAPI App -> ConsistentHashing: get_node(key)
ConsistentHashing -> FastAPI App: node
FastAPI App -> Client: node



## Instance Creation Per Node

Each node in this decentralized system creates the following instances:

### ConsistentHashing:

- Manages the consistent hash ring and node distribution.
- Each node maintains its own view of the hash ring to determine where keys should be stored or retrieved from.

### KeyValueStore:

- Manages the local storage of key-value pairs on the node.
- Each node handles its own key-value operations.

## When to Apply Such a System

This decentralized key-value store is ideal for:

- **High Availability**: Systems that require continuous availability without a single point of failure.
- **Scalability**: Applications that need to scale horizontally by adding more nodes to distribute the load.
- **Fault Tolerance**: Environments where resilience to node failures is crucial.
- **Distributed Systems**: Use cases that benefit from distributed data storage and processing, such as large-scale web applications, content delivery networks, and distributed databases.

## Pros and Cons

**Pros**:

- **Scalability**: Easily add nodes to increase capacity.
- **Fault Tolerance**: No single point of failure; nodes can join or leave dynamically.
- **Performance**: Distributes load across multiple nodes, reducing bottlenecks.

**Cons**:

- **Complexity**: Managing a distributed system and ensuring consistency can be complex.
- **Eventual Consistency**: Depending on the implementation, there might be periods where data is not consistent across all nodes.
- **Coordination Overhead**: Adding and removing nodes requires updating the consistent hash ring on all nodes.


## Endpoints

/create/{key}: Create a new key-value pair.
/read/{key}: Read the value of a key.
/update/{key}: Update the value of a key.
/delete/{key}: Delete a key-value pair.
/add_node/{node}: Add a new node to the consistent hashing ring.
/get_node/{key}: Get the node responsible for a given key.


## Conclusion
This project provides a robust, scalable, and fault-tolerant key-value store using a decentralized approach. By leveraging consistent hashing and dynamic node management, the system ensures high availability and performance for distributed applications. The provided FastAPI endpoints and client examples make it easy to interact with and manage the key-value store. This decentralized key-value store is a powerful tool for building distributed systems that require efficient data storage and retrieval.