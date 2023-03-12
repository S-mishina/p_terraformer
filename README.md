# p_terraformer

p_terraformer is a CLI that extends terraformer.

## support platform

The following environments are supported

* Darwin
* Linux

## install

terraformer must be installed to use p_terraformer.
To install terraformer from official sources, please check the following documentation.
An installation program is provided in this repository.


```:terminal
python terraformer_install.py
```

To install p_terraformer yourself, you will need to execute the following code


```:terminal
python setup.py install
```

## quick

### How to register for secret

```:terminal
$ p_terraformer profile

---output---
Please enter a profile name >hogehoge
secret manager api_key >hogehoge
secret manager app_key >hogehoge
```

You can set up a profile by executing the above command and entering each item
The information entered is recorded in `.p_terraformer/config.yaml`.

```:output
---example---
profile:
- name: hogehoge
  api_key: hogehoge
  app_key: hogehoge
```

### Datadog
#### When using aws secret manager

* Generate dashboard

```:terminal
$ p_terraformer datadog aws_secret -p hogehoge --resource dashboard --resource_id hogehoge
```

Resource can be generated by entering the name of the resource you wish to generate in --resource and entering the corresponding resource id.

※ you must register a secret in the profile

### When using secret default

```:terminal
$ p_terraformer datadog default_secret --api_key hogehoge --app_key hogehoge--resource dashboard --resource_id hogehoge
```
