# -*- coding: utf-8 -*-
# IMPORTS
from typing import Dict, List, Union, Tuple, Optional

# LOCAL IMPORTS
from walmart.core import Resource

class WalmartItems(Resource):
  """
  Items
  """

  path = 'items'

  def count(
    self,
    status: str = 'PUBLISHED'
  ) -> Dict:
    """
    "PUBLISHED"
    "UNPUBLISHED"
    "SYSTEM_PROBLEM"
    "IN_PROGRESS"
    "ALL"
    """
    url = 'count'
    return self.connection.send_request(
      method='GET',
      url='{}/{}'.format(self.url, url),
      params={'status': status}
    )

  def get_item(
    self,
    id: str,
    product_type: str
  ) -> Dict:
    """
    "GTIN"
    "UPC"
    "ISBN"
    "EAN"
    "SKU"
    "ITEM_ID"
    """
    return self.connection.send_request(
      method='GET',
      url='{}/{}'.format(self.url, id),
      params={'productIdType': product_type}
    )

  def all_items(
    self,
    sku: str = '',
    offset: str = '0',
    limit: str = '20',
    life_cycle_status: str = 'ACTIVE',
    published_status: str = 'PUBLISHED',
    next_curson: str = '*'
  ) -> Dict:
    """
    "ACTIVE"
    "INACTIVE"
    "ALL"
    """
    return self.connection.send_request(
      method='GET',
      url=self.url,
      params={
        'sku': sku,
        'offset': offset,
        'limit': limit,
        'lifeCycleStatus': life_cycle_status,
        'publishedStatus': published_status,
        'nextCursor': next_curson
      }
    )

  @property
  def taxonomy(self) -> Dict:
    url = 'taxonomy'
    return self.connection.send_request(
      method='GET',
      url='{}/{}'.format(self.url, url)
    )

  def search(
    self,
    query: str = '',
    upc: str = '',
    gtin: str = ''
  ) -> Dict:
    url = 'walmart/search'
    self.connection.send_request(
      method='GET',
      url='{}/{}'.format(self.url, url),
      params={
        'query': query,
        'upc': upc,
        'gtin': gtin
      }
    )
