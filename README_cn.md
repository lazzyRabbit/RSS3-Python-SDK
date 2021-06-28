# RSS3 Python SDK

python3 version：v3.9.X  
这是一个还未完全跑通的rss3 python sdk

## 当前暂未解决问题

* 由于时间开发的关系，签名问题暂未解决，导致流程参数暂未调通   
  这里的坑是开发中遇到的，发现eth_keys和rss3中所用到sign会有不兼容性的问题，这里大概使用的库的兼容性问题   
  同样的问题go的官方库中也遇到了类似的问题   
  [rss3go_lib](https://github.com/nyawork/rss3go) 中解决了这个问题  
  
* 由于时间开发的关系，测试用例暂未编写完整 
* 由于开发时间的关系，暂未跟得上RSS3-SDK-for-JavaScript的步伐，目前的版本是围绕第一版RSS3-SDK-for-JavaScript第一版进行开发的

## API

### Account

```python
    from rss3_sdk import rss3_account
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
    endpoint = 'rss3-hub-playground-6raed.ondigitalocean.app',
    rss3_account = curr_account,
    fill_update_callback = fill_update)
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

* 解决签名问题，将整体接口调通，完成第一个版本的发布，将工具包推送到pip上
* 以最跟进新版本官方的js版本的SDK进行开发，将模块拆分得更细，将file、item、items拆分开

## 最后呼吁
* 由于本人时间过少，踩坑多，所以希望有时间的同僚多提宝贵意见以及共同合作开发