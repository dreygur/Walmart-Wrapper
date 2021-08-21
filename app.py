from pprint import pprint
from walmart import Walmart

def items(walmart, status="ALL"):
  item = walmart.items.count()
  pprint(item)

def all_orders(walmart, start_date, end_date):
  orders = walmart.orders.all_orders(start_date, end_date)
  pprint(orders)

def all_items(walmart):
  items = walmart.items.all()
  pprint(items)

def main():
  walmart = Walmart(
    'de154667-5b40-49b2-a4e8-77f906749127',
    'AOJMTaoR85oHSdmEZGeuAANzcEaaUKi5DP1Q_rCyuAZdYEfIVkAX9yamOUJ8XUCe1wjd-Vc8JBV6yUw3h0sEDg',
  )

  # pprint(items(walmart))
  # all_items(walmart)
  # pprint(walmart.items.taxonomy)
  # pprint(walmart.items.search('Tires'))
  # pprint(walmart.inventory.all())
  pprint(walmart.insights.unpublished_count('2021-08-18'))

  start_date= "2021-06-01"
  end_date= "2021-08-05"

  # all_orders(walmart, start_date, end_date)
  # single = walmart.report.orders.single_detail('2812168160232')
  # pprint(single)

  # single = walmart.orders.released()
  # pprint(single)

  # orders = walmart.report.recon_report('06092020')
  # with open('./files/recon.zip', 'wb') as f:
  #   f.write(orders)
  # pprint(orders)

  # report = walmart.report.get_report('item')
  # # pprint(report)
  # with open('./files/reports.zip', 'wb') as f:
  #   f.write(report)

  # AN = (
  #   'de154667-5b40-49b2-a4e8-77f906749127',
  #   'AOJMTaoR85oHSdmEZGeuAANzcEaaUKi5DP1Q_rCyuAZdYEfIVkAX9yamOUJ8XUCe1wjd-Vc8JBV6yUw3h0sEDg',
  # )

  # items(walmart)



if __name__ == '__main__':
  main()
