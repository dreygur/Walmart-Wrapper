# -*- coding: utf-8 -*-
# IMPORTS
from typing import Dict, List, Union, Tuple, Optional

# LOCAL IMPORTS
from ..core import Resource

class Orders(Resource):
  """
  Orders
  """

  path = 'orders'

  def all_orders(self, startdate, enddate):
    url = '/orders'
    return self.connection.send_request(
        method='GET',
        url=self.url,
        params={
            'createdStartDate': startdate,
            'createdEndDate': enddate
        }
    )

  def single_detail(self, orderid):
    return self.connection.send_request(
        method='GET',
        url='{}/{}'.format(self.url, orderid)
    )

  def released(self):
    url = 'released'
    return self.connection.send_request(
        method='GET',
        url='{}/{}'.format(self.url, url)
    )
