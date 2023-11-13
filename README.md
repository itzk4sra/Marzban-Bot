# Marzban-Bot
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![GitHub issues](https://img.shields.io/github/issues/Imk4sra/Marzban-Bot)](https://github.com/Imk4sra/Marzban-Bot/issues)
[![GitHub stars](https://img.shields.io/github/stars/Imk4sra/Marzban-Bot)](https://github.com/Imk4sra/Marzban-Bot/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Imk4sra/Marzban-Bot)](https://github.com/Imk4sra/Marzban-Bot/network)

A Python Discord bot that simplifies the usage of [Marzban](https://github.com/Gozargah/Marzban)'s Panel.

## Requirements
```
pip install uuid
pip install discord
pip install marzpy
```

## Add Plan for Create Server
```python
if Data is not None:
    if Data == "plan1" or Data == "Plan1":
        gigabytes = float(20)
        bytes = gigabytes_to_bytes(gigabytes)
    if Data == "plan2" or Data == "Plan2":
        gigabytes = float(30)
        bytes = gigabytes_to_bytes(gigabytes)
    if Data == "plan3" or Data == "Plan3":
        gigabytes = float(40)
        bytes = gigabytes_to_bytes(gigabytes)
    if Data == "plan4" or Data == "Plan4":
        gigabytes = float(50)
        bytes = gigabytes_to_bytes(gigabytes)
    else:
        gigabytes = float(Data)
        bytes = gigabytes_to_bytes(gigabytes)
else:
    bytes = 0
```
### Replace this with 
```python
if Data is not None:
        gigabytes = float(Data)
        bytes = gigabytes_to_bytes(gigabytes)
else:
    bytes = 0
```

<div align="center">
  <p>
    <sub>© 2023 Imk4sra</sub>
  </p>
</div>
