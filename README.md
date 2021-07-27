# RSS3 Python SDK

python3 version: v3.9.X  
SDK version: 0.1.0-alpha

## Current issues to be resolved

* Due to time development, the test case has not yet been written completely
* Due to the development time, I have temporarily kept up with the development process of the first version. Of course, it will be optimized more comprehensively in the later period.

## Fix the problem

* Sign signature mechanism

## API

### Account

```python

from rss3_sdk.until import account
```

#### Generate a new account

```python
    curr_account = rss3_account.RSS3Account()
```

#### Initialize with the original private key

```python
    curr_account = rss3_account.RSS3Account('0x47e18d6c386898b424025cd9db446f779ef24ad33a26c499c87bb3d9372540ba')
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

* Develop with the latest official js version of the SDK (there will be slightly different), split the module into more detail, split the file, item, and items, and publish it to pip


## Final appeal
 Since I have too little time and stepped on more pits, I hope that colleagues who have the time can give more valuable opinions and cooperate in development.
