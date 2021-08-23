from pprint import pprint
from walmart import Walmart

def main():
  walmart = Walmart(
    'de154667-5b40-49b2-a4e8-77f906749127',
    'AOJMTaoR85oHSdmEZGeuAANzcEaaUKi5DP1Q_rCyuAZdYEfIVkAX9yamOUJ8XUCe1wjd-Vc8JBV6yUw3h0sEDg',
  )

  # # Get a list of all products
  # reports = walmart.report.available
  # # pprint(reports)
  # recon_report = walmart.report.recon_report(reports['availableApReportDates'][0])
  # with open('files/recon_report.zip', 'wb') as f:
  #   f.write(recon_report)

  # Get Items Taxonomies
  items = walmart.items.taxonomy
  pprint(items)

if __name__ == '__main__':
  main()
