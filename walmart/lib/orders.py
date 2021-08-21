# -*- coding: utf-8 -*-
# IMPORTS
from typing import Dict

# LOCAL IMPORTS
from walmart.core import Resource

class Orders(Resource):
  """
  Orders
  """

  path = 'orders'

  def all_orders(
    self,
    startdate: str,
    enddate: str
  ) -> Dict:
    url = '/orders'
    return self.connection.send_request(
      method='GET',
      url=self.url,
      params={
        'createdStartDate': startdate,
        'createdEndDate': enddate
      }
    )

  def single_detail(
    self,
    orderid: str
  ) -> Dict:
    return self.connection.send_request(
      method='GET',
      url='{}/{}'.format(self.url, orderid)
    )

  def released(self) -> Dict:
    url = 'released'
    return self.connection.send_request(
      method='GET',
      url='{}/{}'.format(self.url, url)
    )
