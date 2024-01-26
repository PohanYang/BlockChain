# Block Chain
## The block chain survey/learning

# Chapter 1. "Be Your Own Bank"

Let's begin by examining the architecture of blockchain and the key elements it contains. First, we need to clearly define the basic format and content of transactions and blocks.

### Transaction
Similar to the bank transfers we are accustomed to, each transaction generates a detailed record, known as a Transaction. This record meticulously logs the sender, receiver, amount, transaction fee, and any accompanying notes.

![1-1.Begin_Transition](https://github.com/PohanYang/BlockChain/blob/main/image/1-1.Begin_Transition.png

For example, if we have a transaction ready to do:
```
Sender: Frank
Receiver: David
Amount: 100
Fee: 5
Massage: bounus
```

We'll label this section as 'Transaction #1,' and subsequent transactions will be sequentially named 'Transaction #2,' 'Transaction #3,' and so on. 
All these records will be logged into the blockchain. 
In this way, we can define a transaction.

```c
struct _TRANS {
	u8 sender:0;
        u8 receiver:0;
        u8 amounts:0;
        u8 fee:0;
        char message;
}TRANS, *PTRAN;
```

![1-2.Begin_Transition_Chain](https://github.com/PohanYang/BlockChain/blob/main/image/1-2.Begin_Transition_Chain.png)

Next, each Transaction is encrypted using the simple sha-256 encryption method.
Reference: [SHA-256](https://github.com/983/SHA-256 "link")

In this way, each document is encrypted content. 
But how do we 'chain' each transaction together? 
At this point, we add some definitions to the content.


```c
struct _BLOCK {
	struct *_TRANS trans_info;
	u8 hash;
        u8 previousHash;
}BLOCK, *PBLOCK;
```

The sha-256 encription function may be:

```c
void sha256_process(struct _BLOCK *block_info)
{
	char hex[SHA256_HEX_SIZE];
	const char *text = (
			BLOCK->previousHash +
			BLOCK->trans_info->sender + BLOCK->tran_info->receiver +
			BLOCK->trans_info->tran_info->amounts + 
			BLOCK->trans_info->fee + BLOCK->tran_info->message);

	/* Compute SHA-256 sum. */
	sha256(text, strlen(TRANS), hex);
}
```