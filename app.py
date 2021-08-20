from pprint import pprint
from walmart import Walmart

def main():
  walmart = Walmart(
    'de154667-5b40-49b2-a4e8-77f906749127',
    'AOJMTaoR85oHSdmEZGeuAANzcEaaUKi5DP1Q_rCyuAZdYEfIVkAX9yamOUJ8XUCe1wjd-Vc8JBV6yUw3h0sEDg',
  )

  start_date= "2020-01-01"
  end_date= "2020-01-31"

  # orders = walmart.report.recon_report('06092020')
  # with open('./files/recon.zip', 'wb') as f:
  #   f.write(orders)
  # pprint(orders)

  report = walmart.report.get_report('item')
  # pprint(report)
  with open('./files/reports.zip', 'wb') as f:
    f.write(report)

  # AN = (
  #   'de154667-5b40-49b2-a4e8-77f906749127',
  #   'AOJMTaoR85oHSdmEZGeuAANzcEaaUKi5DP1Q_rCyuAZdYEfIVkAX9yamOUJ8XUCe1wjd-Vc8JBV6yUw3h0sEDg',
  # )


if __name__ == '__main__':
  main()
