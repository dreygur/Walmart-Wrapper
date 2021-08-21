# -*- coding: utf-8 -*-
# IMPORTS
from typing import Dict, List, Union, Tuple, Optional

# LOCAL IMPORTS
from ..core import Resource

class Inventory(Resource):
  """
  Items
  """

  path = 'inventories'

  def all(self, limit='10', next=''):

    return self.connection.send_request(
        method='GET',
        url=self.url,
        params={
          'limit': limit,
          'nextCursor': next
        }
    )

  def inventory(self, sku, ship_node=''):
    url = 'inventory'
    return self.connection.send_request(
      method='GET',
      url='{}/{}'.format(self.connection.base_url, url),
      params={
        'sku': sku,
        'shipNode': ship_node
      }
    )

  def wfs_inventory(
    self,
    sku='',
    from_modified_date='',
    to_modified_date='',
    limit='10',
    offset='0'
  ):
    url = 'fulfillment/inventory'
    return self.connection.send_request(
      method='GET',
      url='{}/{}'.format(self.connection.base_url, url),
      params={
        'sku': sku,
        'fromModifiedDate': from_modified_date,
        'toModifiedDate': to_modified_date,
        'limit': limit,
        'offset': offset
      }
    )

  def single_by_ship(self, sku, ship_node=''):
    return self.connection.send_request(
        method='GET',
        url='{}/{}'.format(self.url, sku),
        params={
          'shipNode': ship_node
        }
    )
