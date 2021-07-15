# RSS3 Python SDK

python3 version：v3.9.X  
This is a python sdk that is not fully accessible yet  

## Current issues to be resolved
    
* Due to time development, the test cases are not yet complete
* Due to the development time, we have not kept up with the pace of RSS3-SDK-for-JavaScript. The current version is developed around the first version of RSS3-SDK-for-JavaScript.

## API

### Account

```python

from rss3_sdk.until2 import account
```

#### Generate a new account

```python
    curr_account = rss3_account.RSS3Account()
```

#### Initialize with the original private key

```python
    curr_account = rss3_account.RSS3Account('0xa55afab0f35bdc00c1ac137a98d5d037609eeaead8ba930c4c3878e38630e38a')
```

### RSS3Handle

```python
    from rss3_sdk import rss3_handle
```

#### Initialization

```python
    handle = rss3_handle.RSS3Handle(
    endpoint = 'rss3-hub-playground-6raed.ondigitalocean.app',
    rss3_account = curr_account,
    fill_update_callback = fill_update)
```

#### Get and modify item

```python
    # The type of'inn_item' is IInnItem, you can also generate a new one yourself
    
    inn_item = handle.item_get('0x6338ee94fB85e157D117d681E808a34a9aC21f31-item-1')
    inn_item.title = "Change this one"
    handle.item_patch(inn_item)
```

#### User information modification

```python
    # The type of'inn_profile' is IInnProfile, you can also generate a new one yourself
    
    inn_profile = handle.profile_get()
    inn_profile.name = "Child"
    handle.profile_patch(inn_profile)
```

## Next step plan

* Solve the signature problem, adjust the overall interface, complete the release of the first version, and push the toolkit to pip
* Develop with the latest official js version of the SDK, split the module into more detail, and separate the file, item, and items.

## Final appeal
 Since I have too little time and stepped on more pits, I hope that colleagues who have the time can give more valuable opinions and cooperate in development.