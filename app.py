import os
from pprint import pprint
from walmart import Walmart

def main():
  walmart = Walmart(
    'de154667-5b40-49b2-a4e8-77f906749127',
    'AOJMTaoR85oHSdmEZGeuAANzcEaaUKi5DP1Q_rCyuAZdYEfIVkAX9yamOUJ8XUCe1wjd-Vc8JBV6yUw3h0sEDg',
  )

  # # https://developer.walmart.com/api/us/mp/orders
  # all_orders = walmart.orders.all_orders('2021-07-03', '2021-08-03')
  # pprint(all_orders)
  # single_detail = walmart.orders.single_detail('2812146864864')
  # pprint(single_detail)
  # released = walmart.orders.released()
  # pprint(released)

  # # https://developer.walmart.com/api/us/mp/items
  # all_items = walmart.items.all_items()
  # pprint(all_items)
  # taxonomy = walmart.items.taxonomy
  # pprint(taxonomy)
  # search_result = walmart.items.search('Oil')
  # pprint(search_result)
  # item_count = walmart.items.count()
  # print(item_count)
  # get_item = walmart.items.get_item('00363307970460', 'GTIN')
  # pprint(get_item)

  # # https://developer.walmart.com/api/us/mp/inventory
  # inventory_all = walmart.inventory.all()
  # pprint(inventory_all)
  # single_item_from_inventory = walmart.inventory.inventory('ANHS-SCFR-8-8')
  # pprint(single_item_from_inventory)
  # wfs_inventory = walmart.inventory.wfs_inventory(
  #     'ANHS-SCFR-8-8', '03072021', '03082021')
  # pprint(wfs_inventory)
  # single_by_ship = walmart.inventory.single_by_ship('ANVA-1014')
  # pprint(single_by_ship)

  # # https://developer.walmart.com/api/us/mp/reports
  # # https://developer.walmart.com/us/whats-new/new-item-performance-report/
  # available_reports = walmart.report.available
  # pprint(available_reports)
  # recon_reports = walmart.report.recon_report(
  #     available_reports.get('availableApReportDates')[0])
  # pprint(recon_reports)
  # single_report = walmart.report.get_report('cpa')
  # pprint(single_report)

  # # https://developer.walmart.com/api/us/mp/insights#operation/getListingQualityScore
  # unpublished_items = walmart.insights.unpublished('2020-06-03')
  # pprint(unpublished_items)
  # unpublished_items_count = walmart.insights.unpublished_count('2020-06-03')
  # pprint(unpublished_items_count)
  quality_scores = walmart.insights.quality_score()
  pprint(quality_scores)
  # trending_items = walmart.insights.trending_items()
  # pprint(trending_items)
  # listing_quality_issue_categories = walmart.insights.listing_quality_issue_categories()
  # pprint(listing_quality_issue_categories)
  # unpublished_insights = walmart.insights.unpublished()
  # pprint(unpublished_insights)
  # unpublished_insights_count = walmart.insights.unpublished_count('2021-01-03')
  # pprint(unpublished_insights_count)


if __name__ == '__main__':
  if not os.path.isdir(os.path.join(os.getcwd(), 'reports')):
    os.mkdir('reports')
  main()
