# -*- coding: utf-8 -*-
# IMPORTS
from datetime import datetime
from typing import Dict, List, Union, Tuple, Optional

# LOCAL IMPORTS
from .core import Core
from .lib.report import Report
from .lib.orders import Orders
from .lib.inventory import Inventory
from .lib.items import WalmartItems

def epoch_milliseconds(dt: int) -> int:
  "Walmart accepts timestamps as epoch time in milliseconds"
  epoch = datetime.utcfromtimestamp(0)
  return int((dt - epoch).total_seconds() * 1000.0)

class Walmart(Core):
  def __init__(
    self,
    client_id: str,
    client_secret: str
  ) -> object:
    """To get client_id and client_secret for your Walmart Marketplace
    visit: https://developer.walmart.com/#/generateKey
    """
    super(Walmart, self).__init__(client_id, client_secret)

  @property
  def report(self):
    return Report(connection=self)

  @property
  def orders(self):
    return Orders(connection=self)

  @property
  def items(self):
    return WalmartItems(connection=self)

  @property
  def inventory(self):
    return Inventory(connection=self)

