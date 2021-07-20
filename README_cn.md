# RSS3 Python SDK

python3 version：v3.9.X  
版本0.1.0 beta版

## 当前暂未解决问题
  
* 由于时间开发的关系，测试用例暂未编写完整 
* 由于开发时间的关系，暂时跟上了第一版的开发进程，当然，后期会优化的更加全面

## 修复问题

* sign 签名机制的问题

## API

### Account

```python

from rss3_sdk.module.base import account
```

#### 生成一个新的账户

```python
    curr_account = rss3_account.RSS3Account()
```

#### 用原来的私钥进行初始化

```python
    curr_account = rss3_account.RSS3Account('0xa55afab0f35bdc00c1ac137a98d5d037609eeaead8ba930c4c3878e38630e38a')
```

### RSS3Handle

```python
    from rss3_sdk import rss3_handle
```

#### 初始化

```python
    handle = rss3_handle.RSS3Handle(
    endpoint = 'hub.rss3.io',
    rss3_account = curr_account)
```

#### 获取并修改item

```python
    # The type of'inn_item' is IInnItem, you can also generate a new one yourself
    
    inn_item = handle.item_get('0x6338ee94fB85e157D117d681E808a34a9aC21f31-item-1')
    inn_item.title = "Change this one"
    handle.item_patch(inn_item)
```

#### 用户信息修改

```python
    # The type of'inn_profile' is IInnProfile, you can also generate a new one yourself
    
    inn_profile = handle.profile_get()
    inn_profile.name = "Child"
    handle.profile_patch(inn_profile)
```

## 下一步计划

* 以最跟进新版本官方的js版本的SDK进行开发(会略有区别)，将模块拆分得更细，将file、item、items拆分开后，发布到pip上

## 最后呼吁
* 由于本人时间过少，踩坑多，所以希望有时间的同僚多提宝贵意见以及共同合作开发