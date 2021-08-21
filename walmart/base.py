# -*- coding: utf-8 -*-
# IMPORTS
from typing import Dict, List, Union, Tuple, Optional

# LOCAL IMPORTS
from walmart.core import Core
from walmart.lib.report import Report
from walmart.lib.orders import Orders
from walmart.lib.insights import Insights
from walmart.lib.inventory import Inventory
from walmart.lib.items import WalmartItems

class Walmart(Core):
  def __init__(
    self,
    client_id: str,
    client_secret: str
  ) -> object:
    """
    To get client_id and client_secret for your Walmart Marketplace
    visit: https://developer.walmart.com/#/generateKey
    """
    super(Walmart, self).__init__(client_id, client_secret)

  @property
  def report(self) -> Report:
    return Report(connection=self)

  @property
  def orders(self) -> Orders:
    return Orders(connection=self)

  @property
  def items(self) -> WalmartItems:
    return WalmartItems(connection=self)

  @property
  def inventory(self) -> Inventory:
    return Inventory(connection=self)

  @property
  def insights(self) -> Insights:
    return Insights(connection=self)

