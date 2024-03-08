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
from walmart.lib.onrequest import ONRequest

class Walmart(Core):
  def __init__(
    self,
    client_id: str,
    client_secret: str
  ) -> object:
    """Walmart API Client

    Args:
        client_id (str): [description]
        client_secret (str): [description]

    Returns:
        object: [description]
    """
    super(Walmart, self).__init__(client_id, client_secret)

  @property
  def report(self) -> Report:
    """Report

    Returns:
        Report: [description]
    """
    return Report(connection=self)

  @property
  def orders(self) -> Orders:
    """Orders

    Returns:
        Orders: [description]
    """
    return Orders(connection=self)

  @property
  def items(self) -> WalmartItems:
    """Items

    Returns:
        WalmartItems: [description]
    """
    return WalmartItems(connection=self)

  @property
  def inventory(self) -> Inventory:
    """Inventory

    Returns:
        Inventory: [description]
    """
    return Inventory(connection=self)

  @property
  def insights(self) -> Insights:
    """Insights

    Returns:
        Insights: [description]
    """
    return Insights(connection=self)
  
  @property
  def onreport(self)->ONRequest:
    """ON Request

    Returns:
      ONRequest: [description]
    """
    return ONRequest(connection=self)