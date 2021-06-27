# RSS3 Python SDK

这是一个还未完全跑通的rss3 python sdk

## 当前暂未解决问题

* 签名问题
* 由于开发时间的关系，暂未跟得上RSS3-SDK-for-JavaScript的步伐，目前的版本是围绕第一版RSS3-SDK-for-JavaScript第一版进行开发的

## API

### Account

```
from rss3_sdk import rss3_accountss
```

#### 生成一个新的账户

```
    curr_account = rss3_account.RSS3Account()
```

#### 用原来的私钥进行初始化

```
    curr_account = rss3_account.RSS3Account('0xa55afab0f35bdc00c1ac137a98d5d037609eeaead8ba930c4c3878e38630e38a')
```

### RSS3Handle

#### 初始化

```
    
```

#### 获取item

```python

```

#### 修改item

```python

```

#### 用户信息修改

```python

```