# -*- coding: utf-8 -*-
# IMPORTS
from typing import Dict, List, Union, Tuple, Optional

# LOCAL IMPORTS
from walmart.core import Resource

class Inventory(Resource):
  """
  Items
  """

  path = 'inventories'

  def all(
    self,
    limit: str = '10',
    next: str = ''
  ) -> Dict:
    """A list of all items in the inventory

    Args:
        limit (str, optional): [description]. Defaults to '10'.
        next (str, optional): [description]. Defaults to ''.

    Returns:
        Dict: [description]
    """
    return self.connection.send_request(
        method='GET',
        url=self.url,
        params={
          'limit': limit,
          'nextCursor': next
        }
    )

  def inventory(
    self,
    sku: str,
    ship_node: str = ''
  ) -> Dict:
    """A single item in the inventory

    Args:
        sku (str): [description]
        ship_node (str, optional): [description]. Defaults to ''.

    Returns:
        Dict: [description]
    """
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
    sku: str = '',
    from_modified_date: str = '',
    to_modified_date: str = '',
    limit: str = '10',
    offset: str = '0'
  ) -> Dict:
    """A list of all items in the inventory by WFS

    Args:
        sku (str, optional): [description]. Defaults to ''.
        from_modified_date (str, optional): [description]. Defaults to ''.
        to_modified_date (str, optional): [description]. Defaults to ''.
        limit (str, optional): [description]. Defaults to '10'.
        offset (str, optional): [description]. Defaults to '0'.

    Returns:
        Dict: [description]
    """
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

  def single_by_ship(
    self,
    sku: str,
    ship_node: str = ''
  ) -> Dict:
    """A single item in the inventory by Spipping number

    Args:
        sku (str): [description]
        ship_node (str, optional): [description]. Defaults to ''.

    Returns:
        Dict: [description]
    """
    return self.connection.send_request(
        method='GET',
        url='{}/{}'.format(self.url, sku),
        params={
          'shipNode': ship_node
        }
    )
