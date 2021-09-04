# Walmart Business API wrapper

> __NOT DOCUMENTED YET & WORK-IN-PROGRESS__

_Contributions are Welcomed!_

__Code Samples__

```python
from walmart import Walmart
from pprint import pprint

def main():
  walmart = Walmart(
    'de154667-5b40-49b2-a4e8-77f906749127',
    'AOJMTaoR85oHSdmEZGeuAANzcEaaUKi5DP1Q_rCyuAZdYEfIVkAX9yamOUJ8XUCe1wjd-Vc8JBV6yUw3h0sEDg',
  )

  orders = walmart.report.recon_report('06092020')
  with open('./files/recon.zip', 'wb') as f:
    f.write(orders)
  pprint(orders)

  report = walmart.report.get_report('item')
  with open('./files/reports.zip', 'wb') as f:
    f.write(report)

if __name__ == '__main__':
  main()
```

__Methods__

```python
help()
```
