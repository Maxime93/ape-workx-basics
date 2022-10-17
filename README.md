# Deploy Token on ETH-GOERLI using APE Framework (Python)

Following APE official docs: https://docs.apeworx.io/ape/stable/
Using Ape for deploying/interacting with a basic Token smart contract.

#### Hardhat mainnet fork console

Export Alchemy API key: `export WEB3_ALCHEMY_API_KEY="key"` and/or `export WEB3_INFURA_API_KEY=""`

Run `ape console --network ethereum:local:hardhat`
Run `ape compile` to compile the smart contract.

```python
# Accounts
In [2]: accounts.test_accounts
Out[2]: [0x1e59ce931B4CFea3fe4B875411e280e173cB7A9C, 0xc89D42189f0450C2b2c3c61f58Ec5d628176A1E7, 0x318b469BBa396AEc2C60342F9441be36A1945174, 0x1e14cBD146c3a5496F588CF28Ee656c210057904, 0x63953eB1B3D8DB28334E7C1C69456C851F934199, 0x1e6f0dfb1775f5032f12f56a01526351eD3F07aF, 0x8656bDDC790dA239824eE2eA782d350c80AA2Cf4, 0x2192f6112a026bce4047CeD2A16553Fd31E798B6, 0x1fC1FcEccD0d0cf092Dd11465f2e9Ce6BE3F62ac, 0xBc8563cb0eeDbd1b95CCafD0c156e2daf5E18c29]

In [3]: accounts.test_accounts[0].balance
Out[3]: 10000000000000000000000

In [4]: deployer = accounts.test_accounts[0]

In [13]: token = deployer.deploy(project.Token)
INFO: Confirmed 0x3cdfa7c3f7613453c034681c1f528c0f8b453030a382e835c3eee2578fc38658 (total fees paid = 0)
SUCCESS: Contract 'Token' deployed to: 0x274b028b03A250cA03644E6c578D81f019eE1323
Out[13]: <Token 0x274b028b03A250cA03644E6c578D81f019eE1323>


In [17]: token.balanceOf(deployer)
Out[17]: 1000000000

In [18]: receiver = accounts.test_accounts[2]

In [19]: receiver
Out[19]: <TestAccount 0x318b469BBa396AEc2C60342F9441be36A1945174>

In [20]: token.balanceOf(receiver)
Out[20]: 0

In [22]: receipt = token.transfer(receiver, 5000, sender=deployer)
INFO: Confirmed 0x1836924ea062e10a4ee5db809574c158bcfdf9f8d4be4f3ddc42712950a6b592 (total fees paid = 0)
Out[22]: <Receipt 0x1836924ea062e10a4ee5db809574c158bcfdf9f8d4be4f3ddc42712950a6b592>

In [23]: token.balanceOf(receiver)
Out[23]: 5000

In [24]: token.balanceOf(deployer)
Out[24]: 999995000

In [33]: receipt.transaction
Out[33]: <DynamicFeeTransaction chainId=31337, to=0xBcF7FFFD8B256Ec51a36782a52D0c34f6474D951, from=0x1e59ce931B4CFea3fe4B875411e280e173cB7A9C, gas=32551, nonce=3, value=0, data=b'\xa9\x05\x9c\xbb\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x001\x8bF\x9b\xba9j\xec,`4/\x94A\xbe6\xa1\x94Qt\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x13\x88', type=0x02, maxFeePerGas=0, maxPriorityFeePerGas=0, accessList=[]>
```

#### Create account from on-chain address

Create a new account like such: `ape accounts import my_goerli_account`
Follow the steps:
```
Enter Private Key:
Create Passphrase:
Repeat for confirmation:
SUCCESS: A new account '<ADDRESS>' has been added with the id 'my_goerli_account'
```

From the console `ape console --network ethereum:goerli:alchemy`
```python
In [4]: my_account = accounts.load("my_goerli_account")

In [5]: my_account.balance
Out[5]: 319249932664448808
```

See `scripts/accounts.py` an try:
```
ape run scripts/accounts.py --network ethereum:goerli:alchemy
0x1e59ce931B4CFea3fe4B875411e280e173cB7A9C
0
<my_goerli_account ADDRESS>
319249932664448808
```
vs.
```
ape run scripts/accounts.py
0x1e59ce931B4CFea3fe4B875411e280e173cB7A9C
1000000000000000000000000
<my_goerli_account ADDRESS>
0
```
vs.
```
ape run scripts/accounts.py --network ethereum:local:hardhat
INFO: Starting 'Hardhat node' process.
0x1e59ce931B4CFea3fe4B875411e280e173cB7A9C
10000000000000000000000
<my_goerli_account ADDRESS>
0
INFO: Stopping 'Hardhat node' process.
```

#### Mainnet console

Create a new account like such: `ape accounts import my_mainnet_account`
Follow the steps:
```
Enter Private Key:
Create Passphrase:
Repeat for confirmation:
SUCCESS: A new account '<ADDRESS>' has been added with the id 'my_mainnet_account'
```

`ape console --network ethereum:mainnet:infura`

```python
#Check balance of my address
In [1]: accounts
Out[1]: [<KeyfileAccount address=0xe16Bd85C59f7A75350350676D798A1C193F9e7f0 alias=my_mainnet_account>, <KeyfileAccount address=0xe16Bd85C59f7A75350350676D798A1C193F9e7f0 alias=max_goerli>]

In [2]: a = accounts.load("my_mainnet_account")

In [3]: a
Out[3]: <KeyfileAccount address=0xe16Bd85C59f7A75350350676D798A1C193F9e7f0 alias=my_mainnet_account>

In [4]: a.balance
Out[4]: <Your account balance>
```

#### Deploying to local blockchain

Run `ape run scripts/deploy.py --network ethereum:local:hardhat`

#### Testing on a local blockchain

Run `ape test` or `ape test --network ethereum:local:hardhat`

#### Deploying to Goerli test blockchain

Run `ape run scripts/deploy.py --network ethereum:goerli:alchemy`



